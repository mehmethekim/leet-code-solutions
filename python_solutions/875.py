# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
 
from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Look at the piles from the middle by going left and right.
        # We are to find the min number that satisfies th condition.
        #Divide the number by h to find the the min number and number of piles.
        # IF we are to the O(n^2), we should divide each number with the number we find
        # Iterate every number
        
        for pile in piles:
            hour = 0
            for num in piles:
                hour+= math.ceil(num/pile)
            print(hour) 
if __name__ == "__main__":
    sol = Solution()
    print(sol.minEatingSpeed([3,6,7,11], 8)) # 4
    # print(sol.minEatingSpeed([30,11,23,4,20], 5)) # 30
    # print(sol.minEatingSpeed([30,11,23,4,20], 6)) # 23