class Solution:
    def maxArea(self, heights: List[int]) -> int:

        L = 0
        R = len(heights) - 1
        maxArea = 0

        while (L < R):
            newArea = min(heights[L], heights[R]) * (R-L)
            if (maxArea < newArea):
                maxArea = newArea

            if (heights[L] > heights[R]):
                R -= 1
            else:
                L += 1
            
        return maxArea