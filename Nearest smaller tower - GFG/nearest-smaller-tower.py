#User function Template for python3

class Solution:
    def nearestSmallestTower(self,arr):
        #code here
        ans=[float("inf") for i in range(len(arr))]
        stack = []
        for i in range(len(arr)):
            
            while stack != [] and stack[-1][0]>=arr[i]:
                stack.pop()
            
            ans[i]=stack[-1][1] if len(stack)>0 else -1
            if stack ==[] or stack[-1][0]<arr[i]:
                stack.append([arr[i],i])
        # print (ans)
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            while stack != [] and stack[-1][0]>=arr[i]:
                stack.pop()
            choice=stack[-1][1] if len(stack)>0 else -1
            if stack ==[] or stack[-1][0]<arr[i]:
                stack.append([arr[i],i])
            if ans[i]==-1:
                ans[i]=choice
            elif choice==-1:
                ans[i]=ans[i]
            else:
                if i- ans[i] < choice-i:
                    ans[i]=ans[i]
                elif i- ans[i] > choice-i:
                    ans[i]=choice
                else:
                    if arr[ ans[i]]<arr[choice]:
                        ans[i]=ans[i]
                    elif arr[ ans[i]]>arr[choice]:
                        ans[i]=choice
                    else:
                        ans[i] = ans[i]

        return ans
            
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input().strip())):
        N=int(input())
        arr=[int(i) for i in input().strip().split()]
        obj=Solution()
        ans=obj.nearestSmallestTower(arr)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends