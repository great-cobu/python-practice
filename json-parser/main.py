import argparse
from argparse import Namespace
from statistics import median


def grab():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    parser.add_argument('--median', dest='accumulate', action='store_const',
                        const=median, default=max,
                        help='find the median of integers (default: find the max)')
    return parser.parse_args()


def run(opt: Namespace):
    function = opt.accumulate
    integers = opt.integers
    print(function(integers))


if __name__ == '__main__':
    opt = grab()
    print(opt)
    run(opt)