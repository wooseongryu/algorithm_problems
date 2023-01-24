# def trap(height: list[int]) -> int:
#     volume = 0
#     for i in range(1, len(height) - 1):
#         left_max = max(height[:i])
#         right_max = max(height[i + 1:])
#         second_max = min(left_max, right_max)
#
#         if second_max > height[i]:
#             volume += second_max - height[i]
#
#     return volume

def trap(height: list[int]) -> int:
    volume = 0
    left_index, right_index = 0, len(height) - 1
    left_max, right_max = height[left_index], height[right_index]
    while left_index < right_index:
        left_max, right_max = max(left_max, height[left_index]), max(right_max, height[right_index])
        if left_max <= right_max:
            volume += left_max - height[left_index]
            left_index += 1
        else:
            volume += right_max - height[right_index]
            right_index -= 1
    return volume


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))
