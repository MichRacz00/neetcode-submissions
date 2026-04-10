class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxVolumeLeft = []
        maxVolumeRight = [0] * n

        curMaxLeft = height[0]
        for i in range(n):
            curMaxLeft = max(curMaxLeft, height[i])
            maxVolumeLeft.append(curMaxLeft)
            
        curMaxRight = height[-1]
        for i in range(n - 1, -1, -1):
            curMaxRight = max(curMaxRight, height[i])
            maxVolumeRight[i] = curMaxRight

        total = 0

        for i in range(len(height)):
            maxVol = min(maxVolumeLeft[i], maxVolumeRight[i])
            total += maxVol - height[i]
            print(maxVol - height[i])

        return total

