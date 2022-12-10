# FRIDAY, DECEMBER 2 2020

# QUESTION 1
# A number is said to be Disarium if the sum of its digits raised to
# their respective positions is the number itself.
# Create a function that determines whether a number is a Disarium or not.
# Examples
# is_disarium(75) ➞ False
# # 7^1 + 5^2 = 7 + 25 = 32
# is_disarium(135) ➞ True
# # 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
# is_disarium(544) ➞ False
# is_disarium(518) ➞ True
# is_disarium(466) ➞ False
# is_disarium(8) ➞ True


# # SOLUTION
# def is_disarium(number):
#     number_to_string = str(number)
#     index = 1
#     total_value = 0
#     for digit in number_to_string:
#         total_value += int(digit) ** index
#         index += 1
#
#     if total_value == number:
#         return True
#     else:
#         return False
#
#
# print(is_disarium(75))
# print(is_disarium(135))
# print(is_disarium(544))
# print(is_disarium(518))
# print(is_disarium(466))
# print(is_disarium(8))


# QUESTION 2
# In this challenge, establish if a given integer num is a Curzon number.
# If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num,
# then num is a Curzon number.
# Given a non-negative integer num, implement a function that returns True
# if num is a Curzon number, or False otherwise.
# Examples
# is_curzon(5) ➞ True
# # 2 ** 5 + 1 = 33
# # 2 * 5 + 1 = 11
# # 33 is a multiple of 11
# is_curzon(10) ➞ False
# # 2 ** 10 + 1 = 1025
# # 2 * 10 + 1 = 21
# # 1025 is not a multiple of 21
# is_curzon(14) ➞ True
# # 2 ** 14 + 1 = 16385
# # 2 * 14 + 1 = 29
# # 16385 is a multiple of 29

# # SOLUTION
# def is_curzon(num):
#     two_raised_num = 2 ** num + 1
#     two_by_num = 2 * num + 1
#
#     if two_raised_num % two_by_num == 0:
#         return True
#     else:
#         return False
#
#
# print(is_curzon(5))
# print(is_curzon(10))
# print(is_curzon(14))


#  QUESTION 3
# Create a function that takes two arguments:
# the original price and the discount percentage as integers and
# returns the final price after the discount.
# Examples
# dis(1500, 50) ➞ 750
# dis(89, 20) ➞ 71.2
# dis(100, 75) ➞ 25

# # SOLUTION
# def dis(price, discount):
#     return price - discount / 100 * price
#
#
# print(dis(1500, 50))
# print(dis(89, 20))
# print(dis(100, 75))


# QUESTION 4
# Given a positive number x, if all the positive divisors of x (excluding x) add up to x,
# then x is said to be a perfect number.
# For example, the set of positive divisors of 6 excluding 6 itself is (1, 2, 3).
# The sum of this set is 6. Therefore, 6 is a perfect number.
# Given a positive number x, if all the positive divisors of x add up to a second number y,
# and all the positive divisors of y add up to x, then x and y are said to be a pair of
# amicable numbers.
# Create a function that takes a number and returns
# "Perfect" if the number is perfect, "Amicable" if the number is part of an amicable pair,
# or "Neither".
# Examples
# num_type(6) ➞ "Perfect"
# num_type(2924) ➞ "Amicable"
# num_type(5010) ➞ "Neither"

# # SOLUTIONS
# def num_type(num):
#     divisors = []
#     for divisor in range(num):
#         if divisor != 0 and num % divisor == 0:
#             divisors.append(divisor)
#     sum_of_divisors = 0
#     for digit in divisors:
#         sum_of_divisors += digit
#     if sum_of_divisors == num:
#         return 'Perfect'
#
#     divisors.clear()
#     for divisor in range(sum_of_divisors):
#         if divisor != 0 and sum_of_divisors % divisor == 0:
#             divisors.append(divisor)
#     sum_of_divisors2 = 0
#     for digit in divisors:
#         sum_of_divisors2 += digit
#     if sum_of_divisors2 == sum_of_divisors:
#         return 'Amicable'
#     else:
#         return 'Neither'
#
#
# print(num_type(6))
# print(num_type(2924))
# print(num_type(5010))


# QUESTION 5
# Given a list of numbers, create a function that removes 25% from every number
# in the list except the smallest number, and adds the total amount removed
# to the smallest number.
# Examples
# show_the_love([4, 1, 4]) ➞ [3, 3, 3]
# show_the_love([16, 10, 8]) ➞ [12, 7.5, 14.5]
# show_the_love([2, 100]) ➞ [27, 75]

# # SOLUTION
# def show_the_love(number_list):
#     empty_array = []
#     to_add = 0
#     minimal_number = min(number_list)
#     for number in number_list:
#         if number != min(number_list):
#             reduced = number * .75
#             to_add += number * .25
#             empty_array.append(reduced)
#         if number == min(number_list):
#             empty_array.append(number)
#
#     empty_array[empty_array.index(minimal_number)] = minimal_number + to_add
#     return empty_array
#
#
# print(show_the_love([4, 1, 4]))
# print(show_the_love([16, 10, 8]))
# print(show_the_love([2, 100]))
# print(show_the_love([10, 20, 40, 80, 100]))


# SUN, DEC 4 2022


# QUESTION 1
# Create a function that creates a box based on dimension n.
# Examples
# make_box(5) ➞ [
#   "#####",
#   "#   #",
#   "#   #",
#   "#   #",
#   "#####"
# ]
# make_box(3) ➞ [
#   "###",
#   "# #",
#   "###"
# ]
# make_box(2) ➞ [
#   "##",
#   "##"
# ]
# make_box(1) ➞ [
#   "#"
# ]

# # SOLUTION
# def make_box(n):
#     for value in range(n):
#         if value == 0 or value == n - 1:
#             print('#' * n)
#         else:
#             print(f'#{(n - 2) * " "}#')
#
#     return ''
#
#
# print(make_box(5))
# print(make_box(3))
# print(make_box(2))
# print(make_box(1))


# QUESTION 2
# Given a list of words in the singular form, return a set of those words in the plural form
# if they appear more than once in the list.
# Examples
# pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }
# pluralize(["table", "table", "table"]) ➞ { "tables" }
# pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }

# # SOLUTION
# def pluralize(lst):
#     new_array = []
#     for word in lst:
#         if lst.count(word) > 1 and not word + 's' in new_array:
#             new_array.append(word + 's')
#         elif lst.count(word) == 1:
#             new_array.append(word)
#     return new_array
#
#
# print(pluralize(["cow", "pig", "cow", "cow"]))
# print(pluralize(["table", "table", "table"]))
# print(pluralize(["chair", "pencil", "arm"]))

# QUESTION 3
# Create a function that takes an angle in radians and
# returns the corresponding angle in degrees rounded to one decimal place.
# Examples
# radians_to_degrees(1) ➞ 57.3
# radians_to_degrees(20) ➞ 1145.9
# radians_to_degrees(50) ➞ 2864.8
# Notes
# The number π can be loaded from the math module with from math import pi.

# # SOLUTION
# from math import pi
#
#
# def radians_to_degrees(rad):
#     return round(rad * 180 / pi, 1)
#
#
# print(radians_to_degrees(1))
# print(radians_to_degrees(20))
# print(radians_to_degrees(50))


# QUESTION 4
# Create a function that takes a string's characters as ASCII and
# returns each character's hexadecimal value as a string.
# Examples
# convert_to_hex("hello world") ➞ "68 65 6c 6c 6f 20 77 6f 72 6c 64"
# convert_to_hex("Big Boi") ➞ "42 69 67 20 42 6f 69"
# convert_to_hex("Marty Poppinson") ➞ "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e"

# # SOLUTION
# def convert_to_hex(txt):
#     hexa = ''
#     for i in txt:
#         int_value = ord(i)
#         hexadecimal = hex(int_value).lstrip('0x').rstrip('L')
#         hexa += hexadecimal
#         hexa += ' '
#     return hexa
#
#
# print(convert_to_hex("hello world"))
# print(convert_to_hex("Big Boi"))
# print(convert_to_hex("Marty Poppinson"))


#  QUESTION 5
# Create a function that takes a string as an argument and returns the Morse code equivalent.
# Examples
# encode_morse("EDABBIT CHALLENGE") ➞ ". -.. .- -... -... .. -
# -.-. .... .- .-.. .-.. . -. --. ."
# encode_morse("HELP ME !") ➞ ".... . .-.. .--.   -- .   -.-.--"
# This dictionary can be used for coding:
# char_to_dots = {
#   'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#   'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#   'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#   'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
#   '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
#   '6': '-....', '7': '--...', '8': '---..', '9': '----.',
#   '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
#   ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
#   '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
# }

# # SOLUTION
# def encode_morse(message):
#     encoded = ''
#     char_to_dots = {
#         'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#         'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#         'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
#         '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
#         '6': '-....', '7': '--...', '8': '---..', '9': '----.',
#         '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
#         ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
#         '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
#     }
#     for character in message.upper():
#         encoded += char_to_dots[character]
#         encoded += ' '
#     return encoded
#
#
# print(encode_morse("EDAbBIT CHALLENGE"))
# print(encode_morse("HELP ME !"))
# print(encode_morse("jArvis23+=12 "))


# QUESTION 6
# Create a function which concatenates the number 7 to the end of every chord in a list.
# Ignore all chords which already end with 7.
# Examples
# jazzify(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]
# jazzify(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]
# jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]
# jazzify([]) ➞ []

# # SOLUTION
# def jazzify(lst):
#     jazzified = []
#     for value in lst:
#         if value[-1] != '7':
#             jazzified.append(value + '7')
#         else:
#             jazzified.append(value)
#     return jazzified
#
#
# print(jazzify(["G", "F", "C"]))
# print(jazzify(["Dm", "G", "E", "A"]))
# print(jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]))
# print(jazzify([]))


# MONDAY, 5 DECEMBER 2022

# QUESTION 1

# Someone has attempted to censor my strings by replacing every vowel with
# a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.
# Given a censored string and a string of the censored vowels, return the original uncensored string.
# Example
# uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"
# uncensor("abcd", "") ➞ "abcd"
# uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"

# # SOLUTION
# def uncensor(txt, vowels):
#     if vowels == '' or vowels == ' ':
#         return txt
#     for vowel in vowels:
#         txt = txt.replace('*', vowel, 1)
#     return txt


# print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
# print(uncensor("abcd", ""))
# print(uncensor("*PP*RC*S*", "UEAE"))
