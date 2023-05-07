

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        res = []
        dp = [10 ** 8] * (len(obstacles) + 1)
        for n in obstacles:
            i = bisect.bisect(dp, n)
            res.append(i+1)
            dp[i] = n
        return res