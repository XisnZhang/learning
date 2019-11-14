"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        results = []
        length = len(nums)
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = length - 1
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                if _sum < 0:
                    j += 1
                elif _sum > 0:
                    k -= 1
                else:
                    results.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                    while j < k and nums[k + 1] == nums[k]:
                        k -= 1
        return results


class Solution2:
    def threeSum(self, nums):
        results = {}
        length = len(nums)
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = length - 1
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                if _sum < 0:
                    j += 1
                elif _sum > 0:
                    k -= 1
                else:
                    key = "|".join([str(nums[i]), str(nums[j]), str(nums[k])])
                    results[key] = [nums[i],nums[j],nums[k]]
                    j += 1
                    k -= 1
        return list(results.values())


if __name__ == '__main__':
    # a = [-1, 0, 1, 2, -1, -4]
    # a = [0, 0, 0]
    a = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    # a = [-1, 0, 1, 2, -1, -4]
    # a = [-2, 0, 0, 2, 2]
    print(Solution2().threeSum(a))
