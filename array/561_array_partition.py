def array_pair_sum(nums: list[int]) -> int:
    nums.sort()
    total = sum(nums[::2])

    return total


# def array_pair_sum(nums: list[int]) -> int:
#     nums.sort()
#     total = 0
#
#     for i, n in enumerate(nums):
#         if i % 2 == 0:
#             total += n
#
#     return total


nums = [1, 4, 3, 2]
print(array_pair_sum(nums))
