"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""

import sys


class Solution:
    def threeSumClosest(self, nums, target):

        if len(nums) <= 3:
            return sum(nums)

        nums = sorted(nums)
        length = len(nums)
        result = nums[0] + nums[1] + nums[2]
        min_diff = abs(result - target)
        for i, a in enumerate(nums):
            j = i + 1
            k = length - 1
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum == target:
                    return current_sum
                diff = abs(current_sum - target)
                if diff < min_diff:
                    result = current_sum
                    min_diff = diff
                if current_sum < target:
                    j += 1
                else:
                    k -= 1
        return result


if __name__ == '__main__':
    a = [-1, 2, 1, -4]
    print(Solution().threeSumClosest(a, 1))
