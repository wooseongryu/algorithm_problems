import re


# def is_palindrome(s: str) -> bool:
#     s = s.lower()
#     s = re.sub('[^a-z0-9]', '', s)
#     return s == s[::-1]

from collections import deque


def is_palindrome(s: str) -> bool:
    alnum = deque()

    for char in s:
        if char.isalnum():
            alnum.append(char.lower())

    while len(alnum) > 1:
        if alnum.popleft() != alnum.pop():
            return False

    return True


s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))
