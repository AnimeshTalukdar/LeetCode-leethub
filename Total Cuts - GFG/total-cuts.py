from typing import List


class Solution:
    def totalCuts(self, N: int, K: int, A: List[int]) -> int:
        max_left = [A[0]] * N
        min_right = [A[-1]] * N
        
        for i in range(1, N):
            max_left[i] = max(max_left[i-1], A[i])
        
        for i in range(N-2, -1, -1):
            min_right[i] = min(min_right[i+1], A[i])
        
        count = 0
        for i in range(N-1):
            if max_left[i] + min_right[i+1] >= K:
                count += 1
        
        return count



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        K = int(input())
        
        
        A=IntArray().Input(N)
        
        obj = Solution()
        res = obj.totalCuts(N,K,A)
        
        print(res)
        

# } Driver Code Ends