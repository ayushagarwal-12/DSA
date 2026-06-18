class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        pos = 0

        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1

        # Fill remaining positions with 0
        while pos < len(nums):
            nums[pos] = 0
            pos += 1