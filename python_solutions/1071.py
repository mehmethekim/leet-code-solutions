# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.
import math 
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 1. Select the smaller string.
        # 2. Look at the slices of smaller string one by one and see if it divides other one.
        # If yes for that, try bigger slice
        # For ABC, try A, if satisfies try AB, if yes try ABC.
        # If we reach the smaller string length, we can terminate prematurely.
        # For CODE, try C, not satisfy, then O,then D, then E, then terminate
        # For ABAB, try A, then AB, note that, then try ABA no, then try B, BA,
        divisor = str2 if len(str1) >= len(str2) else str1
        divident = str1 if len(str1) >= len(str2) else str2
        divisor_len = len(divisor)
        max_divisor_len = 0
        max_divisor = ""
        for slice_len in range(1,divisor_len+1):
            for i in range(math.ceil(divisor_len/(slice_len))):
                slice = divisor[i:i+slice_len]
                if self.divides(divident,slice) and self.divides(divisor,slice):
                    print(slice," divides ",divident)
                    if len(slice)>max_divisor_len:
                        max_divisor_len = len(slice)
                        max_divisor = slice
                    
        return max_divisor
    def divides(self,string:str,divisor:str) -> bool:
        #1. look at the length of divisor.
        #2. In a for loop look at the slices of string, if it equals to divisor. If yes for all it divides.
        div_len = len(divisor)
        for i in range(math.ceil(len(string)/div_len)):
            slice = string[i*div_len:i*div_len+div_len]
            if slice != divisor:
                return False
        return True
        
if __name__ == "__main__":
    sol = Solution()
    str1 = "ABCABC"
    str2 = "ABC"
    #print(sol.gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
    print(sol.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))  # Output: "TAUXX"
    # print(sol.divides("ABCABC", "ABC"))
    # print(sol.divides("ABABAB", "AB"))