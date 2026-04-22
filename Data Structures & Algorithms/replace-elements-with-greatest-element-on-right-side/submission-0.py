class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        le = len(arr)
        rmax = arr[le - 1]

        while le != 0:
            nrmax = max(rmax, arr[le-1])
            arr[le - 1] = rmax
            rmax = nrmax
            le -= 1

        arr[len(arr) -1] = -1
        return arr


        