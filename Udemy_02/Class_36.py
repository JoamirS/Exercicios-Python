"""
Consider two lists of integers and floats (list A and list B)
Sum the values on the list returning a new list with added values:
If a list is longer that the other, the sum will consider the length of the smallest list

Sample:
list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [1, 2, 3, 4]

============ Result

list_sum = [2, 4, 6, 8]
"""


def sum_two_list(list_1, list_2, length):
    list_result_sum_two_list = list()
    counter_position_increase = 0
    while counter_position_increase < length:
        list_result_sum_two_list.append(list_1[counter_position_increase] + list_2[counter_position_increase])
        counter_position_increase += 1

    return list_result_sum_two_list


def check_small_list(list_1, list_2):
    length_list_1 = len(list_1)
    length_list_2 = len(list_2)

    if length_list_1 < length_list_2:
        length_small_list = length_list_1
        small_list = list_1
    else:
        length_small_list = length_list_2
        small_list = list_2

    return length_small_list, small_list


list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [1, 2, 3, 6]

length_small_list_result = check_small_list(list_a, list_b)
result_sum_list = sum_two_list(list_a, list_b, length=length_small_list_result[0])
print(result_sum_list)
