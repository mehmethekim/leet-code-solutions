
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 


class Solution:
    def reverseVowels(self, s: str) -> str:
        # we can have two pointers on the s.
        # One starts from the start, other one from the back.
        # Go to forward for first pointer until found any vowel
        # Go backward for the second pointer if found for the first pointer until vowel
        # If both found without touching switch places.
        # Then continue until they both meet.

        forward_pointer = 0
        backward_pointer = len(s)-1
        vowels = set('aeiouAEIOU')
        s_list = list(s)
        while forward_pointer < backward_pointer:

            if s_list[forward_pointer] in vowels and s_list[backward_pointer] in vowels:
                #swap
                s_list[forward_pointer], s_list[backward_pointer] = s_list[backward_pointer], s_list[forward_pointer]
                backward_pointer-=1
                forward_pointer+=1
            elif s_list[forward_pointer] in vowels and s_list[backward_pointer] not in vowels:
                #backward decrement
                backward_pointer-=1
            elif s_list[forward_pointer] not in vowels and s_list[backward_pointer]  in vowels:
                #forward increment
                forward_pointer+=1
            else:
                backward_pointer-=1
                forward_pointer+=1
                #both change
        return ''.join(s_list)

if __name__ == "__main__":
    sol = Solution()
    str1 = "ABCABC"
    str2 = "ABC"
    #print(sol.gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
    print(sol.reverseVowels("IceCreAm"))
    # print(sol.divides("ABCABC", "ABC"))
    # print(sol.divides("ABABAB", "AB"))