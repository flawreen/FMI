"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
"""
# digits = [3, 9, 9]
# rez = []
# leng = len(digits)
# if digits[-1] == 9 and len(digits) > 1:
#     i = leng-1
#     while digits[i] == 9:
#         digits[i] = 0
#         i -= 1
#     if digits[0] == 0:
#         digits[1:] = digits[:]
#         digits[0] = digits[1] + 1
#     else:
#         digits[i] += 1
# elif digits[-1] == 9 and len(digits) == 1:
#     digits = 1, 0
# else:
#     digits[-1] += 1
# print(digits)
"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
nums = [0,0]
i = len(nums)-1
# while i > 1:
#     if nums[i] == nums[i-2]:
#         nums[i:] = nums[i+1:]
#     i -= 1
# print(nums)

# s = "MMMCDXC"
# d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL':40, 'XC': 90, 'CD': 400, 'CM':900}
# nr = 0
# i = len(s)-1
# while i > -1:
#     if s[i-1] + s[i] not in d:
#         # print(s[i-1] + s[i], end="\n\n")
#         nr += d[s[i]]
#         i -= 1
#     else:
#         print(s[i-1] + s[i], end="\n\n")
#         nr += d[s[i-1]+s[i]]
#         i -= 2
# print(nr)

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""
# s = input()
# def abc(s):
#     stak = []
#     length = 0
#     if len(s) < 2:
#         return False
#     match s[0]:
#         case ']' | '}' | ')':
#             return False
#         case _:
#             for c in s:
#                 match c:
#                     case '(' | '[' | '{':
#                         stak.append(c)
#                         length += 1
#                     case ']' if length > 0 and stak[-1] == '[':
#                         length -= 1
#                         stak.pop()
#                     case ')' if length > 0 and stak[-1] == '(':
#                         length -= 1
#                         stak.pop()
#                     case '}' if length > 0 and stak[-1] == '{':
#                         length -= 1
#                         stak.pop()
#                     case _:
#                         return False
#     if length == 0:
#         return True
#     else:
#         return False

# print(abc(s))


# d1 = {'(': 0, '[': 1, '{': 2}
# d2 = {0: ')', 1: ']', 2: '}'}
# pos2 = list(d2.values())
# if len(s) < 2:
#     return False
# if s[0] in pos2:
#     return False
# for c in s:
#     if c in pos1:
#         stak.append(c)
#         length += 1
#     elif length > 0:
#         if d2[d1[stak[-1]]] == c:
#             stak.pop()
#             length -= 1
#         else:
#             return False
# if len(stak) == 0:
#     return True
# else:
#     return False

# from collections import deque
# ls = [1]
# target = 1
#
# j = len(ls) - 1
# i = 0
# if j > 1:
#     if target > ls[-1]:
#         print(j + 1)
#     elif target < ls[0]:
#         print(0)
#     while i < j:
#         m = (i + j) // 2
#         if ls[m] < target <= ls[m+1]:
#             print(m+1)
#             break
#         elif target < ls[m]:
#             j -= 1
#         elif target > ls[m]:
#             i += 1
#         elif ls[m] == target:
#             print(m)
#             break
# else:
#     if target <= ls[0]:
#         print(0)
#     elif target > ls[0]:
#         print(1)
#     elif j > 0 and ls[0] < target <= ls[1]:
#         print(1)
#     elif j > 0 and target > ls[1]:
#         print(2)


# while i < len(s):
#     if s[i] != ' ':
#         if s[i-1] == ' ':
#             sol.clear()
#             sol.append(s[i])
#         else:
#             sol.append(s[i])
#     i += 1
# return len(sol)
import collections
sol = collections.deque([])
a = "1010"
b = "1011"
#   10101
lena = len(a)
lenb = len(b)
i = -1
c = 0
while i >= min(lena, lenb):
    if a[i] == b[i] == '1':
        sol.appendleft('0')
        c = 1
    else:
        if a[i] == b[i] == '0':
            if c == 1:
                sol.appendleft('1')
                c = 0
            else:
                sol.appendleft('0')
        else:
            if c == 1:
                sol.appendleft('0')
            else:
                sol.appendleft('1')
    i -= 1
while i <= -lena:
    if c == 0:
        sol.appendleft(f"{a[i]}")
    else:
        if a[i] == 1:
            sol.appendleft('0')
        else:
            sol.appendleft('1')
            c = 0
    i -= 1
while i <= -lenb:
    if c == 0:
        sol.appendleft(f"{b[i]}")
    else:
        if b[i] == 1:
            sol.appendleft('0')
        else:
            sol.appendleft('1')
            c = 0
    i -= 1
print(sol)
