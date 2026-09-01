# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        #root to leaf path
        #is a full path that hits a None type for both children and then returns
        #we want to recursively try every path and our base case is when we reach target

        #or, we can make use of the left/right rule and follow the path we need?

        #how do we track the sum

        if not root:
            return False

        if not root.left and not root.right:
            return targetSum - root.val == 0
        
        targetSum -= root.val
            
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)