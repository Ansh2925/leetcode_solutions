class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        a = n - 999
        if a > 0:
            res += a
            a = n - 999999
            if a > 0:
                res += a
                a = n - 999999999
                if a > 0:
                    res += a
                    a = n - 999999999999
                    if a > 0:
                        res += a
                        a = n - 999999999999999
                        if a > 0:
                            res += a

        return res