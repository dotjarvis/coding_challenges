# SUNDAY, 27  NOV 2022

# # QUESTION 1
# # Write a function that stutters a word as if someone is struggling to read it.
# # The first two letters are repeated twice with an ellipsis ... and space after each,
# # and then the word is pronounced with a question mark ?.
# # stutter("incredible") ➞ "in... in... incredible?"
# # stutter("enthusiastic") ➞ "en... en... enthusiastic?"
# # stutter("outstanding") ➞ "ou... ou... outstanding?"
#
# # Solution
# def stutter(word):
#     return f'{word[:2]}... {word[:2]}... {word}?'
#
#
# print(stutter('jarvis'))

#
# # QUESTION 2
# # Create a function that takes two numbers and a mathematical operator + - / *
# # and will perform a calculation with the given numbers.
# # calculator(2, "+", 2) ➞ 4
# # calculator(2, "*", 2) ➞ 4
# # calculator(4, "/", 2) ➞ 2
#
# # SOLUTION
# def calculator(num1, operator, num2):
#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '*':
#         return num1 * num2
#     elif operator == '/':
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Can't divide by 0!"
#
#
# print(calculator(23, '/', 0))
#
#
# # QUESTION 3
# # # Create a function that takes an integer and returns the factorial of that integer.
# # # That is, the integer multiplied by all positive lower integers.
# # # factorial(3) ➞ 1 * 2 * 3  6
# # # factorial(5) ➞ 1 * 2 * 3 * 4 * 5 120
# # # factorial(13) ➞ 6227020800
# #
# # SOLUTION
# def factorial(num):
#     output = 1
#     for number in range(num + 1):
#         if number > 0:
#             output *= number
#     return output
#
#
# print(factorial(3))
# print(factorial(5))
# print(factorial(13))
#
# # QUESTION 4
# # Given the radius of a circle and the area of a square,
# # return True if the circumference of the circle is greater than the square's perimeter
# # and False if the square's perimeter is greater than the circumference of the circle.
# # circle_or_square(16, 625) ➞ True
# # circle_or_square(5, 100) ➞ False
# # circle_or_square(8, 144) ➞ True
#
# # SOLUTION
# import math
#
#
# def circle_or_square(rad, area):
#     pi = 3.14
#     circumference = 2 * pi * rad
#     square_side = math.sqrt(area)
#     perimeter = square_side * 4
#     if circumference > perimeter:
#         return True
#     else:
#         return False
#
#
# print(circle_or_square(16, 625))
# print(circle_or_square(5, 100))
# print(circle_or_square(8, 144))
#
#
# # QUESTION 5
# # Create a function that takes damage and speed (attacks per second) and
# # returns the amount of damage after a given time.
# # damage(40, 5, "second") ➞ 200
# # damage(100, 1, "minute") ➞ 6000
# # damage(2, 100, "hour") ➞ 720000
#
# # SOLUTION
#
# def damage(damages, speed, time):
#     if damages < 0 or speed < 0:
#         return 'invalid'
#     if time == 'second':
#         time_in_sec = speed
#     elif time == 'minute':
#         time_in_sec = speed * 60
#     elif time == 'hour':
#         time_in_sec = speed * 60 * 60
#     return time_in_sec * damages
#
#
# print(damage(40, 5, "second"))
# print(damage(100, 1, "minute"))
# print(damage(2, 100, "hour"))
# print(damage(2, -100, "hour"))


# MONDAY 28, NOV 2022

# # QUESTION 1
# # Create a function that takes a number num and returns its length.
# # use of the len() function is prohibited.
# # number_length(10) ➞ 2
# # number_length(5000) ➞ 4
# # number_length(0) ➞ 1
#
# # SOLUTION
# def receive(num):
#     output = 0
#     for digit in str(num):
#         output += 1
#
#     return output
#
#
# print(receive(30))
# print(receive(0))
# print(receive(312345600))


# QUESTION 2
# Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
# format_date("11/12/2019") ➞ "20191211"
# format_date("12/31/2019") ➞ "20193112"
# format_date("01/15/2019") ➞ "20191501"

# SOLUTION
# def format_date(date):
#     split_date = date.split('/')
#     date, month, year = split_date
#     return year + month + date
#
#
# print(format_date("11/12/2019"))
# print(format_date("12/31/2019"))
# print(format_date("01/15/2019"))


# QUESTION 3
# Write a function that takes a list of numbers and returns a list with two elements:
# The first element should be the sum of all even numbers in the list.
# The second element should be the sum of all odd numbers in the list.
# sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])
# sum_odd_and_even([0, 0]) ➞ [0, 0])

# SOLUTION
# def sum_odd_and_even(list):
#     even = 0
#     odd = 0
#     for number in list:
#         if number % 2 == 0:
#             even += number
#         else:
#             odd += number
#
#     return f'[{even},{odd}]'
#
#
# print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))
# print(sum_odd_and_even([-1, -2, -3, -4, -5, -6]))
# print(sum_odd_and_even([0, 0]))


# QUESTION 4
# Python got drunk and the built-in function's str() and int() are acting odd:
# str(4) ➞ 4
# str("4") ➞ 4
# int("4") ➞ "4"
# int(4) ➞ "4"
# You need to create two functions to substitute str() and int().
# A function called int_to_str() that converts integers into strings and
# a function called str_to_int() that converts strings into integers.
# int_to_str(4) ➞ "4"
# str_to_int("4") ➞ 4
# int_to_str(29348) ➞ "29348"

# SOLUTION
# class GotDrunk:
#     def int_to_str(num):
#         return str(num)
#
#     def str_to_int(num):
#         return int(num)
#
#
# got_drunk = GotDrunk
#
# print(got_drunk.str_to_int('4'))
# print(got_drunk.int_to_str(8))

# QUESTION 5
# Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".
# If the number is a multiple of 3 the output should be "Fizz".
# If the number given is a multiple of 5, the output should be "Buzz".
# If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
# If the number is not a multiple of either 3 or 5,
# the number should be output on its own as shown in the examples below.
# The output should always be a string even if it is not a multiple of 3 or 5.
# fizz_buzz(3) ➞ "Fizz"
# fizz_buzz(5) ➞ "Buzz"
# fizz_buzz(15) ➞ "FizzBuzz"
# fizz_buzz(4) ➞ "4"

# # SOLUTION
# def fizz_buzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return 'FizzBuzz'
#     if num % 3 == 0:
#         return 'Fizz'
#     elif num % 5 == 0:
#         return 'Buzz'
#     else:
#         return f'{num}'
#
#
# print(fizz_buzz(3))
# print(fizz_buzz(5))
# print(fizz_buzz(15))
# print(fizz_buzz(4))

# QUESTION 6
# Create a function that finds the highest integer in the list using recursion.
# find_highest([-1, 3, 5, 6, 99, 12, 2]) ➞ 99
# find_highest([0, 12, 4, 87]) ➞ 87
# find_highest([8]) ➞ 8

# # SOLUTION
# def find_highest(list):
#     if len(list) == 1:
#         return list[0]
#     if list[0] > list[1]:
#         return list[0]
#     elif list[0] < list[1]:
#         return find_highest(list[1:])
#
#
# print(find_highest([-1, 3, 5, 6, 99, 12, 2]))
# print(find_highest([0, 12, 4, 87]))
# print(find_highest([8]))

# TUESDAY 29 NOV 2022

# QUESTION 1
# Write a function that takes coordinates of two points on a two-dimensional plane
# and returns the length of the line segment connecting those two points.
# line_length([15, 7], [22, 11]) ➞ 8.06
# line_length([0, 0], [0, 0]) ➞ 0
# line_length([0, 0], [1, 1]) ➞ 1.41

# # SOLUTION
# import math
#
#
# def line_length(point1, point2):
#     length = abs(point1[0] - point2[0])
#     width = abs(point1[1] - point2[1])
#
#     return math.sqrt(length ** 2 + width ** 2)
#
#
# print(line_length([15, 7], [22, 11]))
# print(line_length([0, 0], [0, 0]))
# print(line_length([0, 0], [1, 1]))


# QUESTION 2
# Create a function that takes two number strings and returns their sum as a string.
# add("111", "111") ➞ "222"
# add("10", "80") ➞ "90"
# add("", "20") ➞ "Invalid Operation"
# If any input is "" or None, return "Invalid Operation".

# # SOLUTION
#
# def add(first_number, second_number):
#     if not bool(first_number) or not bool(second_number):
#         return 'Invalid Operation'
#     else:
#         output = int(first_number) + int(second_number)
#         return str(output)
#
#
# print(add("111", "111"))
# print(add("10", "80"))
# print(add("", "20"))
# print(add("", ""))


# QUESTION 3
# Create a function that takes the number of daily average recovered cases recovers,
# daily average new_cases, current active_cases, and returns the number of days
# it will take to reach zero cases.
# end_corona(4000, 2000, 77000) ➞ 21
# end_corona(3000, 2000, 50699) ➞ 19
# end_corona(30000, 25000, 390205) ➞ 15

# # SOLUTION
#
# def end_corona(recovers, new_cases, current_cases):
#     total_cases = new_cases + current_cases
#     days = 0
#     while total_cases > 0:
#         days += 1
#         total_cases -= recovers
#     return days+1
#
#
# print(end_corona(4000, 2000, 77000))
# print(end_corona(3000, 2000, 50699))
# print(end_corona(30000, 25000, 390205))

# QUESTION 4
# Write a program that takes a temperature input in celsius
# and converts it to Fahrenheit and Kelvin. Return the converted temperature values in a list.
# Return calculated temperatures up to two decimal places.
# Return "Invalid" if K is less than 0.
# The formula to calculate the temperature in Fahrenheit from Celsius is:
# F = C*9/5 +32
# The formula to calculate the temperature in Kelvin from Celsius is:
# K = C + 273.15
# temp_conversion(0) ➞ [32, 273.15]
# # 0°C is equal to 32°F and 273.15 K.
# temp_conversion(100) ➞ [212, 373.15]
# temp_conversion(-10) ➞ [14, 263.15]
# temp_conversion(300.4) ➞ [572.72, 573.55]

# # SOLUTION
# def temp_conversion(temp):
#     to_fahrenheit = temp * 9 / 5 + 32
#     to_kelvin = temp + 273.15
#     if to_kelvin<0:
#         return 'Invalid'
#     return f'[{round(to_fahrenheit,2)},{round(to_kelvin,2)}]'
#
#
# print(temp_conversion(100))
# print(temp_conversion(-10))
# print(temp_conversion(300.4))

# QUESTION 5
# Given two unique integer lists a and b, and an integer target value v,
# create a function to determine whether there is a pair of numbers that
# add up to the target value v, where one number comes from one list a
# and the other comes from the second list b.
# Return True if there is a pair that adds up to the target value and False otherwise.
# sum_of_two([1, 2], [4, 5, 6], 5) ➞ True
# sum_of_two([1, 2], [4, 5, 6], 8) ➞ True
# sum_of_two([1, 2], [4, 5, 6], 3) ➞ False
# sum_of_two([1, 2], [4, 5, 6], 9) ➞ False

# # SOLUTION
#
# def sum_of_two(a, b, v):
#     decision = False
#     for number_in_a in a:
#         for number_in_b in b:
#             if number_in_a + number_in_b == v:
#                 decision = True
#     return decision
#
#
# print(sum_of_two([1, 2], [4, 5, 6], 5))
# print(sum_of_two([1, 2], [4, 5, 6], 8))
# print(sum_of_two([1, 2], [4, 5, 6], 3))
# print(sum_of_two([1, 2], [4, 5, 6], 9))


# QUESTION 6
# Create a function to test if a string is a valid pin or not.
# A valid pin has: Exactly 4 or 6 characters.
# Only numerical characters (0-9).
# No whitespace.
# Empty strings should return False when tested.
# Examples
# valid("1234") ➞ True
# valid("45135") ➞ False
# valid("89abc1") ➞ False
# valid("900876") ➞ True
# valid(" 4983") ➞ False

# # SOLUTION
# def valid(txt):
#     try:
#         if bool(txt) and len(txt) == 6 or len(txt) == 4:
#             if txt[0] == ' ' or txt[-1] == ' ':
#                 return False
#             else:
#                 int(txt)
#                 return True
#         else:
#             return False
#     except ValueError:
#         return False
#
#
# print(valid("1234"))
# print(valid("45135"))
# print(valid("89abc1"))
# print(valid("900876"))
# print(valid(" 4983"))
# print(valid(" "))
# print(valid(""))


# WEDNESDAY 30 NOV 2022

# QUESTION 1
# Create a function to perform basic arithmetic operations that includes
# addition, subtraction, multiplication and division on a string number
# (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").
# Here, we have 1 followed by a space, operator followed by another space and 2.
# For the challenge, we are going to have only two numbers between 1 valid operator.
# The return value should be a number.
#
# eval() is not allowed. In case of division, whenever the second number equals "0" return -1.
# For example:
# "15 // 0"  ➞ -1
# Examples
# arithmetic_operation("12 + 12") ➞ 24 // 12 + 12 = 24
# arithmetic_operation("12 - 12") ➞ 24 // 12 - 12 = 0
# arithmetic_operation("12 * 12") ➞ 144 // 12 * 12 = 144
# arithmetic_operation("12 // 0") ➞ -1 // 12 / 0 = -1

# # SOLUTION
# def arithmetic_operation(operation):
#     first_num, operator, second_num = operation.split(' ')
#     if second_num == '0':
#         return -1
#
#     if operator == '+':
#         return int(first_num) + int(second_num)
#     elif operator == '-':
#         return int(first_num) - int(second_num)
#     elif operator == '*':
#         return int(first_num) * int(second_num)
#     elif operator == '//':
#         return int(first_num) // int(second_num)
#
#
# print(arithmetic_operation("12 + 12"))
# print(arithmetic_operation("12 - 12"))
# print(arithmetic_operation("12 * 12"))
# print(arithmetic_operation("12 // 0"))


# QUESTION 2
# When resistors are connected together in series,
# the same current passes through each resistor in the chain and the total resistance,
# RT, of the circuit must be equal to the sum of all the individual resistors added together.
# That is:
# RT = R1 + R2 + R3 ...
# Create a function that takes an array of values resistance that are connected in series,
# and calculates the total resistance of the circuit in ohms.
# The ohm is the standard unit of electrical resistance in the International System of Units ( SI ).
# Notice the singular ohm for values <= 1.
# Examples
# series_resistance([1, 5, 6, 3]) ➞ "15 ohms"
# series_resistance([16, 3.5, 6]) ➞ "25.5 ohms"
# series_resistance([0.5, 0.5]) ➞ "1.0 ohm"

# # SOLUTION
# def series_resistance(list):
#     total_resistors = 0
#     for resistor in list:
#         total_resistors += resistor
#     return f"{total_resistors} {'Ohm' if total_resistors <= 1 else 'Ohms'}"
#
#
# print(series_resistance([1, 5, 6, 3]))
# print(series_resistance([16, 3.5, 6]))
# print(series_resistance([0.5, 0.5]))


# QUESTION 3
# This challenge is based on the classic video game "Snake".
# Assume the game screen is an n * n square, and the snake starts the game with length 1
# (i.e. just the head) positioned in the top left corner.
# For example, if n = 7 the game looks something like this:
# Oops no image
# In this version of the game, the length of the snake doubles each time it eats food
# (e.g. if the length is 4, after eating it becomes 8).
# Create a function that takes the side n of the game screen and
# returns the number of times the snake can eat before it runs out of space in the game screen.
# Examples
# snake_fill(3) ➞ 3
# snake_fill(6) ➞ 5
# snake_fill(24) ➞ 9

# # SOLUTION
# # 1 -> 2 -> 4 -> 8 -> 16 -> 32 -> 64 -> 128 ->256 -> 512 -> 1024 ...
#
# def snake_fill(length):
#     spaces = length * length
#     snake_length = 1
#     number_of_times = 0
#     while spaces > snake_length:
#         snake_length *= 2
#         number_of_times += 1
#     return number_of_times - 1
#
#
# print(snake_fill(3))
# print(snake_fill(6))
# print(snake_fill(24))


# QUESTION 4
# Create a function to check if a candidate is qualified in an
# imaginary coding interview of an imaginary tech startup.
#
# The criteria for a candidate to be qualified in the coding interview is:
#
# The candidate should have complete all the questions.
# The maximum time given to complete the interview is 120 minutes.
# The maximum time given for very easy questions is 5 minutes each.
# The maximum time given for easy questions is 10 minutes each.
# The maximum time given for medium questions is 15 minutes each.
# The maximum time given for hard questions is 20 minutes each.
# If all the above conditions are satisfied, return "qualified", else return "disqualified".
#
# You will be given a list of time taken by a candidate to solve a
# particular question and the total time taken by the candidate to complete the interview.
#
# Given a list , in a true condition will always be in the format
# [very easy, very easy, easy, easy, medium, medium, hard, hard].
# The maximum time to complete the interview includes a buffer time of 20 minutes.
#
# Examples
# interview([5, 5, 10, 10, 15, 15, 20, 20], 120) ➞ "qualified"
# interview([2, 3, 8, 6, 5, 12, 10, 18], 64) ➞  "qualified"
# interview([5, 5, 10, 10, 25, 15, 20, 20], 120) ➞ "disqualified"
# # Exceeded the time limit for a medium question.
# interview([5, 5, 10, 10, 15, 15, 20], 120) ➞ "disqualified"
# # Did not complete all the questions.
# interview([5, 5, 10, 10, 15, 15, 20, 20], 130) ➞ "disqualified"
# # Solved all the questions in their respected time limits but exceeded the total time limit of the interview.

# # SOLUTION
# def interview(lst, tot):
#     v_easy = lst[0:2]
#     easy = lst[2:4]
#     medium = lst[4:6]
#     hard = lst[6:8]
#
#     if len(lst) < 8 or tot > 120:
#         return 'Disqualified'
#     if v_easy[0] > 5 or v_easy[1] > 5:
#         return 'Disqualified'
#     if easy[0] > 10 or easy[1] > 10:
#         return 'Disqualified'
#     if medium[0] > 15 or medium[1] > 15:
#         return 'Disqualified'
#     if hard[0] > 20 or hard[1] > 20:
#         return 'Disqualified'
#
#     return 'qualified'
#
#
# print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))
# print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64))
# print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120))
# print(interview([5, 5, 10, 10, 15, 15, 20], 120))
# print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130))
