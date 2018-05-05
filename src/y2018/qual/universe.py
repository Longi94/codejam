#!/usr/bin/python3


def main():

    case_count = int(input())

    for case_number in range(1, case_count + 1):
        case_input = input().split(" ")

        # Do computations here
        result = calculate_switches(int(case_input[0]), case_input[1])

        print("Case #{}: {}".format(case_number, result))
        

def calculate_switches(D, str):
    current_dmg = calculate_dmg(str)
    
    if current_dmg <= D:
        return "0"
    
    if 'S' not in str or 'C' not in str:
        return "IMPOSSIBLE"
            
    s_count = str.count('S')
    
    if (s_count > D):
        return "IMPOSSIBLE"

    c_count = str.count('C')
    
    return calc_rec(D, str, current_dmg, c_count)
    
    
def calc_rec(D, str, current_dmg, c_count):

    if D >= current_dmg:
        return 0

    if str[-1] == 'C':
        return calc_rec(D, str[:-1], current_dmg, c_count - 1)
    
    i = str.rfind('C')
    
    return calc_rec(D, str[:i] + 'SC' + str[i + 2:], current_dmg - pow(2, c_count - 1), c_count) + 1


def calculate_dmg(str):
    dmg = 0
    power = 1
    
    for ch in str:
        if ch == 'C':
            power = power * 2
        if ch == 'S':
            dmg = dmg + power
    
    return dmg


if __name__ == '__main__':
    main()
