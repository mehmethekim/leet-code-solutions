# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: One of the valid triplet is (3, 4, 5), because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.




# Faster soln iterate the list once. Find the smallest by iterating,
#Then find the 
from typing import List
class Solution:
    # def increasingTriplet(self, nums: List[int]) -> bool:
    #     # If found early exit.
    #     #O(1) space and O(n)time
    #     # Hold 3 integers, first, second, third
    #     if len(nums) < 3:
    #         return False
    #     i,j,k = 0,1,2
    #     # Look at nums[i],nums[j],nums[k] if they are valid return True
    #     # If not valid increment k until the end of the list.
    #     # If not found return k to j+1, increment j by one, then increment k
    #     # If not found increment i by 1, increment k and go on.
    #     # we will do this until i is at len(nums) -3
    #     for i in range(0,len(nums)-2):
    #         for j in range(i+1,len(nums)-1):
    #             for k in range(j+1,len(nums)):
    #                 if nums[i] < nums[j] < nums[k]:
                        
    #                     return True
    #     return False
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num<=first:
                first = num
            elif num<=second:
                second =num
            else:
                    #Found n such that first< second < n
                return True
        return False

        
if __name__ == "__main__":
    sol = Solution()
    print(sol.increasingTriplet([1,2,3,4,5]))# True
    print(sol.increasingTriplet([5,4,3,2,1]))# False
    print(sol.increasingTriplet([2,1,5,0,4,6]))# True