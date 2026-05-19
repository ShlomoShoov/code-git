# 1. Counter with global. Write a function bump() that increments a module-level variable count by 1,
# and a function value() that returns its current value. After three calls to bump(), value() should
# return 3

counter = 0

def bump():
    global counter
    counter += 1

def value():
    return(counter)



# 2. Counter with closure. Write a function make_counter() that returns a function. Each call to the
# returned function should return the next integer starting from 1.

def make_counter():
    counter = 0
    def step():
        nonlocal counter
        counter += 1
        return counter
    return step

# 3. LEGB walk-through. Predict the output of this code, then run it to verify.


x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()
    print(x)
outer()
print(x)

# will print:
# 'local'
# 'enclosing'
# 'global'

# 4. Shadowing trap. Explain why the following code raises a TypeError, and rewrite it to work correctly.
# list = [1, 2, 3]
# print(list(range(5)))
# it will rewrite the build -in functions to be a 'list' object so we wont be able to use the list build function (or class)

# to correct it I'll use onoter name

my_list = [1, 2, 3]
print(list(range(5)))

# works!

