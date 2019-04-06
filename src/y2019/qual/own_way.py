#!/usr/bin/python3


def main():
    t = int(input())

    for i in range(1, t + 1):
        n = int(input())
        lydia = input()

        result = get_path(n, lydia)

        print('Case #{}: {}'.format(i, result))


def get_path(n, lydia):
    result = ''

    pos_me = [0, 0]
    pos_lydia = [0, 0]

    for step in lydia:
        if pos_me == pos_lydia:
            step_me = 'S' if step == 'E' else 'E'
        else:
            if n - 1 == pos_me[0]:
                step_me = 'S'
            elif n - 1 == pos_me[1]:
                step_me = 'E'
            else:
                step_me = 'S' if step == 'E' else 'E'

        result += step_me

        if step == 'S':
            pos_lydia[1] += 1
        else:
            pos_lydia[0] += 1

        if step_me == 'S':
            pos_me[1] += 1
        else:
            pos_me[0] += 1

    return result


if __name__ == '__main__':
    main()
