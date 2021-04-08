# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def array_to_tree(left, right):
            nonlocal preorder_index
            # if there is no element to construct tree
            if left > right:return None
            
            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)
            
            preorder_index += 1
            
            root.left = array_to_tree(left, inorder_index_map[root_value] -1)
            root.right = array_to_tree(inorder_index_map[root_value] +1, right)
            return root
        
        preorder_index = 0
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index
        return array_to_tree(0, len(preorder) -1)


# LC106 Construct Binary Tree from Inorder and Postorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        def array_to_tree(left, right):
            
            if left > right: return None
            
            val = postorder.pop()
            root = TreeNode(val)
            
            postorder_index = inorder_index_map[val]
            root.right = array_to_tree(postorder_index +1, right)
            root.left = array_to_tree(left, postorder_index -1)
            return root
        
        
 
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index
        
        return array_to_tree(0, len(postorder) -1)
