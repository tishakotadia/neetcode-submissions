class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,i,h=0,0,len(nums)-1
        while i<=h:
            if nums[i]==1:
                i+=1
            elif nums[i]==0:
                nums[l],nums[i]=nums[i],nums[l]
                l+=1
                i+=1
            else:
                nums[h],nums[i]=nums[i],nums[h]
                h-=1

        