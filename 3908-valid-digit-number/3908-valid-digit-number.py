class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        dig = []

        while n > 0:
            d = n % 10
            dig.append(d)
            n = n // 10

        dig.reverse()
        if len(dig) == 0:
            return False
            
        if dig[0] == x:
            return False
        
        for i in range(len(dig)):
            if dig[i] == x:
                return True


        return False