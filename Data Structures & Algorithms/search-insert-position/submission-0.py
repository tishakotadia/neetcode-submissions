class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l, mid, r=0, n//2, n-1
        # [1,2,4,5,6,7] target=3
        while l<=r:
            mid=l + ((r - l) // 2)
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                r=mid-1
                n=mid
            else:
                l=mid+1
        return n