# Name = 'jhon smith'
# age = 20
# is_new = True
# print (Name, age  )
# import math

# name = input('what is your name? ')
# favorite_color = input ('what is your favroute colour? ')
# question = input ( " which colour you don't like's colour  ")
# print (name + ' likes ' + favorite_color + ' colour ' + question + 'you should like some colour ' )

# about_me = '''hi sagar
# i am good , what about you good to know you good
# hope we meet soon. '''
# print (about_me)

# weight_in_pound = input('weight in pound: ')
# weight_in_kg= 0.453*float(weight_in_pound )
# print(weight_in_kg )

# about = 'sagar is good boy'
# boy = about [1:50]
# print(about [-1])
# print(about[2:5])
# print(about[0:9])
# print(about[:9])
# print(boy)
# print(about[1:-1])



# last_name='kumar'
# first_name='sagar'
# massage = first_name+'['+ last_name +' '+ '] is satarted codeing '
# msg = f'{first_name}[{last_name }] is started codeing '
# print(msg)
# print(massage)

# About = 'I am not Rich Guy'
# print (len(About))
# print (About.upper())
# print(About.lower())
# print(About.title())
# print(About.find('R'))
# print (About.replace('Rich', 'Average '))
# print ('rich' in About)

# x = 22/7
# print(x)
# print(round(x))
# print(abs(x)) #absloute return always positive number
# import math
# print(math.ceil(3.09))
# The result of the integer division 0.
# The result of the float division is 0.6
# a = 3
# b = 5
# print(a//b)
# print(a/b)

# age = int(input('what is your age? '))
# if age > 18:
#     print('you are ok for voting')
# else:
#     print('you are not allow to vote')

# Driving Eligibility:
# Write a program that asks the user for their age and prints whether they are eligible to get a driver's license.
# Assume the minimum age to get a driver's license is 18.

# age_for_driving_licence = int(input('let me know are you eligibility of driving put age here ? '))
# if age_for_driving_licence > 21:
#     print('you are not')
# else:
#     print('go to hell')

# Grade Classification:
# Write a program that takes a student's score as input and prints their grade based on the following criteria:
#
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F

# Prompt the user to enter their score
# score = float(input("Enter your score: "))
#
# # Determine the grade based on the score
# if 90 <= score <= 100:
#     grade = 'A'
# elif 80 <= score < 90:
#     grade = 'B'
# elif 70 <= score < 80:
#     grade = 'C'
# elif 60 <= score < 70:
#     grade = 'D'
# else:
#     grade = 'F'
#
# Print the grade
# print(f"Your grade is: {grade}")

# Leap Year Checker:
# Write a program that asks the user for a year and prints whether the year is a leap year or not.
# A year is a leap year if it is divisible by 4 but not divisible by 100 unless it is also divisible by 400.

# leap_year = int(input('tell me the year'))
# if leap_year%400==0 :
#     print('this is a leap year')
# else :
#     print('this is not leap year')

# year = int(input("Enter a year: "))
#
#Check if the year is a leap year
# if (year % 4 == 0 and year % 100 != 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")
# Number Range:
# Write a program that asks the user for a number and prints whether the number is positive, negative, or zero.
# number_range =int(input('number range: '))
# if number_range>0:
#     print('positive number')
# elif number_range < 0:
#     print(' negative number')
# else:
#     print('zero number')

# Even or Odd:
# Write a program that asks the user for a number and prints whether the number is even or odd.

# number = int(input('even or odd number: '))
# if number%2 == 0:
#     print('odd number')
# else :
#     print('even number')

# Temperature Converter:
# Write a program that asks the user to enter a temperature in Celsius and converts it to Fahrenheit.
# Then, print whether the temperature is above or below freezing (0°C).


# Prompt the user to enter a temperature in Celsius
# celsius = float(input("Enter temperature in Celsius: "))
#
# # Convert to Fahrenheit
# fahrenheit = (celsius * 9/5) + 32
#
# # Determine if it's above or below freezing
# if celsius > 0:
#     print(f"The temperature is {fahrenheit}°F and it's above freezing.")
# else:
#     print(f"The temperature is {fahrenheit}°F and it's at or below freezing.")

# Number Comparison:
# Write a program that asks the user for two numbers and prints which number is larger, or if they are equal.
# num1 = float(input('enter a first numbers'))
# take a 1st input
# num2 = float(input('enter a second numbers'))
# take second input
# cheack the number comprasion
# if num1 > num2:
#     print('the first number in larg')
# elif num1< num2:
#     print('the second number is larg')
# else:
#     print('they are equal')

# Vowel or Consonant:
# Write a program that asks the user to enter a single letter and prints whether it is a vowel or a consonant.
# (Assume the input is a letter).

# letter = input('enter a single letter: ')
# if letter in 'aieou':
#     print(f'this is vowel letter')
# else:
#     print(f'this is consonant letter')

# Triangle Type:
# Write a program that takes the lengths of three sides of a triangle as input and determines whether the triangle is
# equilateral (all sides equal), isosceles (two sides equal), or scalene (no sides equal).
# length1 = int(input('one side of trangle: '))
# length2 = int(input('second side of trangle: '))
# length3 = int(input('third side of trangle: '))
# if length1==length2==length3:
#     print('this is equilateral trangle')
# elif length1==length2 or length2== length3 or length3==length1 :
#     print('this is isosceles trangle')
# else :
#     print('this is scalene trangle ')

# Shopping Discount:
# Write a program that asks the user for the total amount of a purchase and applies a discount based on the following criteria:
#
# If the amount is greater than $100, apply a 10% discount.
# If the amount is between $50 and $100 (inclusive), apply a 5% discount.
# If the amount is less than $50, no discount is applied.
# Print the final amount after discount.


    # Prompt the user to enter the total purchase amount
# amount = float(input("Enter the total purchase amount: "))
#
#     # Apply discount based on the amount
# if amount > 100:
#     discount = amount * 0.10
# elif 50 <= amount <= 100:
#     discount = amount * 0.05
# else:
#      discount = 0
#
#     # Calculate the final amount after discount
# final_amount = amount - discount
#
#     # Print the final amount
# print(f"The final amount after discount is ¥{final_amount:2f}.")

# Library Fine Calculation:
# Write a program that asks the user for the number of days a library book is overdue and calculates the fine based on the following criteria:
#
# First 5 days: $0.50 per day
# Next 5 days: $1.00 per day
# Beyond 10 days: $2.00 per day

# book_overdues = int(input('enter a book overdue days: '))
# if book_overdues <= 5:
#     fine= book_overdues*0.5
# elif book_overdues <=10 :
#     fine= (5 * 0.5)+ (book_overdues-5)*1.00
# else :
#     fine = (5*0.5) + (5*1.0)+(book_overdues-10)*2.00
# print(f'your book overdue  {fine}¥')

