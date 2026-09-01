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
        #level order traversal means bfs printing
        #bfs means to explore the entire level, and then the children
        #so we do it with a queue?
        #but we need a way to group each level
        

        q = []
        ret = []

        if root:
            q.append(root)

        while q:
            length = len(q)
            level = []
            #process that many nodes to do the entire level
            for n in range(length):
                val = q.pop(0)
                level.append(val.val)
                if val.left:
                    q.append(val.left)
                if val.right:
                    q.append(val.right)

            ret.append(level)

        return ret

        