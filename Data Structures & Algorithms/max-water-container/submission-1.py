class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        volume = 0

        for i in range(len(heights)):
            curVol = min(heights[l], heights[r]) * (r - l)
            volume = max(curVol, volume)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return volume
        