#!/usr/bin/python3


def main():

    case_count = int(input())

    for case_number in range(1, case_count + 1):
        N = int(input())
        V = [int(s) for s in input().split(" ")]

        # Do computations here
        result = calculate(V, N)

        print("Case #{}: {}".format(case_number, result))
        

def calculate(V, N):
    evens = sorted(V[::2])
    odds = sorted(V[1::2])

    result = [None]*(len(V))
    result[::2] = evens
    result[1::2] = odds

    for i in range(N - 1):
        if result[i] > result[i + 1]:
            return str(i)
    
    return "OK"

        
if __name__ == '__main__':
    main()
