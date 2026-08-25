class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # create a stack
        # push the parenthesis onto the stack
        # when we hit closing, pop until you reach the matching opening bracket

        closing_parenth = [')', ']', '}']
        opening_parenth = ['(', '[', '{']
        
        stack = []

        #only add opening brackets waiting for a match
        for c in s:
            if c in opening_parenth:
                stack.append(c)
            
            elif c in closing_parenth:
                index = closing_parenth.index(c)
                if stack:
                    if stack[-1] == opening_parenth[index]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        if stack:
            return False
        return True
        