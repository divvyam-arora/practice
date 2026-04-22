class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nlis = []
        for i in range(len(nums)):
            if nums[i] != val:
                nlis.append(nums[i])

        for i in range(len(nlis)):
            nums[i] = nlis[i]

        return len(nlis)     