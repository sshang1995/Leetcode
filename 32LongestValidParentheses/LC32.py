class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLength = 0
        stack = [-1]        # ')('
        for i, v in enumerate(s):
            if v == '(':
                stack.append(i)
            else:
                stack.pop()
                if (len(stack) == 0):
                    stack.append(i)
                else:
                    maxLength = max(maxLength, i-stack[-1])
        return maxLength
# using stack to keep track of index.