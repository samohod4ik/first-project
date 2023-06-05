from itertools import groupby, dropwhile


def ranges(numbers):
    key = lambda x: x[1] - x[0]
    result = []
    for group in groupby(enumerate(numbers), key=key):
        segment = tuple(elem[1] for elem in group[1])
        result.append((segment[0], segment[-1]))
    return result


def group_anagrams(words):
    key = lambda x: sum(ord(i) for i in x)
    for group in groupby(sorted(words, key=key), key=key):
        yield tuple(group[1])


def first_largest(iterable, number):
    for i, n in dropwhile(lambda x: x[1] <= number, enumerate(iterable)):
        return i
    return -1


if __name__ == '__main__':
    pass

