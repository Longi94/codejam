t = int(input())
for i in range(1, t + 1):

    p, q = input().split(' ')
    p = int(p)
    q = int(q) + 1

    people = [input().split(' ') for _ in range(p)]

    grid = [0] * q
    for j in range(q):
        grid[j] = [0] * q

    for person in people:
        if person[2] == 'N':
            for j in range(int(person[1]) + 1, q):
                for k in range(q):
                    grid[j][k] += 1
        elif person[2] == 'S':
            for j in range(int(person[1])):
                for k in range(q):
                    grid[j][k] += 1
        elif person[2] == 'E':
            for j in range(int(person[0]) + 1, q):
                for k in range(q):
                    grid[k][j] += 1
        elif person[2] == 'W':
            for j in range(int(person[0])):
                for k in range(q):
                    grid[k][j] += 1

    max_val = -1
    max_coords = (0, 0)
    for j in range(q):
        for k in range(q):
            if grid[k][j] > max_val:
                max_val = grid[k][j]
                max_coords = (k, j)

    print("Case #{}: {} {}".format(i, max_coords[1], max_coords[0]))
