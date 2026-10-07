class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        for i in range(len(nums)):
            j= target-nums[i]
            if j in hashMap:
                return [hashMap[j], i]
            else:
                hashMap[nums[i]]=i