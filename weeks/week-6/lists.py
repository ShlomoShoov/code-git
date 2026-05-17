# 1. Sum of a list. Given a list of integers, return the sum of its elements — without using the built-in sum().

def get_sum_of_list(numbers):
    list_sum = 0
    for num in numbers:
        list_sum += num
    return list_sum

# 2. Maximum element. Given a non-empty list of numbers, return the largest element — without using the
# built-in max().

def get_max_element(numbers):
    max_element = numbers[0]

    for number in numbers:
        if number > max_element:
            max_element = number
    return  max_element

# 3. Count occurrences. Given a list and a value, return how many times that value appears in the list.

def count_item(items, target):
    cnt_of_target = 0
    for item in items:
        if item == target:
            cnt_of_target += 1
    return cnt_of_target

# 4. Reverse a list. Given a list, return a new list with the elements in reverse order — without using
# reverse() or slicing with [::-1].


def reverse_list(l):
    reveresd_new_list = []

    for index in range(len(l)-1,-1,-1):
        reveresd_new_list.append(l[index])
    return reveresd_new_list

def reverse_list_2(l):
    reversed_new_list = []
    for index in range(1,len(l)+1):
        reversed_new_list.append(l[-index])
    return reversed_new_list

# 5. Remove duplicates. Given a list, return a new list with duplicates removed, preserving the original order.

def remove_duplicates(l):
    uniq_values_list = []
    used_values = set() # use a set bcz we going do a lot of 'in' and its cheaper in sets (o(1))

    for value in l:
        if value not in used_values:
            uniq_values_list.append(value)
            used_values.add(value)
    
    return uniq_values_list

# 6. Second largest. Given a list of numbers, return the second-largest distinct value.

def second_largest(numbers):
    largest_item = get_max_element(numbers=numbers)
    second_largest_number = None
    for number in numbers:
        if second_largest_number is None and number < largest_item: # we didn't found our second largest yet
            second_largest_number = number
        elif  largest_item > number > second_largest_number: # we have found it but we want to check if we found something bigger
            second_largest_number = number

    return second_largest_number

def second_largest2(numbers):
    largest_item = float('-inf')
    second_largest_item = float('-inf')
    for number in numbers:
        if numbers > largest_item:
            second_largest_item = largest_item
            largest_item = number
            
        elif second_largest_item < number < largest_item:
            second_largest_item = number
    if second_largest_item == float('-inf'):
        return None
    return second_largest_item

# 7. Merge two sorted lists. Given two lists already sorted in ascending order, return a single sorted list
# containing all their elements

def marge_two_sorted_listes(list1,list2):
    list1_index = 0
    list2_index = 0
    new_sorted_list = []
    
    while list1_index < len(list1) and list2_index < len(list2):
        list1_item = list1[list1_index]
        list2_item = list2[list2_index]
        if list1_item < list2_item: # if the list 1 item is smallest it should be before it
            new_sorted_list.append(list1_item)
            list1_index += 1
        else:
            new_sorted_list.append(list2_item)
            list2_index += 1
    
    new_sorted_list+= list1[list1_index:]
    new_sorted_list+= list2[list2_index:]
    return new_sorted_list



# 8. Rotate a list. Given a list and an integer k, return the list rotated to the right by k positions.

def rotate_list(l,k):
    k = k % len(l)

    return l[-k:] + l[:-k]

    



       