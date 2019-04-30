import numpy as np


def get_result(c_skill, d_skill, n, k):
    if n == 0:
        return 0

    if n == 1:
        return 1 if abs(c_skill[0] - d_skill[0]) <= k else 0

    c_max = c_skill.max()
    d_max = d_skill.max()

    if c_max > d_max + k:
        ci = c_skill.argmax()
        return get_result(c_skill[: ci], d_skill[: ci], ci, k) + \
               get_result(c_skill[ci + 1:], d_skill[ci + 1:], n - ci - 1, k)
    elif c_max + k < d_max:
        di = d_skill.argmax()
        return get_result(c_skill[: di], d_skill[: di], di, k) + \
               get_result(c_skill[di + 1:], d_skill[di + 1:], n - di - 1, k)

    c_indices = np.where(c_skill == c_max)[0]
    d_indices = np.where(d_skill == d_max)[0]

    equals = (c_indices == d_indices)

    if equals.any():
        equal_index = (c_indices == d_indices).argmax()
        return get_result(c_skill[: equal_index], d_skill[: equal_index], equal_index, k) + \
               get_result(c_skill[equal_index + 1:], d_skill[equal_index + 1:], n - equal_index - 1, k) + \
               (equal_index + 1) * (n - equal_index)

    fair = 0
    for j in range(n):
        for l in range(j + 1, n + 1):
            diff = abs(max(c_skill[j:l]) - max(d_skill[j:l]))
            if diff <= k:
                fair += 1

    return fair


t = int(input())
for i in range(1, t + 1):
    n, k = input().split(' ')
    n = int(n)
    k = int(k)

    c_skill = input().split(' ')
    d_skill = input().split(' ')

    c_skill = np.array(list(map(int, c_skill)))
    d_skill = np.array(list(map(int, d_skill)))

    result = get_result(c_skill, d_skill, n, k)

    print("Case #{}: {}".format(i, result))
