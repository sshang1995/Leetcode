class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        o =[]
        c = set()

        for i,v in enumerate(s):
            if v not in '()':
                continue
            if v == '(':
                o.append(i)
            elif not o:# ')' appear before '('
                c.add(i)
            else: # v ==')'
                o.pop()
        c = c.union(set(o))
        strs =''
        for i, v in enumerate(s):
            if i not in c:
                strs += v
        return strs
                
# TC:O(N)
# SC:O(N) o and c