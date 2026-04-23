class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        l = (start+end)//2
        while nums[l] != target:
            if start > end:
                return -1
            if nums[l] < target:
                start = l+1
            else:
                end = l-1

            l=(start+end)//2

        return l
