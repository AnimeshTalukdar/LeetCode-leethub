from typing import List

class Solution:
    def powerfullInteger(self, n : int, intervals : List[List[int]], k : int) -> int:
        starts=[]
        ends=[]
        for s,e in intervals:
            starts.append(s)
            ends.append(e)
        starts.sort()
        ends.sort()
        max_level=0
        max_point=0
        level=0
        s,e=0,0
        while s<len(starts) and e<len(starts):
            while s<len(starts) and starts[s]<=ends[e]:
                s+=1
                level+=1
            if level>=k:
                max_level=level
                max_point = ends[e]
            level-=1
            e+=1
        while e<len(ends):

            if level>=k:
                max_level=level
                max_point = ends[e]
            e+=1
            level-=1
        return max_point if max_level !=0 else -1

            
            
        



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


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        intervals=IntMatrix().Input(n, 2)
        
        
        k = int(input())
        
        obj = Solution()
        res = obj.powerfullInteger(n, intervals, k)
        
        print(res)
        

# } Driver Code Ends