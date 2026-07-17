class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        best = 0
        while left < right:
            width = right - left
            h = min(heights[left], heights[right])
            current = h*width
            if current > best:
                best = current
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return best


        