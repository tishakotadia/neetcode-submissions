class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashDict={}
        for i, num in enumerate(nums):
            diff=target-num
            if diff in hashDict:
                return [hashDict[diff], i]
            hashDict[num]=i