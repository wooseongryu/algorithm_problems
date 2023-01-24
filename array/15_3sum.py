# def three_sum(nums: list[int]) -> list[list[int]]:
#     nums_list = []
#     nums.sort()
#
#     for i in range(len(nums) - 2):
#         for j in range(i + 1, len(nums) - 1):
#             for k in range(j + 1, len(nums)):
#                 if nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in nums_list:
#                     nums_list.append([nums[i], nums[j], nums[k]])
#
#     return nums_list


# def three_sum(nums: list[int]) -> list[list[int]]:
#     nums_list = []
#     nums.sort()
#
#     for i in range(len(nums) - 2):
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#         for j in range(i + 1, len(nums) - 1):
#             if j > i + 1 and nums[j] == nums[j - 1]:
#                 continue
#             for k in range(j + 1, len(nums)):
#                 if k > j + 1 and nums[k] == nums[k - 1]:
#                     continue
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     nums_list.append([nums[i], nums[j], nums[k]])
#
#     return nums_list


def three_sum(nums: list[int]) -> list[list[int]]:
    result_list = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result_list.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result_list


nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))
