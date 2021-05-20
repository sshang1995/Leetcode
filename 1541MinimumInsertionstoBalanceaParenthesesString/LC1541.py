class Solution:
    def minInsertions(self, s: str) -> int:
        add = closing = 0
        for i,v in enumerate(s):
            if v == '(': 
                closing += 2
                if closing % 2:# odd, need to add one ')'
                    closing -=1
                    add += 1
            elif v == ')':
                closing -= 1
                if closing < 0: # add '('
                    closing += 2
                    add += 1
        return add + closing
                    
# 921Minimum Add to Make Parentheses Valid (similar)
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