class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        floor = n // 3
        ls = []
        i=0

        while i < n:
            j = i
            while j < n and nums[j] == nums[i]:
                j += 1

            if (j - i) > floor:
                ls.append(nums[i])

            i = j

        return ls