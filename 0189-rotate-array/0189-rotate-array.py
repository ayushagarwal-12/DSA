class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)

        for i in range(k):
            last = nums.pop()
            nums.insert(0, last)