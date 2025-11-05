# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

from typing import List

# This is again two pointer problem, but can we solve it in O(n)? Do we consider O(n^2)
# below is n + n-1 + n-2 + ... + 1 = n(n-1)/2 = O(n^2)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max_area = 0
        # j = len(height) - 1
        # for first in range(len(height)):
        #     #Comapre start with the next loop
        #     for second in range(first+1,len(height)):
        #         area = (second-first)* min(height[first],height[second])
        #         if area > max_area:
        #             max_area = area

        # return max_area
        max_area = 0
        left = 0 
        right = len(height)-1

        #try to move inward,
        while left != right:
            area = (right-left)* min(height[left],height[right])
            if area>max_area:
                max_area=area
            if height[left] < height[right]:
                left +=1
            else:
                right-=1
        return max_area
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
    print(sol.maxArea([1,1]))