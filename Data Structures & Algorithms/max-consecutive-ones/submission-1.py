class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        fin_count = 0
        count = 0
        for i in range (len(nums)):
            if nums[i] == 1:
                count+=1
                if count > fin_count:
                    fin_count = count
            else:
                count=0
        
        return fin_count

        