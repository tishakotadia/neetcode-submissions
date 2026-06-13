class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {} #{val:index}
        for i,number in enumerate(nums):
            diff=target-number
            if diff in myMap:
                return [myMap[diff], i]
            myMap[number]=i
