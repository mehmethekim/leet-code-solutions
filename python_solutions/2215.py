# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

# Example 1:

# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].
# Example 2:

# Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# Output: [[3],[]]
# Explanation:
# For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
# Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        #There will be dictionaries for both lists
        set1 = set()
        set2 = set()

        for number in nums1:
            set1.add(number)
        for number in nums2:
            set2.add(number)
        
        # If a number in set1 is not in set2 add it to output list 1

        # Do the same for set 2
        result1 = []
        result2=[]
        for item1 in set1:
            if item1 not in set2:
                result1.append(item1)
        for item2 in set2:
            if item2 not in set1:
                result2.append(item2)
        return [result1,result2]
if __name__ == "__main__":
    sol = Solution()
    print(sol.findDifference([1,2,3], [2,4,6])) # [[1,3],[4,6]]
    print(sol.findDifference([1,2,3,3], [1,1,2,2])) # [[3],[]] 