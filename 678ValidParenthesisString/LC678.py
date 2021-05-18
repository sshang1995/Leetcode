class Solution:
    def checkValidString(self, s: str) -> bool:
        #greedy
        # minimum number of open parenthesis
        # max number of open parenthesis
        # op_min cannot be lower than 0, because if it's below 0, that means ')' appeared before '('
        op_min = op_max = 0
        for i in s:
            if i == '(':
                op_min += 1
                op_max += 1
            elif i == ')':
                op_min = max(op_min -1, 0)
                op_max -= 1
            else:
                op_min = max(op_min -1, 0)
                op_max += 1
            if op_max < 0: #not every ')' has '(' to match
                return False
        # if op_min > 0 that means not every '(' has ')' to match
        return op_min == 0
                