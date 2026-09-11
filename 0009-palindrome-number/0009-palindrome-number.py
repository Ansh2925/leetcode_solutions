class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        revNum = 0

        while num > 0:
            lastDigit = num % 10
            revNum *= 10
            revNum += lastDigit
            num = num // 10
        return revNum == x

        