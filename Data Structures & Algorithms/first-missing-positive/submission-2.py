class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num=set(nums)
        count=1
        while count in num:
            count+=1
        return count