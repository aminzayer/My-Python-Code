# Search in Rotated Sorted Array II
# There is an integer array nums sorted in non-decreasing order(not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k(0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]](0-indexed). For example, [0, 1, 2, 4, 4, 4, 5, 6, 6, 7] might be rotated at pivot index 5 and become[4, 5, 6, 6, 7, 0, 1, 2, 4, 4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.


# Example 1:

# Input: nums = [2, 5, 6, 0, 0, 1, 2], target = 0
# Output: true

# Example 2:

# Input: nums = [2, 5, 6, 0, 0, 1, 2], target = 3
# Output: false

# Solution 1
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            if nums[0] == target:
                return True
            else:
                return False
        bigest_error = target - nums[0]
        if bigest_error > 0:
            dir_flag = 1
        else:
            dir_flag = 0

        for i in range(0, len(nums)):
            error = target - nums[i]
            if error > bigest_error and dir_flag:
                return False
            if error == 0:
                return True
        return False

# Solution 2