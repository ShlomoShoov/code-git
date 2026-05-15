# 1. Loop over numbers 1–10. Skip even numbers (continue), and stop completely
# when you reach 7. What gets printed?

for i in range(1,11):
    if i % 2 == 0:
        continue
    elif i == 7:
        break
    print(i)

#prints 1,3,5

# 2. Write a loop that asks the user for a password (input()).
# If the password is "1234" — print "Welcome!" and exit.
# Otherwise, print "Try again".
# (Why is while True the right tool here?)


correct_password = False
PASSWAORD = '1234'

while not correct_password:
    user_pass = input('enter your password->> ')
    if user_pass ==  PASSWAORD:
        print('welcome')
        correct_password = True
    
    else:
        print('try again')

# answer: while true (or while flag - true) need bcz we dont know when the user enter the correct password

# 3. Take product names from the user one by one, and stop when the user types "done".
# Print the full list at the end. (Why is while the only loop option here?)

is_done = False
product_list = []
while not is_done:
    user_input = input('enter your prodocot name or done-> ')
    if user_input == 'done':
        is_done = True
    else:
        product_list.append(user_input)

for product in product_list:
    print(product)

# ans = we dont know when the uset will be done


# 3.1 Write a double loop: rows 1–3, columns 1–3. Print each pair (row, col),
# but if col == 2 stop the inner loop. What gets printed? Does the outer loop keep
# going?

for row in range(1,4):
    for col in range (1,4):
        if col == 2:
            break
        print(f'row: {row} | col: {col}')



# 4. Get a string from the user. Use a for loop to count how many vowels (a, e, i, o, u,
# both lowercase and uppercase) appear in it. Print the count.# 

user_string = input('enter your string: ').lower()
cnt = 0
for char in user_string:
    if char in ['a','e','i','o','u']:
        cnt += 1

print(f'in total -> {cnt} vowels letters in your string ')

# 5. Multiplication Table — Use a nested for loop to print the multiplication table from 1x1
# to 5x5. Format each line as "3 x 4 = 12".

for i in range (1,6):
    for j in range(1,6):
        print (f'{i} * {j} = {i*j}')


# 6. Get a string from the user and print it reversed using a for loop and an accumulator
# variable. You may not use slicing like s[::-1] or the built-in reversed() function.



user_string = input('enter your string ')

reversed_string = ''
for i in range (len(user_string)-1, -1, -1):
    reversed_string += user_string[i]

print(f'your reversed string is {reversed_string}')


# 7. Given a positive integer, use a while loop and arithmetic operators (%, //) to count
# how many of its digits are even.

user_number = int(input('enter a positive number'))

cnt_even = 0

while user_number > 0:
    cnt_even += (user_number % 10) % 2 == 0
    user_number //= 10

print(f'in your number you have {cnt_even} even numbers')


# 8. Given a string, use a for loop to construct and print a new string where every
# character from the original is repeated twice (e.g., "abc" becomes "aabbcc").

user_string = input('enter a string-> ')

repeted_string = ''

for char in user_string:
    repeted_string += char + char

print(f' your repeted string -> {repeted_string}')

# 9. Continuously ask the user for positive integers until they enter 0. Once the loop
# stops, print the highest number entered during the process.

is_zero = False
higher_number = None


while not is_zero:
    user_number = int(input('enter your number'))
    if user_number == 0:
        is_zero = True
    elif higher_number is None or user_number > higher_number :
        higher_number = user_number

if higher_number:
    print(f'your higher number is: {higher_number}')

    
# 10. Iterate through a string and check if it contains only letters and numbers. Print False
# if any special characters or spaces are found, otherwise print True.

string = 'hello2theworld!'

only_letters_and_numbers = True
for letter in string:
    if not('a' <= letter <= 'z' or 'A' <= letter <= 'Z' or '0' <= letter <= '9'):
        only_letters_and_numbers = False

print(f'is there only letters and numbeets -> {only_letters_and_numbers}')


# 11. Given an integer, use a loop and mathematical operations to reverse its digits (e.g.,
# 123 becomes 321). Constraint: Do not convert the number to a string.

given_number = int(input('enter an interger -> '))
is_negative = given_number < 0
given_number = abs(given_number)
reversed_number = 0

while given_number != 0:
    reversed_number *= 10
    reversed_number += given_number%10
    given_number = given_number/10
if is_negative:
    given_number *= -1

    
print(f'your reversed numbers is {reversed_number}')