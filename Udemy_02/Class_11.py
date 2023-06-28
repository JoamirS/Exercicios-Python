"""
Create a function that finds the first duplicate considering the second number like a duplication.
Return the considered duplication.
Requirements:
    The order of duplicate number is considered from the second occurrence of the number, i.e., the duplicate number itself.
    Sample:
    [1, 2, 3, 3, 2, 1] -> 1, 2 e 3 are duplicated (return 3)
    [1, 2, 3, 4, 5, 6] -> Return -1 (Aren't duplicates)
    If not find duplication in list, return -1
"""

list_of_of_integers = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def find_first_duplicate(list_integers):
    check_numbers = set()
    first_duplicate = -1

    for number in list_integers:
        if number in check_numbers:
            first_duplicate = number
            break

        check_numbers.add(number)

    return first_duplicate


for list_iterable in list_of_of_integers:
    print(find_first_duplicate(list_iterable))
