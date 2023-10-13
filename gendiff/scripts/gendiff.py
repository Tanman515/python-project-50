from gendiff.gendiff import generate_diff
from gendiff.parser_args import get_args


def main():
    args = get_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
