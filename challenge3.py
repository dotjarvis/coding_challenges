# THUR DEC, 8 2022


# QUESTION 1


# Luke Skywalker has family and friends. Help him remind them who is who.
# Given a string with a name, return the relation of that person to Luke.
# Person	        Relation
# Darth Vader	    father
# Leia	            sister
# Han	            brother-in-law
# R2D2	            droid
# Examples
# relation_to_luke("Darth Vader") ➞ "Luke, I am your father."
# relation_to_luke("Leia") ➞ "Luke, I am your sister."
# relation_to_luke("Han") ➞ "Luke, I am your brother in law."

# # SOLUTION
# def relation_to_luke(name):
#     person_relation = {
#         'Darth Vader': 'father',
#         'Leia': 'sister',
#         'Han': 'brother-in-law',
#         'R2D2': 'droid',
#     }
#
#     return f'Luke, I am your {person_relation.get(name, "UNKOWN")}'
#
#
# print(relation_to_luke("Darth Vader"))
# print(relation_to_luke("Leia"))
# print(relation_to_luke("Han"))
# print(relation_to_luke("Hussain"))


# QUESTION 2


# Create a function that takes a number as input and returns True
# if the sum of its digits has the same parity as the entire number.
# Otherwise, return False.
# Examples
# parity_analysis(243) ➞ True
# # 243 is odd and so is 9 (2 + 4 + 3)
# parity_analysis(12) ➞ False
# # 12 is even but 3 is odd (1 + 2)
# parity_analysis(3) ➞ True
# # 3 is odd and 3 is odd and 3 is odd (3)

# # SOLUTION
# def parity_analysis(num):
#     total_sum = 0
#     for digit in str(num):
#         total_sum += int(digit)
#     if num % 2 == 0 and total_sum % 2 == 0:
#         return True
#     elif num % 2 == 1 and total_sum % 2 == 1:
#         return True
#     else:
#         return False
#
#
# print(parity_analysis(243))
# print(parity_analysis(12))
# print(parity_analysis(3))
# print(parity_analysis(2003))


# QUESTION 3


# Write a function that returns True if two arrays, when combined, form a consecutive sequence.
# A consecutive sequence is a sequence without any gaps in the integers,
# e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.
# Examples
# consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True
# consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False
# consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False
# consecutive_combo([44, 46], [45]) ➞ True

# # SOLUTION
# def consecutive_combo(lst1, lst2):
#     overall_list = []
#     for lst in lst1:
#         overall_list.append(lst)
#     for lst in lst2:
#         overall_list.append(lst)
#     overall_list.sort()
#
#     if overall_list[0] + len(overall_list) - 1 == overall_list[-1]:
#         return True
#     else:
#         return False
#
#
# print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
# print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))
# print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))
# print(consecutive_combo([44, 46], [45]))


# FRIDAY DEC, 9 2022

# QUESTION 1


# Write a function that takes a list of lists and returns the value of all of the symbols in it,
# where each symbol adds or takes something from the total score. Symbol values:
# # = 5
# O = 3
# X = 1
# ! = -1
# !! = -3
# !!! = -5
# A list of lists containing 2 #s, a O, and a !!! would equal (0 + 5 + 5 + 3 - 5) 8.
# If the final score is negative, return 0 (e.g. 3 #s, 3 !!s, 2 !!!s and a X would be (0 + 5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) -3, so return 0.
# Examples
# check_score([
#   ["#", "!"],
#   ["!!", "X"]
# ]) ➞ 2
# check_score([
#   ["!!!", "O", "!"],
#   ["X", "#", "!!!"],
#   ["!!", "X", "O"]
# ]) ➞ 0
# check_score([
#   ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
#   ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
#   ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
#   ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
#   ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
#   ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
#   ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
#   ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
#   ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
#   ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
#   ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
#   ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
#   ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
#   ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]
# ]) ➞ 12

# # SOLUTION
# def check_score(symbol_list):
#     total = 0
#     symbol_dict = {
#         '#': 5,
#         'O': 3,
#         'X': 1,
#         '!': -1,
#         '!!': -3,
#         '!!!': -5,
#     }
#     for outer in symbol_list:
#         for symbol in outer:
#             total += symbol_dict.get(symbol, 'NONE')
#     if total > 0:
#         return total
#     else:
#         return 0
#
#
# print(check_score([
#     ["#", "!"],
#     ["!!", "X"]
# ]))
# print(check_score([
#     ["!!!", "O", "!"],
#     ["X", "#", "!!!"],
#     ["!!", "X", "O"]
# ]))
# print(check_score([
#     ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
#     ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
#     ["#", "X", "#", "!!!", "!"],
#     ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
# ]))


# QUESTION 2


# A financial institution provides professional services to banks and claims charges
# from the customers based on the number of man-days provided.
# Internally, it has set a scheme to motivate and reward staff to meet
# and exceed targeted billable utilization and revenues by paying a bonus for
# each day claimed from customers in excess of a threshold target.
# This quarterly scheme is calculated with a threshold target of 32 days per quarter, a
# nd the incentive payment for each billable day in excess of such threshold target is
# shown as follows:
# Days          	        Bonus
# 0 to 32 days  	        Zero
# 33 to 40 days	            SGD$325 per billable day
# 41 to 48 days         	SGD$550 per billable day
# Greater than 48 days	    SGD$600 per billable day

# Please note that incentive payment is calculated progressively.
# As an example, if an employee reached total billable days of 45 in a quarter,
# his/her incentive payment is computed as follows:
# 32*0 + 8*325 + 5*550 = 5350

# Write a function to read the billable days of an employee and return the b
# onus he/she has obtained in that quarter.
# Examples
# bonus(15) ➞ 0
# bonus(37) ➞ 1625
# bonus(50) ➞ 8200

# # SOLUTION
# def bonus(days):
#     bonus_cash = 0
#     if days <= 32:
#         bonus_cash += 32 * 0
#     if 32 < days <= 40:
#         bonus_cash += 0 + (days - 32) * 325
#     if 40 < days <= 48:
#         bonus_cash += (8 * 325) + (days - 40) * 550
#     if days > 48:
#         bonus_cash += (8 * 325) + (8 * 550) + (days - 48) * 600
#     return bonus_cash
#
#
# print(bonus(15))
# print(bonus(37))
# print(bonus(50))
# print(bonus(52))


# QUESTION 3


# Given the month and year as numbers, return whether that month contains a Friday 13th.
# Examples
# has_friday_13(3, 2020) ➞ True
# has_friday_13(10, 2017) ➞ True
# has_friday_13(1, 1985) ➞ False
# Notes
# January will be given as 1, February as 2, etc ...
# Check Resources for some helpful tutorials on Python's datetime module.

# # SOLUTION
# import datetime
#
#
# def has_friday_13(month, year):
#     the_date = datetime.date(year, month, 13)
#     if the_date.isoweekday() == 5:
#         return True
#     else:
#         return False
#
#
# print(has_friday_13(3, 2020))
# print(has_friday_13(10, 2017))
# print(has_friday_13(1, 1985))


# QUESTION 4


# Create a function that takes a list and string.
# The function should remove the letters in the string from the list, and return the list.
# Examples
# remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]
# remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]
# remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []

# # SOLUTION
# def remove_letters(letters, word):
#     extra_letters = []
#     for letter in letters:
#         if letter not in word:
#             extra_letters.append(letter)
#     return extra_letters
#
# print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))
# print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))
# print(remove_letters(["d", "b", "t", "e", "a", "i"], "edabit"))
# print(remove_letters(["d", "0", "y", "e", "o", "b"], "boy"))


# QUESTION 5


# Make a function that encrypts a given input with these steps:
# Input: "apple"
# Step 1: Reverse the input: "elppa"
# Step 2: Replace all vowels using the following chart:
# a => 0
# e => 1
# i => 2
# o => 2
# u => 3
# # "1lpp0"
# Step 3: Add "aca" to the end of the word: "1lpp0aca"
# Output: "1lpp0aca"
# Examples
# encrypt("banana") ➞ "0n0n0baca"
# encrypt("karaca") ➞ "0c0r0kaca"
# encrypt("burak") ➞ "k0r3baca"
# encrypt("alpaca") ➞ "0c0pl0aca"

# # SOLUTION
# def encrypt(word):
#     replacement = {
#         'a': '0',
#         'e': '1',
#         'i': '2',
#         'o': '2',
#         'u': '3',
#     }
#     word_to_array = []
#     for letter in word.lower():
#         word_to_array.append(letter)
#     word_to_array.reverse()
#     replaced_word = ''
#     for ltr in word_to_array:
#         if replacement.get(ltr):
#             replaced_word += replacement.get(ltr)
#         else:
#             replaced_word += ltr
#     return replaced_word + 'aca'
#
#
# print(encrypt("banana"))
# print(encrypt("karaca"))
# print(encrypt("burak"))
# print(encrypt("alpaca"))
# print(encrypt("BoYs"))


# QUESTION 6


# A city skyline can be represented as a 2-D list with
# 1s representing buildings. In the example below,
# the height of the tallest building is 4 (second-most right column).
# [[0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 1, 0],
# [0, 0, 1, 0, 1, 0],
# [0, 1, 1, 1, 1, 0],
# [1, 1, 1, 1, 1, 1]]
# Create a function that takes a skyline (2-D list of 0's and 1's)
# and returns the height of the tallest skyscraper.
# Examples
# tallest_skyscraper([
#   [0, 0, 0, 0],
#   [0, 1, 0, 0],
#   [0, 1, 1, 0],
#   [1, 1, 1, 1]
# ]) ➞ 3
# tallest_skyscraper([
#   [0, 1, 0, 0],
#   [0, 1, 0, 0],
#   [0, 1, 1, 0],
#   [1, 1, 1, 1]
# ]) ➞ 4
# tallest_skyscraper([
#   [0, 0, 0, 0],
#   [0, 0, 0, 0],
#   [1, 1, 1, 0],
#   [1, 1, 1, 1]
# ]) ➞ 2


# # SOLUTION
# def tallest_skyscraper(lists):
#     height = 0
#     for lst in lists:
#         if 1 in lst:
#             height += 1
#     return height
#
#
# print(tallest_skyscraper([
#     [0, 0, 0, 0],
#     [0, 1, 0, 0],
#     [0, 1, 1, 0],
#     [1, 1, 1, 1]
# ]))
# print(tallest_skyscraper([
#     [0, 1, 0, 0],
#     [0, 1, 0, 0],
#     [0, 1, 1, 0],
#     [1, 1, 1, 1]
# ]))
# print(tallest_skyscraper([
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [1, 1, 1, 0],
#     [1, 1, 1, 1]
# ]))


# SATURDAY DEC, 10 2022


# QUESTION 1


# Given a name, return the letter with the highest index in alphabetical order,
# with its corresponding index, in the form of a string.
# You are prohibited to use max() nor is reassigning a value to the alphabet list allowed.
# Examples
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
# "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# alphabet_index("Flavio") ➞ "22v"
# alphabet_index("Andrey") ➞ "25y"
# alphabet_index("Oscar") ➞ "19s"
# Notes
# sorted() is not best practice.


# # SOLUTION
# def alphabet_index(string):
#     alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
#                 "v", "w", "x", "y", "z"]
#     highest_index = 'a'
#     for letter in string.lower():
#         if letter > highest_index:
#             highest_index = letter
#
#     return str(alphabet.index(highest_index) + 1) + highest_index
#
#
# print(alphabet_index("Flavio"))
# print(alphabet_index("Andrey"))
# print(alphabet_index("Oscar"))

# QUESTION 2


# If a person traveled up a hill for 18mins at 20mph and
# then traveled back down the same path at 60mph then their average speed traveled was 30mph.
# Write a function that returns the average speed traveled given an uphill time,
# uphill rate and a downhill rate. Uphill time is given in minutes.
# Return the rate as an integer (mph). No rounding is necessary.
# Examples
# ave_spd(18, 20, 60) ➞ 30
# ave_spd(30, 10, 30) ➞ 15
# ave_spd(30, 8, 24) ➞ 12


# SOLUTION
# def ave_spd(up_time, up_spd, down_spd):
#     distance = (up_time / 60) * up_spd
#     down_time = distance / down_spd
#     avg_speed = distance * 2 / ((up_time + down_time * 60) / 60)
#     return int(avg_speed)
#
#
# print(ave_spd(18, 20, 60))
# print(ave_spd(30, 10, 30))
# print(ave_spd(30, 8, 24))


# QUESTION 3


# Create a function that takes an integer n and returns the factorial of factorials.
# See below examples for a better understanding:
# Examples
# fact_of_fact(4) ➞ 288
# # 4! * 3! * 2! * 1! = 288
# fact_of_fact(5) ➞ 34560
# fact_of_fact(6) ➞ 24883200


# # SOLUTION
# def fact_of_fact(n):
#     # 4 * 3 * 2 * 1 * 3 * 2 * 1 * 2 * 1 * 1 = 288
#     total = 1
#     for value in range(n + 1):
#         if value != 0:
#             for val in range(value + 1):
#                 if val != 0:
#                     total *= val
#     return total
#
#
# print(fact_of_fact(4))
# print(fact_of_fact(5))
# print(fact_of_fact(6))


# QUESTION 4


# Create a function that takes a number a and finds the missing exponent x
# so that a when raised to the power of x is equal to b.
# Examples
# solve_for_exp(4, 1024) ➞ 5
# solve_for_exp(2, 1024) ➞ 10
# solve_for_exp(9, 3486784401) ➞ 10
# Notes
# a is raised to the power of what in order to equal b?

# # SOLUTION
# def solve_for_exp(a, b):
#     n = 0
#     while True:
#         if a ** n == b:
#             return n
#         n += 1
#
#
# print(solve_for_exp(4, 1024))
# print(solve_for_exp(2, 1024))
# print(solve_for_exp(9, 3486784401))


# QUESTION 5


# Create a function that returns the majority vote in a list.
# A majority vote is an element that occurs > N/2 times in a list
# (where N is the length of the list).
# Examples
# majority_vote(["A", "A", "B"]) ➞ "A"
# majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"
# majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None
# Notes
# The frequency of the majority element must be strictly greater than 1/2.
# If there is no majority element, return None.
# If the list is empty, return None.

# SOLUTION
# def majority_vote(lst):
#     first_iteration = lst.count(lst[0])
#     output = None
#     for vote in lst:
#         if lst.count(vote) > first_iteration:
#             first_iteration = lst.count(vote)
#             output = vote
#         else:
#             output=lst[0]
#     return output
#
# print(majority_vote(["A", "A", "B"]))
# print(majority_vote(["A", "A", "A", "B", "C", "A"]))
# print(majority_vote(["A", "B", "B", "A", "C", "C"]))
# print(majority_vote(["D", "B", "B", "A", "C", "C"]))


# MON DEC 12, 2022


# QUESTION 1


# Create a function that takes a string txt and censors any word from a given list lst.
# The text removed must be replaced by the given character char.
# Examples
# censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"
# censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")
# censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*")
# ➞ "Why *** the ******* cross the ****?"


# # SOLUTION
# def censor_string(txt, lst, char):
#     censored_txt = ''
#     for word in txt.split(' '):
#         if word.lower() in lst:
#             censored_txt += char * len(word.lower())
#             censored_txt += ' '
#         else:
#             censored_txt += word
#             censored_txt += ' '
#
#     return censored_txt
#
#
# print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))
# print(censor_string("The cow jumped over the moon.", ["cow", "over"], "*"))
# print(censor_string("Why did the chicken cross the road ?", ["Did", "chicken", "road"], "*"))


# TUE, DEC 13 2022


# QUESTION 1
# Given a list of integers representing the color of each sock,
# determine how many pairs of socks with matching colors there are.
# For example, there are 7 socks with colors [1, 2, 1, 2, 1, 3, 2].
# There is one pair of color 1 and one of color 2.
# There are three odd socks left, one of each color. The number of pairs is 2.
#
# Create a function that returns an integer representing the number of
# matching pairs of socks that are available.
# Examples
# sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]) ➞ 3
# sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]) ➞ 4
# sock_merchant([]) ➞ 0

# # SOLUTION
# def sock_merchant(lst):
#     unique_array = []
#     total = 0
#     for color in lst:
#         if color not in unique_array:
#             unique_array.append(color)
#             number = lst.count(color)
#             total += number // 2
#
#     return total
#
#
# print(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))
# print(sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]))
# print(sock_merchant([]))


# WED DEC, 14 2022


# QUESTION 1

# Given a function that accepts unlimited arguments,
# check and count how many data types are in those arguments.
# Finally return the total in a list.
# List order is:
# [int, str, bool, list, tuple, dictionary]
# Examples
# count_datatypes(1, 45, "Hi", False) ➞ [2, 1, 1, 0, 0, 0]
# count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1) ➞ [3, 0, 0, 1, 1, 0]
# count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23) ➞ [2, 2, 3, 1, 0, 2]
# count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]) ➞ [2, 0, 1, 2, 2, 0]
# Notes
# If no arguments are given, return [0, 0, 0, 0, 0, 0]


# # SOLUTION
# def count_datatypes(*args):
#     if not bool(args):
#         return [0, 0, 0, 0, 0, 0]
#     int_type = str_type = bool_type = list_type = tuple_type = dictionary_type = 0
#
#     for data_type in args:
#         if type(data_type) == int:
#             int_type += 1
#         elif type(data_type) == str:
#             str_type += 1
#         elif type(data_type) == bool:
#             bool_type += 1
#         elif type(data_type) == list:
#             list_type += 1
#         elif type(data_type) == tuple:
#             tuple_type += 1
#         elif type(data_type) == dict:
#             dictionary_type += 1
#
#     return [int_type, str_type, bool_type, list_type, tuple_type, dictionary_type]
#
#
# print(count_datatypes(1, 45, "Hi", False))
# print(count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1))
# print(count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23))
# print(count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]))
# print(count_datatypes())


# THURSDAY DEC, 15 2022

# QUESTION 1

# Create a function which takes in an encoded string and
# returns a dictionary according to the following example:
# Examples
# parse_code("John000Doe000123") ➞ {
#   "first_name": "John",
#   "last_name": "Doe",
#   "id": "123"
# }
# parse_code("michael0smith004331") ➞ {
#   "first_name": "michael",
#   "last_name": "smith",
#   "id": "4331"
# }
# parse_code("Thomas00LEE0000043") ➞ {
#   "first_name": "Thomas",
#   "last_name": "LEE",
#   "id": "43"
# }

# # SOLUTION
# def parse_code(txt):
#     obj = {
#         "first_name": "",
#         "last_name": "",
#         "id": ""
#     }
#     for key in obj:
#         for names in txt.split('0'):
#             if bool(names):
#                 obj[key] = names
# 
#     return obj
# 
# 
# print(parse_code("Thomas00LEE0000043"))
# print(parse_code("michael0smith004331"))
# print(parse_code("John000Doe000123"))
