from typing import List


class Solution:
    def is_possible_to_get_seats(self, n : int, m : int, seats : List[int]) -> bool:
        # code here
        if m==1:
            if n==0:
                return True
            elif n==1 and seats[0]==0:
                return True
            return False
        if seats[m-1]==0 and seats[m-2]==0:
            seats[m-1]=1
            n-=1
        if seats[0]==0 and seats[1]==0:
            seats[0]=1
            n-=1
        for i in range(1,m-1):
            if seats[i]==0 and seats[i-1]==0 and seats[i+1]==0:
                seats[i]=1
                n-=1
        return n<=0
        



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
        
        
        m = int(input())
        
        
        seats=IntArray().Input(m)
        
        obj = Solution()
        res = obj.is_possible_to_get_seats(n, m, seats)
        
        result_val = "Yes" if res else "No"
        print(result_val)

# } Driver Code Ends