import os
import json
import argparse
import app
from app.fib import Fibonacci, ReversedFibonacci

BASE_DIR: str = os.path.dirname(os.path.abspath(app.__file__))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--s', help='start of sequence', type=int)
    parser.add_argument('--e', help='end of sequence', type=int)
    parser.add_argument('--r', help='reversed', default=False, type=bool)
    args = parser.parse_args()
    revers = args.r
    collection = ReversedFibonacci(args.e) if revers else Fibonacci(args.e)
    fp = os.path.join(BASE_DIR, 'result.txt')
    res = [_ for _ in collection][args.s:]
    with open(fp, 'w+') as f:
        f.write(json.dumps(res))
    print(f'result: {res}')
    print(f'You can check result in file {fp}')

