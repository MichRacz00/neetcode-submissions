class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        volume = 0

        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            volume = max(volume, height * width)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return volume