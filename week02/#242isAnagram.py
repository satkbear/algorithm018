class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t or len(s) != len(t):
            return False

        count = {}
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        for j in t:
            if j in count:
                count[j] -= 1
            else:
                return False

        for m in count:
            if count[m] != 0:
                return False
            else:
                return True
