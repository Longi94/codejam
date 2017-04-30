import math


def surface(pancakes):
    s = 0

    pancakes.sort(key=lambda x: x[0])
    for pancake in pancakes:
        s += 2 * math.pi * pancake[0] * pancake[1]

    return s + pow(pancakes[-1][0], 2) * math.pi


t = int(input())
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]

    pancakes = []

    for j in range(n):
        pancake = [int(s) for s in input().split(" ")]
        pancakes.append(pancake)

    pancakes.sort(key=lambda x: (2 * math.pi * x[0] * x[1], x[0]), reverse=True)

    result = surface(pancakes[:k])

    print("Case #{}: {}".format(i, result))