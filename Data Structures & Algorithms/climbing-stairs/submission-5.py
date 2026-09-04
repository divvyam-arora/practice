class Solution:

    def climbStairs(self, n: int) -> int:
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
        one = 1
        two = 1
        for i in range(2, n + 1):
            one, two = two, one + two
        return two

