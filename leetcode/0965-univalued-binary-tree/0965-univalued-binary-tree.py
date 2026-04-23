# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        visit=set([root])
        q=deque([root])
        ans=[]

        while q:
            node=q.popleft()

            ans.append(node.val)

            if node.left and node.left not in visit:
                visit.add(node.left)
                q.append(node.left)
            
            if node.right and node.right not in visit:
                visit.add(node.right)
                q.append(node.right)
        
        for i in range(1,len(ans)):
            if ans[i]!=ans[i-1]:
                return False
        
        return True
