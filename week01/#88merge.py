class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = 0, 0
        if m == 0:
            nums1[:] = nums2[:]
        elif n == 0:
            nums1 = nums1
        else:
            while j < n:
                if i >= m+j:
                    nums1[i:(i+n-j)] = nums2[j:n]
                    break 
                elif nums2[j] > nums1[i]:
                    i += 1
                else:
                    nums1.insert(i, nums2[j])
                    nums1.pop()
                    i += 1
                    j += 1

