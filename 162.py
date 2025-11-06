# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # Compare middle element with its right neighbor
            if nums[mid] < nums[mid + 1]:
                # Peak must be on the right half
                left = mid + 1
            else:
                # Peak is on the left half (could be mid itself)
                right = mid
        
        # When left == right, that index is a peak
        return left

if __name__ == "__main__":
    sol = Solution()
    print(sol.findPeakElement([1,2,3,1])) #2
    print(sol.findPeakElement([1,2,1,3,5,6,4])) #5 or 1