class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = right = 0
        for i in s:
            if i == '(':
                left += 1
            elif i == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        result = []
        def recurse(s, index, left_count, right_count, left_rem, right_rem, expre):
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    ans = "".join(expre)
                    result.append(ans)
            else:
                    if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                        recurse(s, index + 1, left_count, right_count, left_rem-(s[index]=='('), right_rem - (s[index]==')'), expre)
                        
                    expre.append(s[index])
                    
                    if s[index] != '(' and s[index] != ')':
                        recurse(s,index+1, left_count, right_count, left_rem, right_rem, expre)
                    elif s[index] == '(':
                        recurse(s, index+1, left_count+1, right_count, left_rem, right_rem, expre)
                    elif s[index] ==')' and left_count > right_count:
                        recurse(s, index+1, left_count, right_count+1, left_rem, right_rem, expre)
                    
                    expre.pop()
                    
        recurse(s, 0, 0, 0, left, right, [])
        #print(result)
        return set(result)
# Recursive 
# TC : O(2^N)
# SC: O(N)

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

