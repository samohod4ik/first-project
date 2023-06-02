from secondary import group_anagrams, ranges, first_largest

numbers = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 20, 25, 56, 57]

anagrams = ['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko']

if __name__ == '__main__':
    groups = group_anagrams(anagrams)
    print(*groups)
    print(ranges(numbers))

    iterator = iter([18, 21, 14, 72, 73, 18, 20])
    print(first_largest(iterator, 10))
