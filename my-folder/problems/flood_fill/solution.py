class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        self.helper(image, sr, sc, color, image[sr][sc])

        return image
        

    def helper(self, image, sr, sc, color, old):
        # starting from the image[sr][sc] index, change to color
        # adjacent indeces might already BE color, so whatev
        # basically filling the entire island
        # base case breaks when the starting value is not the same as old
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != old:
            return 0

        if image[sr][sc] == color:
            return 
        image[sr][sc] = color

        self.helper(image, sr - 1, sc, color, old)
        self.helper(image, sr + 1, sc, color, old)
        self.helper(image, sr, sc - 1, color, old)
        self.helper(image, sr, sc + 1, color, old)        