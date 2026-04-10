class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            candidate = numbers[l] + numbers[r]
            if candidate < target:
                l += 1
            elif candidate > target:
                r -= 1
            else:
                break
        
        return [l + 1, r + 1]