class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        checker = {}

        for i in nums:
            if i in checker:
                return True
            else:
                checker[i] = 1
        
        return False