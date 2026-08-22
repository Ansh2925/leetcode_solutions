class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = str(n)

        plus = 0
        product = 1
        for ch in s:
            plus += int(ch)
            product *= int(ch)

        if n % (plus+product) == 0:
            return True

        return False