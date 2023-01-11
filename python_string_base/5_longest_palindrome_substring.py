def longest_palindrome(s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(0, len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
    return result


s = "babad"
print(longest_palindrome(s))
