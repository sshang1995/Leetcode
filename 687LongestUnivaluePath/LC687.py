# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return 0 
            left = dfs(root.left)
            right = dfs(root.right)
            left_length = right_length = 0
            if root.left and root.left.val == root.val:
                left_length = left +1 
            if root.right and root.right.val == root.val:
                right_length = right +1
            self.res = max(self.res, right_length + left_length)
            return max(left_length, right_length)
        
        dfs(root)
        return self.res
# bottom-up, from leaf node to find the longest path
# at the end of each recursive loop, return the longest length 
# using that node as the root so that the node's parent can potentially use it 
#in its longest path computation.
#Time Complexity: O(N), where N is the number of nodes in the tree. We process every node once.

#Space Complexity: O(H), where H is the height of the tree. Our recursive call stack could be up to HH layers deep.