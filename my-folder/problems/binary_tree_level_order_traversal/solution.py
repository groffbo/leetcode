# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        q = []
        ret = []

        if root:
            q.append(root)
            ret.append([root.val])

        while q:
            curr = []
            for n in range(len(q)):
                tmp = q.pop(0)
                if tmp.left:
                    q.append(tmp.left)
                    curr.append(tmp.left.val)

                if tmp.right:
                    q.append(tmp.right)
                    curr.append(tmp.right.val)
            if curr:
                ret.append(curr)

        return ret
        
        

        