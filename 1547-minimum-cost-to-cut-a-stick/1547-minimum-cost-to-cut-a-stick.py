class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        m = {}
        def dfs(l,r):
            if (l,r) in m:
                return m[(l,r)]
            if r== l+1:
                return 0
            else:
                ans = float("inf")
                for cut in cuts:
                    if l<cut<r:
                        ans = min(
                            ans,
                            r-l+dfs(l,cut)+dfs(cut,r)
                        )
                ans = 0 if ans == float('inf') else ans
                m[(l,r)]= ans
                return ans
        return dfs(0,n)
                        
                        
        