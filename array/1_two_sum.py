# def two_sum(nums: list[int], target: int) -> list[int]:
#     for i in range(len(nums) - 1):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]


# def two_sum(nums: list[int], target: int) -> list[int]:
#     for i, number in enumerate(nums):
#         tmp = target - number
#         if tmp in nums[i + 1:]:
#             return [i, nums[i + 1:].index(tmp) + (i + 1)]


def two_sum(nums: list[int], target: int) -> list[int]:
    numbers_dict = {}
    for i, number in enumerate(nums):
        numbers_dict[number] = i

    for i, number in enumerate(nums):
        if target - number in numbers_dict and i != numbers_dict[target - number]:
            return [i, numbers_dict[target - number]]


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
