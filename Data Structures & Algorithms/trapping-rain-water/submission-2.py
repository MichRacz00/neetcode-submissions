class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxHeightLeft = []
        maxHeightRight = [0] * n

        maxVolLeft = 0
        for i in range(n):
            maxVolLeft = max(maxVolLeft, height[i])
            maxHeightLeft.append(maxVolLeft)

        maxVolRight = 0
        for i in range(n - 1, -1, -1):
            maxVolRight = max(maxVolRight, height[i])
            maxHeightRight[i] = maxVolRight

        totalVol = 0
        for i in range(n):
            totalVol += min(maxHeightRight[i], maxHeightLeft[i]) - height[i]

        return totalVol

