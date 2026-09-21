class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                return num
            else:
                freq[num] = 1


