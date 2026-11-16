class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        if len(s) <= k:
            return s
        result = ""
        for i in range(0, len(s), k):
            groups = s[i: i+k]

            total = 0
            for group in groups:
                total += int(group)

            result += str(total)

        return self.digitSum(result, k)