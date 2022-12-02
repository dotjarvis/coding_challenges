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
