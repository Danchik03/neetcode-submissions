class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol=[]
        nums.sort()
        for index, item in enumerate(nums):
            if index > 0 and item == nums[index - 1]:
                continue
            left = index+1
            right = len(nums)-1
            while left < right:
                triplet = item + nums[left] + nums[right]
                if triplet > 0:
                    right -= 1
                elif triplet < 0:
                    left += 1
                else:
                    if [nums[left],item,nums[right]] not in sol:
                        sol.append([nums[left],item,nums[right]])
                    right -= 1
        return sol

        



    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for index, item in enumerate(nums):
    #         dif = target - nums[index]
    #         if dif in nums[index+1:]:
    #              return [index, nums[index+1:].index(dif) + index + 1]
