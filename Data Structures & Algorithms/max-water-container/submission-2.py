class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0

        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                min_height = min(heights[l], heights[r])
                width = r - l
                volume = max(volume, min_height * width)
        
        return volume