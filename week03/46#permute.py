class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums)
        return self.res

    def backtrack(self, nums, vis = set(), r = []):
        if len(r) == len(nums):
            self.res.append([*r])
            return

        for n in nums:
            if n not in vis:
                vis.add(n)
                r.append(n)
                self.backtrack(nums, vis, r)
                vis.remove(n)
                r.pop()

