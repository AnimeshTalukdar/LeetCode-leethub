
import heapq
import math
class Solution:
    def minimumNumber(self, n, arr):
        gc = arr[0]
        m_element= min(arr)
        for i in range(1,len(arr)):
            gc = math.gcd(gc,arr[i])
        if gc == m_element:
            return m_element
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        arr=[int(i) for i in input().split()]
        obj=Solution()
        print(obj.minimumNumber(n,arr))
# } Driver Code Ends