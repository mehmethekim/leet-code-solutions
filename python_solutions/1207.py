# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:

# Input: arr = [1,2]
# Output: false
# Example 3:

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
# Basic hash map, Count the numbers to a hash map

from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # 1. use a dict.
        hash_map = {}
        for number in arr:
            if number in hash_map:
                hash_map[number]+=1
            else:
                hash_map[number] = 1
        #Iterate over hashmap to see if they are unique
        #Map the hashmap values to a hashmap "wow"

        result = {}
        for key,value in hash_map.items():
            if value in result:
                return False
            else:
                result[value] = 1
        return True
if __name__ == "__main__":
    sol = Solution()
    print(sol.uniqueOccurrences([1,2,2,1,1,3]))