class Solution:
    def smallestNumber(self, n: int) -> int:
        def convertBin(n: int) -> str:
            res = ""
            while n > 0:
                if n % 2 == 1:
                    res += "1"
                else:
                    res += "0"
                n = n //2
            res = res[::-1]
            return res

        bin = convertBin(n)
        power = len(bin)

        return (2**power) -1