from typing import List
class Solution:
    def arrayOperations(self, n: int, arr: List[int]) -> int:
        # code here
        count = 0
        for i in range(n):
            if arr[i] == 0:
                continue
            elif arr[i] != 0:
                count += 1
                j = i + 1
                while j < n:
                    if arr[j] != 0:
                        arr[j] = 0
                    else:
                        break
                    j += 1
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
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.arrayOperations(n, arr)
        
        print(res)
        

# } Driver Code Ends