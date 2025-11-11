# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

#  Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:

# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:

# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        zeros = 0
        max_len = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                zeros += 1

            # If we have more than one zero, shrink from the left
            while zeros > 1:
                if nums[start] == 0:
                    zeros -= 1
                start += 1

            # window length minus one deletion
            max_len = max(max_len, end - start)

        return max_len
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestSubarray([1,1,0,1]))#3
    print(sol.longestSubarray([0,1,1,1,0,1,1,0,1]))#5
    print(sol.longestSubarray([1,1,1]))#2