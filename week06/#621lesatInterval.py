class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l = len(tasks)
        d = {}
        m = 0
        if n == 0:
            return l
        for i in range(l):
            if tasks[i] in d:
                d[tasks[i]] += 1
            else:
                d[tasks[i]] = 1
        a = sorted(d.items(), key=lambda x:x[1], reverse=True)
        for j in range(len(a)):
            if a[j][1] == a[0][1]:
                m += 1
        if len(d) <= n+1:
            res = (a[0][1]-1)*(n+1) + m
        else:
            res = max((a[0][1]-1)*(n+1) + m, l)
        return res
