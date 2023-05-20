#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def isStraightHand(self, N, groupSize, hand):

        m = {}
        for i in hand:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        count_arr = []
        for i in m:
            count_arr.append([i, m[i]])
        count_arr.sort()


        def fun(index, cur_count):
            nonlocal groupSize
            if index >= len(count_arr):
                return cur_count == 0
            if cur_count == 0:
                return True
            else:
                count_arr[index][1] -= 1
                if count_arr[index][1] < 0:
                    return False
                elif cur_count==groupSize or count_arr[index][0] == count_arr[index - 1][0] + 1:
                    return fun(index + 1, cur_count - 1)
                else:
                    return False

        flag = True
        for i in range(len(count_arr)):
            if count_arr[i][1] > 0:
                flag = flag and fun(i, groupSize )
        return flag

        # Code here

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, groupSize = list(map(int, input().split()))
        hand = list(map(int, input().split()))
        ob = Solution()
        res = ob.isStraightHand(N, groupSize, hand);
        print(res)
# } Driver Code Ends