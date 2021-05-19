class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [eval(expression)]
        res = []
        for i,s in enumerate(expression):
            if s in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if s == '+':
                            res.append(l+r)
                        elif s == '-':
                            res.append(l-r)
                        else:# s= '*'
                            res.append(l*r)
                            
        return res

# with memozation
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
       
        
        def dfs(expression,memo):
            res = []
            if expression in memo:
                return memo[expression]
            if expression.isdigit():
                return [eval(expression)]

            for i,s in enumerate(expression):
                if s in "+-*":
                    left = dfs(expression[:i],memo)
                    right = dfs(expression[i+1:],memo)
                    res.extend(eval(str(l)+s+str(r))for l in left for r in right)

                    memo[expression] = res              
            return res
        
        memo = {}
        return dfs(expression,memo)