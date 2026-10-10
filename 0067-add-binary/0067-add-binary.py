class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def convertDec(x: str) -> int:
            dec = 0
            power = 0
            idx = len(x)-1

            while idx >= 0:
                num = int(x[idx])*(2**power)
                dec += num
                idx -=1
                power +=1

            return dec

        # a = convertDec(a)
        # b = convertDec(b)

        return bin(convertDec(a)+ convertDec(b))[2:]