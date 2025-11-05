# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #Iterate over t, look at the s and its first element. If found look at the second char.
        # If iteration is over or end of string s is reached return true
        if not s:
            return True
        count = 0
        for letter in t:
            if letter == s[count]:
                print("Found ",letter)
                count+=1
            if count==len(s):
                return True
        return False
if __name__ == "__main__":
    sol = Solution()
    print(sol.isSubsequence("abc","ahbgdc"))
    print(sol.isSubsequence("axc","ahbgdc"))