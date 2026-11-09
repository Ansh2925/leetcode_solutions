import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        min_heap = []

        for num, count in freq.items():

            heapq.heappush(min_heap, (count, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        result = []

        for count, num in min_heap:
            result.append(num)

        return result