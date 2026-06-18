class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k=0
        # for i in range(len(nums)):
        #     if nums[i]!=val:
        #         nums[k]=nums[i]
        #         k+=1
        # return k
        i, j=0, len(nums)-1
        while i<=j:
            if nums[i]==val:
                nums[i]=nums[j]
                j-=1
            else:
                i+=1
        return j+1