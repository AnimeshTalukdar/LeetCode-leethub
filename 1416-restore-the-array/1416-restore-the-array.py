class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        len_k = len(str(k))
        dp = [0] * (len(s) + 1)
        dp[len(s)]=1
        for i in range(len(s)-1,-1,-1):
            if s[i]=='0':
                dp[i]=0
                continue
            res=0
            no=0
            for j in range(i, min(len(s),i+len_k)):
                no=no*10+int(s[j])
                if no <= k:
                    res = (res+dp[j + 1])% (10 ** 9 + 7)
            dp[i] = res
        return dp[0] % (10 ** 9 + 7)