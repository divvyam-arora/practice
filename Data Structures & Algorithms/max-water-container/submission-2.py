class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights) - 1
        fmax = 0

        while l<r:

            fmax= max(((r-l)*min(heights[l], heights[r])), fmax)

            if (heights[l] < heights[r]):
                l+=1
            else:
                r-=1
        
        return fmax