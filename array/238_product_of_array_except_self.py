# def product_except_self(nums: list[int]) -> list[int]:
#     answer = []
#     mul = 1
#     for i in nums:
#         mul *= i
#
#     for i in nums:
#         answer.append(mul // i)
#
#     return answer


def product_except_self(nums: list[int]) -> list[int]:
    tmp = []
    p = 1
    for i in range(len(nums)):
        tmp.append(p)
        p *= nums[i]

    p = 1
    for i in range(len(nums) - 1, -1, -1):
        tmp[i] *= p
        p *= nums[i]

    return tmp


nums = [1, 2, 3, 4]
print(product_except_self(nums))
