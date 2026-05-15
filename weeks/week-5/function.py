# 1. Write a function is_even(n) that returns True if n is even, False otherwise.


def is_even(n: int | float) -> bool:
    return n % 2 == 0


# 2. Write a function factorial(n) that returns n! using a loop (not recursion).

def factorial(n: int | float) -> int | float:

    factorial_result = n
    while n > 1:
        n = n-1
        factorial_result *= n
    return factorial_result

# 4. Write a function is_palindrome(s) that returns True if the string reads the same forwards and
# backwards.


def is_palindrome(s: str) -> bool:
    left_index = 0
    right_index = len(s)-1

    while left_index < right_index:
        if s[left_index] != s[right_index]:
            return False

        left_index += 1
        right_index -= 1

    return True


# 5. . Write a function digital_root(n) that takes a non-negative integer and
# repeatedly sums its digits until the result is a single digit (0-9).
# Return that digit.

def digital_root(n: int) -> int:
    if n < 10:
        return n
    sum_of_n = 0
    while sum_of_n > 10 or sum_of_n == 0:
        if n == 0:
            n = sum_of_n
            sum_of_n = 0
        while n > 0:

            sum_of_n += n % 10
            n //= 10

    return sum_of_n


# 6. Count digits without str. Given a positive integer, return the number of its digits — without
# converting it to a string.

def count_digits(n: int) -> int:
    cnt_of_digits = 0
    n = abs(n)

    while n > 0:
        cnt_of_digits += 1
        n //= 10
    return cnt_of_digits


# 7. Reverse an integer. Given an integer, return it reversed. If the result has leading zeros, ignore
# them

def reverse_an_integer(n: int):
    is_nagative = n < 0
    n = abs(n)
    reversed_number = 0

    while n > 0:
        reversed_number *= 10
        reversed_number += n % 10
        n //= 10

    if is_nagative:
        reversed_number *= -1

    return reversed_number

# 8. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of
# the non-zero elements.


def moving_zeros_to_end_list_v0(l: list[int]) -> None:

    list_len = len(l)

    for i in range(list_len-1):
        for j in range(i+1, list_len-i):
            if l[i] == 0 and l[j] != 0:
                l[i], l[j] = l[j], l[i]

# o(n) way


def moving_zeros_to_end_list_v1(l: list[int]) -> None:
    zero_place = None  # here we saved the first zero's place we've found.

    for i in range(len(l)):
        if l[i] != 0:
            if zero_place is not None:
                l[i], l[zero_place] = l[zero_place], l[i]
                zero_place += 1
        if l[i] == 0:
            if zero_place is None:
                zero_place = i


#  one more way which dont chack twice (using while loop)

def moving_zeros_to_end_list_v2(l: list[int]) -> None:
    zero_place = None  # here we saved the first zero's place we've found.
    l_len = len(l)
    i = 0

    while i < l_len:
        if l[i] != 0:
            if zero_place is not None:
                l[i], l[zero_place] = l[zero_place], l[i]
                zero_place += 1
                i += 1
        elif l[i] == 0:
            if zero_place is None:
                zero_place = i
        i += 1

l1 = [1, 2, 0, 0, 3]
l2 = [1, 0, 2, 0, 3, 0, 4]
l3 = [1, 0, 0, 0, 3]

print(moving_zeros_to_end_list_v2(l2))
print(l2)


# 9. Given a list of numbers, print the sum, average, minimum, and maximum.

def print_list_detales(l: list[int]) -> None:
    if not l:
        print('list is empty')
        return

    l_sum = 0
    l_cnt = 0
    l_max = l[0]
    l_min = l[0]

    for number in l:
        l_sum += number
        l_cnt += 1
        if number > l_max:
            l_max = number
        if number < l_min:
            l_min = number
    print(f'sum of the list : {l_sum} | avarage value : {l_sum/l_cnt}\n'
          f'max value : {l_max} | minimum value: {l_min}')

# 10. Reverse a list manually using a loop, without using any built-in reverse function.


def revers_list(l: list) -> None:
    left_index = 0
    right_index = len(l)-1

    while left_index < right_index:
        l[left_index], l[right_index] = l[right_index], l[left_index]

        left_index += 1
        right_index += 1


# 11. Given a list with repeating values, return a new list without duplicates while preserving the
# original order.

def remove_dupicates(l: list) -> None:
    exists_values = set()

    i = 0
    l_len = len(l)

    while i < l_len:
        current_value = l[i]
        if current_value in exists_values:
            l.pop(i)
            l_len -= 1
        else:
            exists_values.add(current_value)
            i += 1
