#!/usr/bin/python3

import sys


def main():
    with open(sys.argv[1]) as input_file:
        content = [line.strip('\n') for line in input_file.readlines()]

    case_count = int(content[0])

    with open('output', 'w') as output_file:
        for case_number in range(1, case_count + 1):
            case_input = content[case_number]

            # Do computations here
            result = case_input

            output_file.write('Case #' + str(case_number) + ": " + result + '\n')


if __name__ == '__main__':
    main()
