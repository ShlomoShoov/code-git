# . Sum of a tuple. Given a tuple of integers, return the sum of its elements — without using the built-in
# sum().

def sum_tuple(numbers:tuple[int]):
    sum_of_tuple = 0
    for num in numbers:
        sum_of_tuple += num
    return sum_of_tuple

# 2. Maximum element. Given a non-empty tuple of numbers, return the largest element — without using
# the built-in max().

def get_max_element(numbers):
    max_element =  float('-inf')
    for num in numbers: 
        if num > max_element:
            max_element = num
    return max_element


#3. Count occurrences. Given a tuple and a value, return how many times that value appears — without
# using the count() method.

def count_object(numbers, target):
    cnt_of_object = 0
    for number in numbers:
        if number == target:
            cnt_of_object += 1
    return cnt_of_object

#4. Reverse a tuple. Given a tuple, return a new tuple with the elements in reverse order — without using
#slicing with [::-1].

def reverse_tuple(items):
    reversed_tuple = ()
    for index in range(len(items)-1,-1,-1):
        reversed_tuple += items[index],
    
    return reversed_tuple

# 5. Swap pairs. Given a tuple with an even number of items, return a new tuple where each adjacent pair is
# swapped.

def swap_pairs(items):
    swaped_tuple = ()
    for index in range(0,len(items),2):
        swaped_tuple += items[index+1], items[index]
    return swaped_tuple

# 6. Min and max. Given a non-empty tuple of numbers, return a tuple (min, max) — without using the
# built-in min() or max()

def min_max(numbers):
    max_number = float('-inf')
    min_number = float('inf')

    for num in numbers:
        if num > max_number:
            max_number = num
        if num < min_number:
            min_number = num
    return min_number , max_number

# 7. Distance between points. Given two tuples representing points (x1, y1) and (x2, y2), return the
# Euclidean distance between them.

def get_distance(point_a, point_b):
    x1, y1 = point_a
    x2, y2 = point_b
    dis = ((x2-x1)**2+(y2-y1)**2)**0.5
    return dis

 # 8. Merge and sort. Given two tuples of numbers, return a single sorted tuple containing all their elements.

def marge_two_sorted_tuples(tuple1, tuple2):
    marged_tuple = ()
    tuple1_index = 0
    tuple2_index = 0
    while tuple1_index<len(tuple1) or tuple2_index<len(tuple2):
        tuple_1_item = tuple1[tuple1_index]
        tuple_2_item = tuple2[tuple2_index]
        if tuple_1_item < tuple_2_item:
            marged_tuple += tuple_1_item,
            tuple1_index += 1
        else:
            marged_tuple += tuple_2_item,
            tuple2_index += 1
    marged_tuple += tuple1[tuple1_index:]
    marged_tuple += tuple2[tuple2_index:]

    return marged_tuple

# 9. Frequency table. Given a tuple of items, return a tuple of (item, count) pairs — one for each
# distinct item, in the order of first appearance

def get_frequency_table(items):
    frequency_table = ()
    uniq_items = set()
    for item in items:
        if item not in uniq_items:
            cnt_of_item = count_object(items,target=item)
            frequency_table += (item,cnt_of_item),
        uniq_items.add(item)

    return frequency_table

# 10. Rotate a tuple. Given a tuple and an integer k, return the tuple rotated to the right by k positions.

def move_k_right(items, k):
    k = k % len(items)

    return items[-k:] + items[:-k]


