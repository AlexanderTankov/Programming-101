def is_list_palindrome(list):
    flag = list
    return flag[::-1] == list


def number_to_binary(n):
    binary_number = []
    while n != 0:
        binary_number.append(n % 2)
        n //= 2
    binary_number.reverse
    return binary_number


def hack_number(n):
    temp_list = number_to_binary(n)
    sum_of_numbers = 0
    for x in temp_list:
        if x % 2 != 0:
            sum_of_numbers += 1
    return is_list_palindrome(temp_list) and sum_of_numbers % 2 != 0


def next_hack(n):
    flag = False
    new_number = n + 1
    if n == 0:
        return 1
    while not flag:
        if hack_number(new_number):
            return new_number
            flag = True
        else:
            new_number += 1
    return -1
