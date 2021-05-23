class Solution:
    def removeInvalidParentheses(self, s):
        def isvalid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False
            return ctr == 0
        
        level = {s}
        while True:
            valid = []
            for elem in level:
                if isvalid(elem):
                    valid.append(elem)
            if valid:
                return valid
            # initialize an empty set
            new_level = set()
            # BFS
            for elem in level:
                for i in range(len(elem)):
                    new_level.add(elem[:i] + elem[i + 1:])
            level = new_level