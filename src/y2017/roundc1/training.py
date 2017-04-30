from operator import mul
import functools

t = int(input())
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]

    u = float(input())

    p = [float(s) for s in input().split(" ")]


    while u > 0.0000001:
        p.sort()
        min_p = min(p)

        j = 0
        for k in range(len(p)):
            j = k
            if j == len(p) - 1 or p[j+1] - p[j] > 0.0000001:
                break

        j += 1

        if len(p) == j:
            p = [x + u / len(p) for x in p]
            break
        else:
            diff = p[j] - p[j - 1]
            p = [x + min(diff, u / j) for x in p[:j]] + p[j:]
            u -= min(diff, u / j) * j

    result = functools.reduce(mul, p, 1)

    print('Case #' + str(i) + ": " + str(result))