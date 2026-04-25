class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in range (len(nums)):
            dic[nums[i]] = dic.get(nums[i], 0) + 1

        if len(dic) < len(nums):
            
            return True
        else:
            return False