class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1]* (len(nums)+1)
        memo[0] = nums[0]
        if len(nums) < 2:
            return memo[0]

        memo[1] = max(nums[0], nums[1])

        def dfs(i):
            if i == 0:
                return nums[i]
            
            if i == 1:
                return max(nums[0], nums[1])

            if memo[i] != -1:
                return memo[i]
            
            case1 = nums[i] + dfs(i - 2)
            case2 = dfs(i - 1)

            memo[i] = max(case1, case2)

            return max(case1, case2)

        return dfs(len(nums) - 1)