class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        maxCount=0
        for i in nums:
            count=1
            j=i+1
            while j in nums:
                count+=1
                j+=1
            if count>maxCount:
                maxCount=count
        return maxCount
