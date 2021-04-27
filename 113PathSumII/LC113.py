# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(root, remainSum, pathNode, pathList):
            if not root:
                return 
            pathNode.append(root.val)
            
            if remainSum == root.val and not root.left and not root.right:
                pathList.append(list(pathNode))

            else:
                dfs(root.left, remainSum-root.val, pathNode, pathList)
                dfs(root.right, remainSum-root.val, pathNode, pathList)
            # if reach leaf node and need to got to upper level
            pathNode.pop()
        pathList = []
        dfs(root, targetSum, [], pathList)
        return pathList