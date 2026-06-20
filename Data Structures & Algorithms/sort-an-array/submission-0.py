class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        # [3,2,4,1] ->
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]>nums[j]:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
        return nums
