class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            x = target - nums[i]
            if x in nums:
                m = nums.index(x)
                if m == i:
                    continue
                else:
                    return[i, m]
                    break
            else:
                continue