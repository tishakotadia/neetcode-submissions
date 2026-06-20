class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hs={}
        high=len(nums)//2
        large=0
        for num in nums:
            hs[num]=1+hs.get(num,0)
            if hs[num]>high:
                large=num
        return large
        

        

