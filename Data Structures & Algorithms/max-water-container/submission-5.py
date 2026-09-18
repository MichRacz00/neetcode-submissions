class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_volume = 0

        while l < r:
            height = min(heights[l], heights[r])
            volume = height * (r - l)
            if volume > max_volume:
                max_volume = volume
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return max_volume
