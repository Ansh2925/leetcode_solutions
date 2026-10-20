class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        # s = str(n)
        result = 0
        freq = {}

        while n > 0:
            d = n % 10
            if d in freq:
                freq[d] += 1
            else:
                freq[d] = 1      
            n = n // 10

        for key, val in freq.items():
            result += key * val

        return result