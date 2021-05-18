class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for i in s:
            if i == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2*v, 1)
        return stack.pop()
               
class Solution:
	def scoreOfParentheses(self, s: str) -> int:
	    ans = bal = 0
	    
	    for i, x in enumerate(s):
	        if x == '(':
	            bal += 1
	        else:
	            bal -= 1
	            if s[i-1] == '(':
	                ans += 1 * 2**bal
	                # ans += 1 << bal
	    return ans
	               