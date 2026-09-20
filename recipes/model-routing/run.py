#!/usr/bin/env python3
"""Inspect a routing request, test a fixture, or explicitly make one TypeSafe call."""
import argparse
import json
import math
import os
from pathlib import Path
import sys
import time
import urllib.error
import urllib.request

HERE = Path(__file__).resolve().parent
ENDPOINT = 'https://api.typesafe.ai/v1/systemone'


def probability(value):
    return type(value) in (int, float) and math.isfinite(value) and 0 <= value <= 1


def decide(response, min_confidence):
    """Model classification never executes the selected tier."""
    if not probability(min_confidence):
        raise ValueError('min_confidence must be between 0 and 1')
    if not isinstance(response, dict):
        return {'action': 'review', 'reason': 'invalid_response'}
    answers = response.get('answers')
    answer = answers.get('route') if isinstance(answers, dict) else None
    if not isinstance(answer, dict) or answer.get('type') != 'choice':
        return {'action': 'review', 'reason': 'missing_or_invalid_route'}
    choice, confidence, probs = answer.get('choice'), answer.get('confidence'), answer.get('probabilities')
    if choice not in ('fast', 'strong') or not probability(confidence):
        return {'action': 'review', 'reason': 'invalid_choice_or_confidence'}
    if not isinstance(probs, dict) or set(probs) != {'fast', 'strong'}:
        return {'action': 'review', 'reason': 'invalid_distribution'}
    if not all(probability(p) for p in probs.values()) or abs(sum(probs.values()) - 1) > 0.01:
        return {'action': 'review', 'reason': 'invalid_distribution'}
    if confidence < min_confidence:
        return {'action': 'review', 'reason': 'low_confidence', 'candidate': choice}
    return {'action': 'route', 'tier': choice, 'confidence': confidence}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--live', action='store_true', help='Send one billable request to TypeSafe')
    mode.add_argument('--response', type=Path, help='Read a saved response offline')
    parser.add_argument('--text', help='Replace the sample request text')
    parser.add_argument('--model', help='Explicit model ID; otherwise request.json default')
    parser.add_argument('--min-confidence', type=float, default=0.8, help='Illustrative review threshold, not calibrated')
    args = parser.parse_args(argv)
    if not probability(args.min_confidence):
        parser.error('--min-confidence must be a finite value between 0 and 1')
    payload = json.loads((HERE / 'request.json').read_text())
    if args.text is not None:
        if not args.text.strip():
            parser.error('--text must not be empty')
        payload['state']['request'] = args.text
    if args.model:
        payload['model'] = args.model
    if not args.live and not args.response:
        print(json.dumps({'mode': 'dry-run', 'endpoint': ENDPOINT, 'request': payload}, indent=2))
        return 0
    if args.response:
        response = json.loads(args.response.read_text())
        print(json.dumps({'mode': 'offline-response', 'synthetic': response.get('fixture') is True if isinstance(response, dict) else False,
                          'decision': decide(response, args.min_confidence)}, indent=2))
        return 0
    key = os.environ.get('TYPESAFE_API_KEY')
    if not key:
        parser.error('Set TYPESAFE_API_KEY for --live; never put it in request.json')
    request = urllib.request.Request(ENDPOINT, data=json.dumps(payload).encode(), headers={
        'Content-Type': 'application/json', 'Authorization': 'Bearer ' + key}, method='POST')
    start = time.monotonic()
    try:
        with urllib.request.build_opener(NoRedirect).open(request, timeout=30) as result:
            response = json.load(result)
    except (urllib.error.URLError, TimeoutError, OSError, ValueError) as error:
        # Do not echo provider error bodies, credentials, or send automatic retries.
        code = error.code if isinstance(error, urllib.error.HTTPError) else None
        print(json.dumps({'mode': 'live', 'decision': {'action': 'review', 'reason': 'request_failed'}, 'http_status': code}))
        return 1
    print(json.dumps({'mode': 'live', 'requested_model': payload['model'],
                      'elapsed_seconds': round(time.monotonic() - start, 4),
                      'raw_response': response, 'decision': decide(response, args.min_confidence)}, indent=2))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError) as error:
        print('Invalid local input: ' + str(error), file=sys.stderr)
        sys.exit(2)
