# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
from typing import List
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # With sliding window approach, look at the substrings, or with slicing,
        # Then count the vowels inside and keep max count.We can also use two pointers
        # But first one to first element, secnd in the k-1 element. Then one by one iterate it. We can count the vowels for the first string once and then
        # Increment or decrement it based on first and last vowels

        

        first = 0
        second = k-1
        vowels = set("aeiou")
        length = len(s)
        count = 0
        for char in s[first:second+1]:
            if char in vowels:
                count+=1
        max_count = count
        first_is_vowel = s[first] in vowels
        second +=1
        first+=1
        while second < length:
            
            if s[second] in vowels:
                
                count+=1
            if first_is_vowel:
                count-=1
            first_is_vowel = s[first] in vowels
            if count> max_count:
                max_count = count
            second +=1
            first+=1
            

        return max_count
        # Extract first one

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxVowels("abciiidef",3))
    print(sol.maxVowels("aeiou",2))
    print(sol.maxVowels("leetcode",3))
