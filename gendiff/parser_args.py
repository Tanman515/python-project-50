import argparse


def get_args():
    parser = argparse.ArgumentParser(prog='gendiff', description='Compares two configuration files and shows a difference.') # noqa E501
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', default='stylish', help='output format (default: "stylish")') # noqa E501
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()
    return args
