# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 # Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # look at the value of the node. If equal return the current node,
        if root.val == val:
            print(f"Found the value with node {root.left.val}<-{root.val}->{root.right.val}")
            return root
        else:
            if root.left != None and val < root.val:
                return self.searchBST(root.left,val)
            if root.right != None and val > root.val:
                return self.searchBST(root.right,val)
        return None
    
if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)


    """
         4
       /   \
       2    7
      / \
      1 3 
    """
    print(sol.searchBST(root, 2))