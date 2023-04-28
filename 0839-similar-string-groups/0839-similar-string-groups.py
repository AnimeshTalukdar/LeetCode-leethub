class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                p[py] = px

        p = list(range(len(strs)))
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if sum(a != b for a, b in zip(strs[i], strs[j])) <= 2:
                    union(i, j)
        return len(set(find(i) for i in range(len(strs))))