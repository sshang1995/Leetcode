# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return float('inf'), float('-inf'), 0
            l_min, l_max, l_n = dfs(root.left)
            r_min, r_max, r_n = dfs(root.right)
            n = float('-inf')
            if l_max < root.val < r_min:
                n = l_n + r_n + 1
                self.res = max(self.res, n)
            return min(l_min, root.val), max(r_max, root.val), n
        dfs(root)
        return self.res
# TC: O(N) N is number of node
# SC: O(N)