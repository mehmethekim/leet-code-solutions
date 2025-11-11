# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength 
# of the jth potion.

# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

 

# Example 1:

# Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# Output: [4,0,3]
# Explanation:
# - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
# - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
# - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
# Thus, [4,0,3] is returned.
# Example 2:

# Input: spells = [3,1,2], potions = [8,5,8], success = 16
# Output: [2,0,2]
# Explanation:
# - 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
# - 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
# - 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
# Thus, [2,0,2] is returned.
from typing import List
from math import ceil
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Typical soln is to make O(n^2)
        # result = [0] * len(spells)
        # for idx,spell in enumerate(spells):
        #     for potion in potions:
        #         if spell*potion >= success:
        #             result[idx] +=1
        # return result

        # For faster approach sort the potions list and find the minimum potion threshold
        sorted_potions = sorted(potions)
        length = len(sorted_potions)
        for spell in spells:
            threshold = ceil(success/spell) #>= is ok.
            idx = self.binarySearch(sorted_potions,threshold)
            print(idx)
            
    def binarySearch(self,arr, targetVal):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == targetVal:
                return mid

            if arr[mid] < targetVal:
                left = mid + 1
            else:
                right = mid - 1
        return -1    
if __name__ == "__main__":
    sol = Solution()
    print(sol.successfulPairs([5,1,3], [1,2,3,4,5], 7)) # [4,0,3]
    print(sol.successfulPairs([3,1,2], [8,5,8], 16)) # [2,0,2]