class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        result = 0
        while n > 0:
            d = n % 10
            result += d      
            n = n // 10

        return result