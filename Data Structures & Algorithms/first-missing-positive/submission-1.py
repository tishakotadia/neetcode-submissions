class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num=sorted(set(nums))
        count=1
        while True:
            if count not in num:
                return count
            count+=1
        