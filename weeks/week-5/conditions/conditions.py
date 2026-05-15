# 1. Get an age as input. Print "Invalid" if the age is below 0 or above 120, "Child" if the age is
# between 0 and 12, "Teen" if the age is between 13 and 17, and "Adult" for any other age.

age = int(input('enter your age: '))

if age < 0 or age > 120:
    print ("Invalid")
elif 0 <= age <= 12:
    print('child')
elif 13 <= age <= 17:
    print('teen')
else:
    print('adult')

#2. Get a single character as input. If the character is not an English letter print "Invalid". If the
# character is a vowel (a, e, i, o, u) print "Vowel", otherwise print "Consonant".
 
char = input('enter singel char: ').lower()
if  not (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):
    print('Invalid')
elif char in ['a','e','i', 'o', 'u']:
    print('Vowel')
else:
    print('Consonant')

#3. Get an age and a VIP card (yes/no). Automatically reject anyone under 16. Allow entry only if
# the customer is over 18 and has a VIP card, or if their age is 19, 20, or 21.

age = int(input('enter your age'))
has_vip = input('has a vip card? y/n')

has_vip = has_vip == 'y'

if age < 16:
    print('go away you kiddy')

elif age > 18 and (has_vip or 19 <= age <= 21):
    print('you can enter')

else:
    print('Rejected')








#4. Get a password from the user and compare it to a password saved in the code. If they match
# print "Access Granted". If they don't match and the password is shorter than 8 characters print
# "Too short", otherwise print "Wrong password".


real_password = '12345'

input_password = input('enter your password:')

if input_password == real_password:
    print('Access Granted')
elif len(input_password) < 8:
    print('too short')
else:
    print('wrong password')


#5. Get coordinates x and y as input. The rectangle is defined between x=10 and x=50 and
# between y=20 and y=80. Print "Inside the rectangle" if the point is inside, "On the edge" if it is
# exactly on one of the borders, and "Outside the rectangle" if it is outside.

x = float(input('enter x point'))
y = float(input('enter y point'))


if 10 < x < 50 and 20 < y < 80:
    print("Inside the rectangle")
elif ((x == 10 or x == 50) and (20<y<80))  or ((y==20 or y== 80) and (10<x<50)) :
    print("On the edge")
else:
    print('outside!!')


# 6. Greeting with Default Get a name from the user. If the user pressed Enter without typing
# anything, greet them as "Anonymous", otherwise greet them with their name. using or operator
# instead of if/else


intro = input('enter your name or enter to continue')

print (f"welcomo,{intro or 'Anonymous'}")

# 8. Get three numbers from the user. Print how many of them are positive (greater than 0). You
# must not use any if statement. Use the fact that True + True == 2 to add the comparison results
# directly

first_number = int(input('enter first nu    mber'))
second_number = int(input('enter second number'))
third_number = int(input('enter third number'))

print(f'you gave me {(first_number>0) + (second_number>0) + (third_number>0)} positive numbers')

# 10. Get a score from 0 to 100 from the user. Print "A" for 90-100, "B" for 80-89, "C" for 70-79,
# and "F" for anything below 70. Use only a single nested ternary expression — no if/elif/else
# allowed.

score = int(input('enter your score-> '))

# one way:
print('A' if score >= 90 else 'B' if score >= 80 else 'C' if score>= 70 else 'F')

# second way 

