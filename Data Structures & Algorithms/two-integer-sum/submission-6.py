class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, item in enumerate(nums):
            dif = target - nums[index]
            if dif in nums[index+1:]:
                 return [index, nums[index+1:].index(dif) + index + 1]


                

        
        