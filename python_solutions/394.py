# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ']':
                # Pop substring inside brackets
                sub_str = ''
                while stack and stack[-1] != '[':
                    sub_str = stack.pop() + sub_str
                stack.pop()  # remove '['
                
                # Get the number
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                # Repeat substring and push back
                stack.append(sub_str * int(num))
            else:
                stack.append(char)
        
        # Join everything left in stack
        return ''.join(stack)

if __name__ == "__main__":
    sol = Solution()
    print(sol.decodeString("3[a]2[bc]")) # "aaabcbc"
    print(sol.decodeString("3[a2[c]]")) # "accaccacc"
    print(sol.decodeString("2[abc]3[cd]ef")) # "abcabccdcdcdef"
    print(sol.decodeString("100[leetcode]"))
    print(sol.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")) # "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
    