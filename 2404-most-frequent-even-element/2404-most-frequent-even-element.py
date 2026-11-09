import heapq
class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        
        freq = {}

        for num in nums:
            if num % 2 == 0:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1


        if freq:
            return max(freq, key=lambda x: (freq[x], -x))
        return -1
            