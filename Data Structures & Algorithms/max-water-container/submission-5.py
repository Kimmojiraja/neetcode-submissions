class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # let's go for the bruth force first 

        x,y = 0,len(heights) - 1
        max_water = 0 

        while x<y:
            formulaa = min(heights[x],heights[y]) * (y - x)
            max_water = max(max_water, formulaa)

            if heights[x] <= heights[y]:
                x += 1 
            else:
                y -= 1
        return max_water

            