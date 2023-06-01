from secondary import group_anagrams, ranges

numbers = [1, 2, 3, 4, 5, 6, 7]

anagrams = ['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko']

if __name__ == '__main__':
    groups = group_anagrams(anagrams)
    print(*groups)
    print(ranges(numbers))
