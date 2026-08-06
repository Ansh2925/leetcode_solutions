class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        for i in range(n, 101):
            s = str(i)
            product = 1
            for ch in s:
                product *= int(ch)

            if product%t == 0:
                return i
            # return product