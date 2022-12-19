# SAT DEC 17, 2022


# QUESTION 1


# Given a sentence as txt, return True if any two adjacent words have this property:
# One word ends with a vowel, while the word immediately after begins with a vowel (a e i o u).
# Examples
# vowel_links("a very large appliance") ➞ True
# vowel_links("go to edabit") ➞ True
# vowel_links("an open fire") ➞ False
# vowel_links("a sudden applause") ➞ False


# # SOLUTION
# def vowel_links(txt):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     txt_array = txt.split(' ')
#     index = 0
#     for word in txt_array:
#         index += 1
#         if index < len(txt_array):
#             if word[-1] in vowels and txt_array[index][0] in vowels:
#                 output = True
#             else:
#                 output = False
#     return output
#
#
# print(vowel_links("a very large appliance"))
# print(vowel_links("go to edabit"))
# print(vowel_links("an open fire"))
# print(vowel_links("a sudden applause"))


# QUESRTION 2


# "Loves me, loves me not" is a traditional game in which a person
# plucks off all the petals of a flower one by one, saying the phrase
# "Loves me" and "Loves me not" when determining whether the one that they love, loves them back.

# Given a number of petals, return a string which repeats the phrases
# "Loves me" and "Loves me not" for every alternating petal,
# and return the last phrase in all caps. Remember to put a comma and space between phrases.
# Examples
# loves_me(3) ➞ "Loves me, Loves me not, LOVES ME"
# loves_me(6) ➞ "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"
# loves_me(1) ➞ "LOVES ME"


# # SOLUTION
# def loves_me(n):
#     final_string = ''
#     for number in range(n):
#         if number % 2 == 0:
#             if number == n - 1:
#                 final_string += 'LOVES ME'
#             else:
#                 final_string += 'Loves me, '
#         else:
#             if number == n - 1:
#                 final_string += 'LOVES ME NOT'
#             else:
#                 final_string += 'Loves me not, '
#
#     return final_string
#
#
# print(loves_me(3))
# print(loves_me(6))
# print(loves_me(1))


# MON DEC 19, 2022


# QUESTION 1

# A Collatz sequence is generated by repeatedly applying
# the following rules to an integer and then to each resulting integer in turn:
# If even: divide by 2.
# If odd: multiply by 3, then add 1.
# The Collatz algorithm has been tested and found to always reach 1 for all positive integers.
# Create a function that, when given two positive integers a b, 
# returns the string "a" if integer a took fewer steps to reach 1 than b 
# when passed through the Collatz sequence, or "b" if integer b took fewer steps to reach 1 than a.
# Examples
# collatz(10, 15) ➞ "a"
# # Because 10.0 - 5.0 - 16.0 - 8.0 - 4.0 - 2.0 - 1.0: 6 steps
# # 15.0 - 46.0 - 23.0 - 70.0 - 35.0 - 106.0 - 53.0 - 160.0 - 80.0
# - 40.0 - 20.0 - 10.0 - 5.0 - 16.0 - 8.0 - 4.0 - 2.0 - 1.0: 17 steps
# collatz(13, 16) ➞ "b"
# collatz(53782, 72534) ➞ "b"

# # SOLUTION
# def collatz(a, b):
#     a_num = b_num = 0
#     while a != 1:
#         if a % 2 == 0 and a != 1:
#             a /= 2
#             a_num += 1
#         elif a % 2 == 1 and a != 1:
#             a = a * 3 + 1
#             a_num + 1
#     while b != 1:
#         if b % 2 == 0 and b != 1:
#             b /= 2
#             b_num += 1
#         elif b % 2 == 1 and b != 1:
#             b = b * 3 + 1
#             b_num += 1
#     print(a_num, b_num)
#     if a_num > b_num:
#         return "b"
#     elif b_num > a_num:
#         return 'a'
#
#
# print(collatz(10, 15))
# print(collatz(13, 16))
# print(collatz(53782, 72534))


# QUESTION 2


# Given a predetermined rate from a dictionary, write the function that
# will return the time it takes for a certain amount of people to paint
# a certain amount of walls.
# The "rate" dictionary shows how many minutes it takes "people" people
# to paint "walls" walls. At that same rate, how long should
# it take based on the new variables. Return the minutes as an integer. No rounding is necessary.
# Example
# # It takes 22 minutes for 10 people to paint 10 walls.
# # How many minutes does it take 14 people to paint 14 walls?
# rate = {
#   "people": 10,
#   "walls": 10,
#   "minutes": 22
# }
# time(rate, people, walls) ➞ 22

# # SOLUTION
# def time(rate, people, walls):
#     return rate["minutes"] * (walls / rate["people"])
#
#
# rate = {
#     "people": 10,
#     "walls": 10,
#     "minutes": 22
# }
#
# print(time(rate, 14, 14))


# QUESTION 3


# Create a function based on the input and output. Look at the examples, there is a pattern.
# Examples
# secret("p.one.two.three") ➞ "<p class='one two three'></p>"
# secret("p.one") ➞ "<p class='one'></p>"
# secret("p.four.five") ➞ "<p class='four five'></p>"


# # SOLUTION
# def secret(txt):
#     msg = ''
#     txt_split = txt.split('.')
#     for number in txt_split[1:]:
#         msg += number
#         if number != txt_split[-1]:
#             msg += ' '
#
#     return f"<{txt_split[0]} class='{msg}'></p>"
#
#
# print(secret("p.one.two.three"))
# print(secret("p.one"))
# print(secret("p.four.five"))


# QUESTION 4


# There are three cups on a table, at positions A, B, and C.
# At the start, there is a ball hidden under the cup at position B.
# Image cups where ball is under middle cup
# However, I perform several swaps on the cups, which is notated as two letters.
# For example, if I swap the cups at positions A and B, I could notate this as AB or BA.
# Create a function that returns the letter position that the ball is at,
# once I finish swapping the cups. The swaps will be given to you as a list.

# Worked Example
# cup_swapping(["AB", "CA", "AB"]) ➞ "C"
# # Ball begins at position B.
# # Cups A and B swap, so the ball is at position A.
# # Cups C and A swap, so the ball is at position C.
# # Cups A and B swap, but the ball is at position C, so it doesn't move.
# Examples

# cup_swapping(["AB", "CA"]) ➞ "C"
# cup_swapping(["AC", "CA", "CA", "AC"]) ➞ "B"
# cup_swapping(["BA", "AC", "CA", "BC"]) ➞ "A"

# # SOLUTION
# def cup_swapping(swaps):
#     position = 'B'
#     placeholder = ''
#     first_b = False
#     for swap in swaps:
#         if swap[-1] == 'B' and first_b == True and swap[0] == placeholder:
#             position = swap[0]
#             placeholder = swap[0]
#         if swap[-1] == placeholder:
#             position = swap[0]
#             placeholder = swap[0]
#
#         if swap[-1] == 'B' and first_b == False:
#             first_b = True
#             position = swap[0]
#             placeholder = swap[0]
#
#     return position
#
#
# print(cup_swapping(["AB", "CA", "AB"]))
# print(cup_swapping(["AB", "CA"]))
# print(cup_swapping(["AC", "CA", "CA", "AC"]))
# print(cup_swapping(["BA", "AC", "CA", "BC"]))
#
#
#
# print()
# print(cup_swapping(["AB", "CA"])) # Output: C
# print(cup_swapping(["AC", "CA", "CA", "AC"])) # Output: A
# print(cup_swapping(["BA", "AC", "CA", "BC"])) # Output: C
