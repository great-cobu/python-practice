import argparse
import sys
import json
from statistics import median

import bunch
import pathlib as pl


def create_parser():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    parser.add_argument('--median', dest='accumulate', action='store_const',
                        const=median, default=max,
                        help='find the median of integers (default: find the max)')
    return parser


class MockParser:
    """
    This creates a fake set of commandline options for testing.
    """
    @staticmethod
    def parse_args():
        opt = bunch.Bunch()
        opt['integers'] = [1, 2, 3, 4]
        opt['accumulate'] = lambda x: median(x)
        return opt


def main():
    parser = create_parser()
    opt = parser.parse_args()
    print(sys.argv)
    print(opt)
    function = opt.accumulate
    integers = opt.integers
    print(function(integers))

def parse_json():
    s = '{"id":"01", "name": "Emily", "language": ["C++", "Python"]}'
    #path = pl.Path('/Users/wishitventuresllc/Projects/github/python-practice/sample_json.json')
    #print(path.exists())
    #f = open('/Users/wishitventuresllc/Projects/github/python-practice/sample_json.json', 'rb')
    #employee_dict = json.loads(s)
    #employee_dict = json.loads(f)
    #print(employee_dict)

    with open('/sample_json.json', 'r') as f:
        data = json.load(f)
        print(json.dumps(data, indent=4, sort_keys=True)) # Pretty print
        # print(data)


if __name__ == '__main__':
    #main()
    parse_json()
