from string import printable
from typing import List
from random import randint, choices

"""Make a function that cna take any non-negative integer as an argument and return it with its digits in descending 
order. Essentially, rearrange the digits to create the highest possible number.
"""


def highestNumber(num: int) -> int:
    print(f"Given number: {num}")
    freqList: List[int] = [0 for _ in range(10)]  # digit frequency list

    # count the number of digits into freqList
    while num:
        freqList[num % 10] += 1
        num //= 10

    # create a new number starting from the highest digit
    for i in range(9, -1, -1):
        while freqList[i]:
            num = num * 10 + i
            freqList[i] -= 1

    return num


for _ in range(5):
    print(highestNumber(randint(10, 10 ** 7)))

# Time complexity: O(n), n = number of digits


"""
Write a function that is given a string, replace every letter with its position in the alphabet. If anything in the text
isn't a letter, ignore it and don't return it. a being 1, b being 2 etc.
"""


def alphabetPosition(words: str) -> str:
    print(f"Given string: {words}")
    positions: str = ""
    for letter in words:
        if ord('a') <= ord(letter) <= ord('z'):  # ord returns the ascii code
            positions += f"{ord(letter) - ord('a') + 1} "
        elif ord('A') <= ord(letter) <= ord('Z'):
            positions += f"{ord(letter) - ord('A') + 1} "

    return positions


for _ in range(5):
    # generate random strings with lower case, upper case, digits, whitespaces and punctuation, with random length
    # between 5 and 15
    print(alphabetPosition(''.join(choices(printable, k=randint(5, 15)))))

# Time complexity: O(n), n = given string length
