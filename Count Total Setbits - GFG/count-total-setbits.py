

class Solution:
    def countBits(self, n: int) -> int:
        ans = 0

        for i in range(32):
            x = (n + 1) // (1 << (i + 1))
            x = x * (1 << i)
            ans += x
            if i < 31:
                y = (n + 1) % (1 << (i + 1))
                y = max(0, y - (1 << i))
                ans += y
        return int(ans)

#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        obj = Solution()
        res = obj.countBits(N)
        
        print(res)
        

# } Driver Code Ends