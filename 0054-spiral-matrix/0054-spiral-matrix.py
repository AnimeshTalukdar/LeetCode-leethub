class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l,r,t,b=0,len(matrix[0]),0,len(matrix)
        ans = []
        while l<r and t<b:

                for i in range(l,r):
                    # print(1)
                    ans.append(matrix[t][i])
                t+=1
                # print(ans,l,r,t,b)
                
                

                
                

                for i in range(t,b):
                    # print(2)
                    ans.append(matrix[i][r-1])
                r-=1
                # print(ans,l,r,t,b)
                
                if( not ( l<r and t<b)):
                    break;

                
                for i in range(r-1,l-1,-1):
                    # print(3)
                    ans.append(matrix[b-1][i])
                
                b-=1
                # print(ans,l,r,t,b)
         
                
                for i in range(b-1,t-1,-1):
                    # print(4)
                    ans.append(matrix[i][l])
                l+=1
                # print(ans,l,r,t,b)
        return ans
            