# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:

# Input: nums = []
# Output: []

# Example 3:

# Input: nums = [0]
# Output: []

class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []

        out = set()
        nums = sorted(nums)
        i = 0
        while i < len(nums) - 2:
            while i < len(nums) - 2 and nums[i] == nums[i + 1] and nums[i + 1] == nums[i + 2]:
                if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 0:
                    out.add((0, 0, 0))
                i += 1
            out.update(self.twoSum(nums, i + 1, nums[i]))
            i += 1
        return [list(i) for i in out]

    def twoSum(self, nums, ind, v):
        out = set()
        l, r = ind, len(nums) - 1

        while l < r:
            if v + nums[l] + nums[r] == 0:
                out.add((v, nums[l], nums[r]))
                l += 1
                r -= 1
            elif v + nums[l] + nums[r] < 0:
                l += 1
            else:
                r -= 1

        return out
