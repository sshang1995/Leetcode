class Node:
    def __init__(self, val):
        self.val = val;
        self.left = self.right = None
        
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        self.res = 0
        root = Node(nums[0] % 10)
        # create tree
        for num in nums[1:]:
            depth, pos, val = num//100, num//10 %10, num % 10
            cur = root
            pos -= 1
            for d in range(depth-2, -1, -1):
                if pos < 2**d:
                    cur.left = cur = cur.left or Node(val)
                else:
                    cur.right = cur =cur.right or Node(val)
                pos %= 2**d
        # preorder traverse tree
        def dfs(node, runningSum = 0):
            if not node:
                return 
            runningSum += node.val
            if not node.left and not node.right:
                self.res += runningSum
            else:
                dfs(node.left, runningSum)
                dfs(node.right, runningSum)
        dfs(root)
        return self.res
# TC: O(N)
# SC: O(N)

# Dictionary
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        self.res = 0
        values = {x // 10: x % 10 for x in nums}
        def dfs(key, runningSum = 0):
            if key not in values:
                return
            runningSum += values[key]
            depth, pos = key // 10, key % 10
            left_key = (depth+1)*10 + 2*pos -1
            right_key = (depth+1)*10 + 2*pos
            if left_key not in values and right_key not in values:
                self.res += runningSum
            else:
                dfs(left_key, runningSum)
                dfs(right_key, runningSum)
        
        dfs(nums[0]//10)
        return self.res