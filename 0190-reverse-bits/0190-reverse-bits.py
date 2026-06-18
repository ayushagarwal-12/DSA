class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            result = result << 1      # Make space for next bit
            result += n & 1           # Take last bit of n
            n = n >> 1                # Remove last bit from n

        return result