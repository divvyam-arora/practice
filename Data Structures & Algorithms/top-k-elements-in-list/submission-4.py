class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}

        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        
        return sorted(counter.keys(), key = counter.get, reverse=True)[:k]