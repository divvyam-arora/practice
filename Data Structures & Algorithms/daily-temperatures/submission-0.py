class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = []

        for i, j in enumerate(temperatures):

            while stack and j > stack[-1][1]:

                ind, val = stack.pop()
                res[ind] = i - ind
                
            stack.append([i, j])

        return res
        