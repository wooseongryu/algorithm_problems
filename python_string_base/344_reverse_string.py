# def reverse_string(s: list[str]) -> None:
#     s.reverse()


# def reverse_string(s: list[str]) -> None:
#     s[:] = s[::-1]


def reverse_string(s: list[str]) -> None:
    left, right = 0, len(s) - 1

    while s[left] < s[right]:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


s = ["h", "e", "l", "l", "o"]
reverse_string(s)
print(s)
