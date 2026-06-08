class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l < r:

            mid = (l + r) // 2

            if target <= nums[mid]:
                r = mid

            elif target > nums[mid]:
                l = mid + 1   

        return l if (l < len(nums) and nums[l] == target) else -1