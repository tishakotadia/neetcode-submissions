class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs=set(nums)

        return not(len(hs)==len(nums))
