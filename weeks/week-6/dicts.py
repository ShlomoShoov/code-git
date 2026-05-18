# 1. Sum of values. Given a dictionary mapping strings to integers, return the sum of all its values — without
# using the built-in sum().

def sum_dict_values(d:dict):
    sum_of_values = 0
    for value in d.values():
        sum_of_values += value

# 2. Key with maximum value. Given a non-empty dictionary mapping strings to numbers, return the key
# with the largest value.

def get_max_key(d:dict):
    max_value = float('-inf')
    max_key = None
    for key, value in d.items():
        if value > max_value:
            max_key = key
    return max_key

# 3. Count characters. Given a string, return a dictionary mapping each character to the number of times it
# appears.

def count_characters(s):
    cnt_dict = {}
    for char in s:
        cnt_dict[char] = cnt_dict.get(char,0) + 1
    return cnt_dict

# 4. Invert a dictionary. Given a dictionary with unique values, return a new dictionary that swaps keys and
# values

def invert_dict(d:dict):
    inverted_dict = {}
    for key, value in d.items():
        inverted_dict[value] = key
    return inverted_dict

# 5. Merge two dictionaries. Given two dictionaries, return a new dictionary containing all keys from both. If
# a key appears in both, the value from the second dictionary wins.

def marge_tow_dicts(dic1:dict, dic2:dict):
    marged_dict = {}
    uniq_keys = set(dic1.keys()+dic2.keys())
    for key in uniq_keys:
        if key in dic2: # checking dic2 first so if it's in both of them it will add from dic2
            marged_dict[key] = dic2[key]
        else:
            marged_dict[key] = dic1[key]
    return marged_dict

# 6. Filter by value. Given a dictionary mapping strings to numbers and a threshold, return a new dictionary
# containing only the items whose value is greater than the threshold.

def filter_by_value(d,threshold):
    filterd_dict = {}
    for key,value in d.items():
        if value >= threshold:
            filterd_dict[key] = value
    return filterd_dict

def filterd_by_value2(d, threshold):
    return {key:value for key, value in d.items() if key >= threshold}

# 7. Group by first letter. Given a list of words, return a dictionary mapping each first letter to a list of all
# words starting with that letter.

def group_by_first_letter(items):
    filterd_dict = {}

    for item in items:
        first_letter = item[0]
        if first_letter not in filterd_dict:
            filterd_dict[first_letter] = []
            
        filterd_dict[first_letter].append(item)
            
    return filterd_dict

print(group_by_first_letter(["apple", "ant", "banana", "berry", "cherry"]))


# 8. Word frequency. Given a string of words separated by spaces, return a dictionary mapping each word to
# how many times it appears.

def get_words_frequency(text:str):
    words_frequency_dict = {}
    words = text.split()
    for word in words:
        words_frequency_dict[word] = words_frequency_dict.get(word,0) + 1
    return words_frequency_dict

#  9. Common keys. Given two dictionaries, return a list of keys that appear in both — sorted in ascending
# order.

 
def get_common_keys(dic1, dic2):
    dic1_keys = set(dic1.keys())
    dic2_keys = set(dic2.keys())
    common_keys = dic1_keys & dic2_keys
    return common_keys

print(get_common_keys({"a": 1, "b": 2, "c": 3}, {"b": 9, "c": 8, "d": 7} ))

# 10. Most frequent value. Given a dictionary, return the value that appears most often across all keys. If there
# is a tie, return any one of the tied values.

def get_most_frequnts_value(d:dict):
    values_cnt = {}
    for value in d.values():
        values_cnt[value] = values_cnt.get(value,0) +1

    max_cnt_value = 0
    cnt_dict = {}
    for key, value in values_cnt.items():
        if value > max_cnt_value:
            max_cnt_value = value
        if value not in cnt_dict:
            cnt_dict[value] = []
        cnt_dict[value].append(key)

    return cnt_dict[max_cnt_value]

print(get_most_frequnts_value( {"a": 1, "b": 2, "c": 2, "d": 3, "e": 1} ))