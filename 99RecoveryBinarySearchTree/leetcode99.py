# Binary Search Tree is a node-based binary tree data structure which has the following properties:

# 1. The left subtree of a node contains only nodes with keys lesser than the node’s key.
# 2. The right subtree of a node contains only nodes with keys greater than the node’s key.
# 3. The left and right subtree each must also be a binary search tree.


# Depth First Traversals:
# (a) Inorder (Left, Root, Right) 
# (b) Preorder (Root, Left, Right) 
# (c) Postorder (Left, Right, Root) 

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
	def insert(self, val=0):
		if self.val:
			
			if self.left is None:
				self.left = Node(val)
			elif self.right is None:
				self.right = Node(val)
			elif self.left.left is None:
				self.left.left = Node(val)
			elif self.left.right is None:
				self.left.right= Node(val)
		else:
			self.val = val
	def PrintTree(self):
		if self.left:
			self.left.PrintTree()
		print(self.val)
		if self.right:
			self.right.PrintTree()

root = Node(1)
root.insert(3)
root.insert()
root.insert()
root.insert(2)
root.PrintTree()


class Solution:

 
    def recoverTree(self, r: Node) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # inorder traversal of the tree. it should be an almost sorted list where only two
        #elements are swapped.
        def inorder(r:Node):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        #identify two swapped elements x and y in linear time
        def find_two_swapped(nums) -> (int,int):
            n = len(nums)
            x= y= -1
            for i in range(n-1):
                if nums[i+1] <nums[i]:
                    y = nums[i+1]
                    if x == -1:
                        x= nums[i]
                    else:
                        break
            return x, y
        # traverse the tree again.Change value x to y and y to x
        def recover(r:Node, count:int):
            if r: 
                if r.val == x or r.val ==y:
                    if r.val == x:
                        r.val =y
                    else:
                        r.val = x
                    count -= 1
                    if count ==0:
                        return
                    recover(r.left, count)
                    recover(r.right, count)
        nums = inorder(root)
        x,y = find_two_swapped(nums)
        recover(root,2)
        print("---------")
        root.PrintTree()


sl = Solution()
sl.recoverTree(root)   



