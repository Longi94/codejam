#!/usr/bin/python3


def main():
    case_count = int(input())

    for case_number in range(1, case_count + 1):
        ant_count = int(input())

        ant_weights = [int(x) for x in input().split(" ")]

        # Do computations here
        result = get_max_ant(ant_count, ant_weights)

        print("Case #{}: {}".format(case_number, result))


def get_max_ant(ant_count, ant_weights):

    first_overweight = find_first_overweight(ant_weights)

    if first_overweight == -1:
        return len(ant_weights)

    new_list1 = list(ant_weights)
    del new_list1[first_overweight]

    result1 = get_max_ant(ant_count - 1, new_list1)

    removed = [False] * ant_count

    previous_ants = ant_weights[:first_overweight]
    current_weight = sum(previous_ants)

    while current_weight > ant_weights[first_overweight] * 6:
        fattest = find_fattest(previous_ants, removed[:first_overweight])
        current_weight = current_weight - ant_weights[fattest]
        removed[fattest] = True

    new_list2 = list(ant_weights)

    for i in reversed(range(ant_count)):
        if removed[i]:
            del new_list2[i]

    result2 = get_max_ant(len(new_list2), new_list2)

    return max(result1, result2)


def find_fattest(weights, removed):
    fattest = -1
    for i in range(1, len(weights)):
        if removed[i]:
            continue

        if fattest == -1 or weights[i] > weights[fattest]:
            fattest = i

    return fattest


def find_first_overweight(weights):
    current_weight = 0
    for i in range(len(weights)):
        if current_weight > weights[i] * 6:
            return i
        current_weight = current_weight + weights[i]
    return -1


if __name__ == '__main__':
    main()
