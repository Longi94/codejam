#!/usr/bin/python3
import sys


stats = [0] * 200


def main():
    case_count = int(input())

    for case_number in range(1, case_count + 1):
        lollipop_count = int(input())

        if lollipop_count == -1:
            break

        lollipops = set(range(lollipop_count))

        for i in range(lollipop_count):
            liked = list(map(lambda x: int(x), input().split(" ")[1::]))

            # Do computations here
            result = get_lollipop(lollipops, liked)

            if result >= 0:
                lollipops.remove(result)

            for lollipop in liked:
                stats[lollipop] = stats[lollipop] + 1

            print(str(result))
            sys.stdout.flush()


def get_lollipop(lollipops, liked):
    sellable = lollipops.intersection(liked)

    if len(sellable) == 0:
        return -1

    min_liked = -1

    for lollipop in sellable:
        if min_liked == -1 or stats[min_liked] > stats[lollipop]:
            min_liked = lollipop

    return min_liked


if __name__ == '__main__':
    main()
