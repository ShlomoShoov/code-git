# 1. Remove duplicates. Given a list, return a new list with duplicates removed — order does not need to be
# preserved.

def remove_duplicates(l):
    return list(set(l))

# 2. Count unique elements. Given a list, return the number of distinct elements in it — without using
# len(set(...)) directly as the whole solution (build the count yourself).

def count_unique_elements(l):
    seen = set()
    count = 0
    for item in l:
        if item not in seen:
            seen.add(item)
            count += 1
    return count

# 3. Common elements. Given two lists, return a sorted list of values that appear in both.

def get_common_elements(l1,l2):
    return sorted(set(l1) & set(l2))

# 4. Elements in only one. Given two lists, return a sorted list of values that appear in exactly one of them.

def element_only_in_one(l1, l2):
    return sorted(set(l1) ^ set(l2))

# 5. Is subset. Given two lists a and b, return True if every element of a also appears in b.

def is_subnet(a,b):
    return set(a) <=  set(b)

# 6. Unique characters. Given a string, return True if all of its characters are distinct, and False otherwise.

def is_unique_chracters(s):
    return len(s) == len(set(s))

# 7. First repeated element. Given a list, return the first value that appears more than once as you scan from
# left to right. If no value repeats, return None.


def get_first_repeated_element(l):
    unique_values = set()
    for element in l:
        if element in unique_values:
            return element
        unique_values.add(element)
    return None


# 8. Distinct words. Given a string of words separated by spaces, return the number of distinct words (caseinsensitive).

def cnt_distinct_words(text:str):
    unique_words = set(text.lower().split())
    return  len(unique_words)

# 9. Pair sum exists. Given a list of integers and a target, return True if there exist two distinct elements in
# the list whose sum equals the target. Aim for an O(n) solution using a set.

def pair_sum_exists(l,target):
    needed_num = set()
    for num in l:
        if num in needed_num:
            return True
        needed_num.add(target-num)
    return False

 
 
# 10. Symmetric difference without operators. Given two lists, return a sorted list of values that appear in
# exactly one of them — without using the ^ operator or symmetric_difference().

def symmtric_difference(l1, l2):
    s1 = set(l1)
    s2  = set(l2)
    unique_in_s1 = s1 - s2
    unique_in_s2 = s2 - s1
    unique_in_s1.update(unique_in_s2)


    return sorted(unique_in_s1)


print(symmtric_difference([1, 2, 3, 4], [3, 4, 5, 6] ))