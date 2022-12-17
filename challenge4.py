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
