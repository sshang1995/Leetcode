class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening = closing = 0
        for i, v in enumerate(s):
            if v == '(':
                closing += 1
            elif v == ')':
                if closing > 0:
                    closing -= 1
                else:
                    opening += 1
        return opening + closing