class Solution:
    def validStrings(self, n: int) -> List[str]:
        numbers = ['0']*n
        result = []

        def backtrack(idx, flag, numbers):

            if idx >= len(numbers):
                result.append("".join(numbers))
                return

            numbers[idx] = "1"
            backtrack(idx +1, True, numbers)

            if flag == True:
                numbers[idx] = "0"
                backtrack(idx +1, False, numbers)
                numbers[idx] = "1"

        backtrack(0, True, numbers)
        return result