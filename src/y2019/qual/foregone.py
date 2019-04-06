#!/usr/bin/python3


def main():
    t = int(input())

    for i in range(1, t + 1):
        n = input()

        result = split(n)

        print('Case #{}: {} {}'.format(i, result[0], result[1]))


def split(number):
    num1 = ''
    num2 = ''
    for digit in number:
        if digit == '4':
            num1 += '2'
            num2 += '2'
        else:
            num1 += digit
            num2 += '0'

    return num1, num2.lstrip('0')


if __name__ == '__main__':
    main()
