# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.

 

# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
#We should traverse the list once in O(n), for this purpose we should use two pointers
from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # We can access or delete at O(1) time in a dict.
        pairs = {}
        max_op = 0
        for num in nums:
            # Look at the dict if k-num exist on the dict
            # If not push it
            # If exists, increment and delete the pair
            if (k-num) in pairs:
                #delete the pair
                if pairs[k-num] == 1:
                    del pairs[k-num]
                else:
                    pairs[k-num]-=1
                max_op+=1
            else :
                if num<k:
                    if num in pairs:

                        pairs[num] += 1
                    else:
                        pairs[num] = 1
            # If not exist create it, if exists increment count.
        return max_op
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxOperations([1,2,3,4],k=5))
    print(sol.maxOperations([3,1,3,4,3],k=6))
    print(sol.maxOperations([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2],k=3))
    