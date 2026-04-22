class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        le = len(arr)
        rmax = -1

        while le != 0:
            temp = arr[le - 1]
            arr[le - 1] = rmax
            rmax = max(rmax, temp)
            le -= 1

        return arr


        