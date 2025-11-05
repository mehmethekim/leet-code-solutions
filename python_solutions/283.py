# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Do it like bubble sort, Instead of comparing them shift them if they are 0.
        # There will be two pointers, assign first and second.
        # Move second until  non zero is found, move first until zero is found.
        #first points to zero, second is non-zero. Swap the values. of nums
        # When second is at the end of list, we should be finished.
        last_non_zero_found_at = 0
        #Instead of moving zeros away, move numbers to the beginning.
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i], nums[last_non_zero_found_at] = nums[last_non_zero_found_at], nums[i]
                last_non_zero_found_at += 1
                #Swap it with last non zero
        
if __name__ == "__main__":
    sol = Solution()
    nums=[0,1,0,3,12]
    sol.moveZeroes(nums)
    print(nums)# [1,3,12,0,0]
    nums=[1,0]
    sol.moveZeroes(nums)
    print(nums)# [1,3,12,0,0]          