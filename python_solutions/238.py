# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

#  Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

from typing import List
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        multiplication = 1
        zero_count = 0
        for number in nums:
            if number != 0:
                multiplication *= number
            else:
                zero_count += 1

        # Case 1: More than one zero → all products are zero
        if zero_count > 1:
            return [0] * len(nums)

        # Case 2: Exactly one zero → only that index gets multiplication, others 0
        if zero_count == 1:
            return [0 if number != 0 else multiplication for number in nums]

        # Case 3: No zeros → normal integer division
        return [multiplication // number for number in nums]

        
if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))# [24,12,8,6]
    print(sol.productExceptSelf([-1,1,0,-3,3]))# [0,0,9,0,0]