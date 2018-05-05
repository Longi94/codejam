#!/usr/bin/python3

import math


def main():

    case_count = int(input())

    for case_number in range(1, case_count + 1):
        A = float(input())

        print("Case #{}:".format(case_number))
        
        angle = get_angle(A)
        
        print("{} {} 0".format(math.cos(angle) * 0.5, math.sin(angle) * 0.5))

        print("{} {} 0".format(math.cos(angle + (math.pi / 2)) * 0.5, math.sin(angle + (math.pi / 2)) * 0.5))
        
        print("0 0 0.5")


def get_angle(area):
    return math.asin(area / math.sqrt(2)) - (math.pi / 4)

        
if __name__ == '__main__':
    main()
