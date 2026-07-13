class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l, mid, r=0, n//2, n-1
        # [1,2,4,5,6,7] target=5
        while l<=r:
            if target==nums[l]:
                return l
            elif target==nums[r]:
                return r
            elif target==nums[mid]:
                return mid
            elif target>nums[mid]:
                l=mid+1
            elif target<nums[mid]:
                r=mid-1
            mid=(l+r)//2
        return -1
        