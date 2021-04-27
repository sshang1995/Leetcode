# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.count = 0
        def dfs(root, curr_sum):
            if not root:
                return
            curr_sum += root.val
            if curr_sum == targetSum:
                self.count += 1
            self.count += h[curr_sum - targetSum]
            
            h[curr_sum] += 1
            dfs(root.left, curr_sum)
            dfs(root.right, curr_sum)
            
            h[curr_sum] -= 1
        
        h = defaultdict(int)
        dfs(root, 0)
        return self.count 
        
# prefix sum
# TC: O(N)
# SC: O(N) hashmap keep thr prefix sum