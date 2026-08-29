class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        my_stack1 = []
        my_stack2 = []

        for ch in s:
            if ch != '#':
                my_stack1.append(ch)
            else:
                if my_stack1:
                    my_stack1.pop()

        for ch in t:
            if ch != '#':
                my_stack2.append(ch)
            else:
                if my_stack2:
                    my_stack2.pop()

        return my_stack1 == my_stack2