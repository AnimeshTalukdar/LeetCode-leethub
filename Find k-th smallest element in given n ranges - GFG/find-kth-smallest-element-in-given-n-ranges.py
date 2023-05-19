
from typing import List
class Solution:
    def kthSmallestNum(self, n, v, q, qu):
        ans = []
        v.sort()
        for i in range(q):
            co = -1
            va = -1
            for j in range(n):
                if v[j][0] > co:
                    co = v[j][0] - 1
                if co >= v[j][1]:
                    continue
                if (co + qu[i]) > v[j][1]:
                    qu[i] -= v[j][1] - co
                    co = v[j][1]
                else:
                    va = co + qu[i]
                    break
            ans.append(va)
        return ans




#{ 
 # Driver Code Starts


class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



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
        
        
        ranges=IntMatrix().Input(n, 2)
        
        
        q = int(input())
        
        
        queries=IntArray().Input(q)
        
        obj = Solution()
        res = obj.kthSmallestNum(n, ranges, q, queries)
        
        IntArray().Print(res)
        

# } Driver Code Ends