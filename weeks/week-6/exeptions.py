# 1. Safe int. Write a function safe_int(s) that returns int(s) if s can be parsed as an integer, and
# returns None otherwise. Do not let any exception escape.

def safe_int(s):
    try:
        return int(s)
    except (ValueError, TypeError):
        return None


# 2. Safe divide. Write a function safe_divide(a, b) that returns a / b, or the string "undefined" if
# b == 0. Use exception handling rather than an if check

def safe_divide(a, b):
    try:
        return a/b
    except (ZeroDivisionError, TypeError):
        return "undefined"

# 3. Dictionary lookup with default. Write a function get_value(d, key) that returns d[key] if the key
# is present, and the string "missing" otherwise — using try / except, not in or .get().


def get_value(d, key):
    try:
        return d[key]

    except KeyError:
        return 'missing'

# 4. Parse list of ints. Write a function parse_ints(values) that takes a list of strings and returns a list of
# integers, skipping any string that cannot be parsed.


def parse_ints(values: list[str]) -> list[int]:
    ints_list = []
    for value in values:
        try:
            intergal = int(value)
        except (ValueError, TypeError):
            pass
        else:
            ints_list.append(intergal)
    return ints_list


# 5. Validate age. Write a function set_age(age) that raises ValueError if age is negative or greater
# than 150, and otherwise returns age


def set_age(age: int):
    if 0 <= age <= 150:
        return age
    else:
        raise ValueError(f'unvalid number : {age}')


# 6. Retry. Write a function retry(func, n) that calls the zero-argument function func() up to n times.
# Return the first successful result. If all n attempts raise an exception, re-raise the last one.

def retry(func, n: int):
    for _ in range(n):
        try:
            res = func()

        except Exception as e:
            error = e
        else:
            return res
    raise error


def convert_list():
    l = ['g', 'h', 'h', 'p']
    for i in range(len(l)):
        l[i] = int(l[i])

# retry(convert_list,9)


# 7. Count errors. Write a function count_errors(funcs) that takes a list of zero-argument functions,
# calls each one, and returns the number of calls that raised any exception.

def count_errors(funcs):
    erorr_cnt = 0
    for func in funcs:
        try:
            func()

        except:
            erorr_cnt += 1

    return erorr_cnt

# 8. Chained exceptions. Write a function load_config(path) that opens the file at path and parses its
# first line as an integer. If anything goes wrong, raise a RuntimeError("failed to load
# config") chained from the original exception using raise ... from ....


def load_config(path):
    try:
        with open(path, 'r') as file:
            line_1 = file.readline()
            value = int(line_1)
            return value
    except Exception as original_error:
        raise RuntimeError('could not load config') from original_error
    

# load_config('f')
