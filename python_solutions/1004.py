# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # we should keep a sliding window that contains the k number of  zeros inside and keep track of the first zero that comes in the window
        # We should have two pointers left and right that represent the window
        # When a one comes, we extend the window. If a zero comes, we count the number of zeros in the window, If less than k, we extend the window
        # If more than k, we move the left pointer to the right until we remove one zero from the window. Then we return the maximum window size we have seen
        right=0
        left=0
        zero_count=0
        max_length=0
        n=len(nums)
        while right<n:
            if nums[right]==0:
                zero_count+=1
            while zero_count>k:
                if nums[left]==0:
                    zero_count-=1
                left+=1
            max_length=max(max_length,right-left+1)
            right+=1
        return max_length

if __name__ == "__main__":
    sol = Solution()
    k = 3
    print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2)) #6
    print(sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3)) #10