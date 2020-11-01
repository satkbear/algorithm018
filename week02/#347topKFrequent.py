class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        m = sorted(count.items(), key = lambda x: x[1], reverse=True)
        return [m[j][0] for j in range(k)]