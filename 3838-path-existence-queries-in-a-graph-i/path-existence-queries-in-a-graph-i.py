from typing import List

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[bool]:

        group = [0] * n
        gid = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                gid += 1
            group[i] = gid

        return [group[u] == group[v] for u, v in queries]