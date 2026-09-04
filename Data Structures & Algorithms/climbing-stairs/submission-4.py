class Solution:

    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)
        memo[0] = 1
        memo[1] = 1
        # if n >= 2:
        #     memo[2] = 2
        # def dfs(i):
        #     if i == 1:
        #         return 1
        #     if i == 2:
        #         return 2
        #     if memo[i] != -1:
        #         return memo[i]
        #     two = 1
        #     one = dfs(i - 1)
        #     if i > 1:
        #         two = dfs(i - 2)
        #     memo[i] = one + two
        #     return one + two
        # return dfs(n)
        for i in range(2, n + 1):
            one = memo[i - 1]
            two = memo[i - 2]
            memo[i] = one + two
        return memo[n]

