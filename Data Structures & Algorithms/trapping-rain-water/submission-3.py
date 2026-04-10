class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        max_left = 0
        for h in height:
            max_left = max(h, max_left)
            left.append(max_left)

        right = []
        max_right = 0
        for h in reversed(height):
            max_right = max(h, max_right)
            right.append(max_right)

        volume = 0

        for i in range(len(height)):
            volume += min(left[i], right[len(height) - i - 1]) - height[i]

        return volume