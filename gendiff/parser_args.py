import argparse


def get_args():
    parser = argparse.ArgumentParser(prog='gendiff', description='Compares two configuration files and shows a difference.') # noqa E501
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', metavar='FORMAT', help='set format of output') # noqa E501
    args = parser.parse_args()
    return args
