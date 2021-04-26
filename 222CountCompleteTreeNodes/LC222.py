# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # count node recursively one by one
        return 1+ self.countNodes(root.left) + self.countNodes(root.right) if root else 0
        
# TC: O(N), n is number of treeNode
# SC: O(d) = O(logN) d is a tree depth       

#Binary Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compute_depth(self, root):
        d = 0
        while root.left:
            root = root.left
            d += 1
        return d
    def exists(self,index, d, node):
        left, right = 0, 2**d -1
        for _ in range(d):
            pivot = left +(right - left) //2
            if index <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot +1
        # return true is node exist
        return node is not None
    
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        d = self.compute_depth(root)
        if d == 0:
            return 1
        
        left, right = 1, 2**d -1
        while left <= right:
            pivot = left + (right - left) //2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot -1
        return (2**d - 1) + left
    
#TC: O(d^2) d is tree depth
#SC: O(1)