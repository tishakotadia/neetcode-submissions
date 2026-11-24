class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(len(nums)):
        #     j=i+1
        #     while j<len(nums):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        #         j+=1
        # return [-1,-1]

        ls={}
        for i in range(len(nums)):
            other=target-nums[i]
            if other in ls.keys():
                return [ls[other], i]
            else:
                ls[nums[i]]=i


