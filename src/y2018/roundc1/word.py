#!/usr/bin/python3
import collections


def main():
    case_count = int(input())

    for case_number in range(1, case_count + 1):
        case_input = input().split(" ")

        word_count = int(case_input[0])
        word_length = int(case_input[1])

        words = [input() for i in range(word_count)]
        # Do computations here
        result = get_new_word(word_count, word_length, words)

        print("Case #{}: {}".format(case_number, result))


def get_new_word(word_count, word_length, words):
    max_words = 1

    letter_sets = [list(map(lambda x: x[i], words)) for i in range(word_length)]

    for i in range(word_length):
        max_words = max_words * len(set(letter_sets[i]))

    if max_words == word_count:
        return "-"

    new_word = collections.Counter(letter_sets[0]).most_common()[-1][0]

    conflicting_words = list(filter(lambda x: x.startswith(new_word), words))

    for i in range(1, word_length):
        old_set = set(letter_sets[i])
        letter_set = set(map(lambda x: x[i], conflicting_words))

        if len(letter_set) == len(old_set):
            new_word = new_word + collections.Counter(letter_sets[i]).most_common()[-1][0]
            conflicting_words = list(filter(lambda x: x.startswith(new_word), conflicting_words))
        else:
            new_word = new_word + old_set.difference(letter_set).pop()
            for j in range(i + 1, word_length):
                new_word = new_word + letter_sets[j][0]
            return new_word


if __name__ == '__main__':
    main()
