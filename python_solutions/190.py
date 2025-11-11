# Reverse bits of a given 32 bits signed integer.

# Example 1:

# Input: n = 43261596

# Output: 964176192
class Solution:
    def reverseBits(self, n: int) -> int:
        old_number = bin(n)
        #Fill the number to 32 bits
        old_number = old_number[2:].zfill(32)
        new_number = '0b'

        for bit in old_number[::-1]:
            new_number += bit

        return int(new_number, 2)

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseBits(43261596)) # 964176192