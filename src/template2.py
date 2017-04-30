with open('output', 'w') as output_file:
    t = int(input())
    for i in range(1, t + 1):
        n, m = [int(s) for s in input().split(" ")]

        output_file.write('Case #' + str(i) + ": " + str(n) + ' ' + str(m) + '\n')