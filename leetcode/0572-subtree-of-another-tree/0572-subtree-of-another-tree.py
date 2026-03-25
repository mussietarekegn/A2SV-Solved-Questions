# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(t1: TreeNode,t2: TreeNode) -> bool:
    
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val!=t2.val:
                return False
            
            return helper(t1.right,t2.right) and helper(t1.left,t2.left)
        
        
        if not root:
            return False
        
        if helper(root,subRoot):
            return True
        
        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)
