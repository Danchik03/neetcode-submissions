class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        run_left = 1
        run_right = 1
        for i in range(n):
            left[i] = run_left
            run_left *= nums[i]
        for i in range(n-1,-1,-1):
            right[i] = run_right
            run_right *= nums[i]
        for i in range(n):
            left[i] = left[i] * right[i]
        return left

        