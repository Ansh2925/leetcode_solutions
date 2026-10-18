class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        result = set()

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):

                    if i == j or j == k or i == k:
                        continue

                    if digits[i] == 0:
                        continue

                    if digits[k] %2 != 0:
                        continue

                    digit = 100*digits[i] + 10*digits[j] + digits[k]
                    result.add(digit)
        return len(result)