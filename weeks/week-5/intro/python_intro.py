# 1. Print True if the input integer is even, without using if statements.

input_number = int(input('enter a number -> '))
print(bool(input_number % 2 == 0))


# 2. Swap two integers using only addition and subtraction, without a third variable.

a = 7
b = 13

a = a + b
b = a - b
a = a - b


print(f'a: {a}, b:{b}')


# 3. Find the sum of digits of a 3-digit integer using only division and modulo.

tree_digit_number = 123
# with +

print(123 % 10+(123//10) % 10+(123//100) % 10)


# 4. Calculate BMI from weight and height using weight / height², rounded to 2 decimal places

weight_in_kg = 60
hight_in_meter = 1.70

bmi = weight_in_kg/(hight_in_meter**2)
print(bmi)
bmi = bmi * 100
bmi = int(bmi)
print(bmi/100)


# 5. Take a decimal number and print its integer and fractional parts using type casting only.


decimal_number = float(input('enter a decimal number -> '))
intergal = int(decimal_number)
float_num = decimal_number - intergal
print(f'intergal: {intergal} | float : {float_num}')
