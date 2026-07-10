from typing import List
from bisect import bisect_left
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted((v, i) for i, v in enumerate(nums))

        pos = [0] * n
        for i, (_, idx) in enumerate(arr):
            pos[idx] = i

        m = len(arr)
        LOG = 18

        nxt = [0] * m
        j = 0
        for i in range(m):
            while j + 1 < m and arr[j + 1][0] - arr[i][0] <= maxDiff:
                j += 1
            nxt[i] = j

        up = [nxt]
        for _ in range(1, LOG):
            prev = up[-1]
            cur = [0] * m
            for i in range(m):
                cur[i] = prev[prev[i]]
            up.append(cur)

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            l = min(pos[u], pos[v])
            r = max(pos[u], pos[v])

            if nxt[l] == l:
                ans.append(-1)
                continue

            steps = 0
            cur = l

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < r:
                    cur = up[k][cur]
                    steps += 1 << k

            if nxt[cur] >= r:
                ans.append(steps + 1)
            else:
                ans.append(-1)

        return ans       