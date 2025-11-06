# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.
# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# Example 3:

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
from typing import List
import bisect
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        ends = [end for _, end in intervals]

        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            start_i, end_i = intervals[i]

            # find rightmost j with end_j <= start_i
            j = bisect.bisect_right(ends, start_i) - 1

            include = 1 + (dp[j] if j >= 0 else 0)
            exclude = dp[i-1]

            dp[i] = max(include, exclude)

        keep_max = dp[-1]
        return n - keep_max
if __name__ == "__main__":
    sol = Solution()
    print(sol.eraseOverlapIntervals([[1,10], [3,4], [4,5],[2,3], [5,9],  [9,10],[6,7] ,[7,8]]))