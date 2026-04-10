class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            newArea = min(heights[l], heights[r]) * (r - l)
            if newArea > area:
                area = newArea
                print(area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return area