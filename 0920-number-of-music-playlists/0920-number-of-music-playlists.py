class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        @lru_cache(None)
        def helper(songs_used,songs_required):
            
            if songs_used == n and songs_required == 0:
                return 1
            if songs_used > n or songs_required == 0:
                return 0
            
            ans =( (n-songs_used) * helper(songs_used+1,songs_required-1))
            
            if songs_used > k:
                ans += ((songs_used-k)*helper(songs_used,songs_required-1))
            return ans%(10**9 +7)
        return helper(0,goal) % (10**9+7)