#User function Template for python3
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def constructBinaryTree(self, pre, preMirror, size):
        if size == 0:
            return None
        if size == 1:
            return node(pre[0])
        root = node(pre[0])
        root.left = self.constructBinaryTree(pre[1:(len(pre)-1)//2+1], preMirror[(len(pre)-1)//2+1:], (len(pre)-1)//2 )
        root.right = self.constructBinaryTree(pre[(len(pre)-1)//2+1:], preMirror[1:(len(pre)-1)//2+1], (len(pre)-1)//2 )
        return root



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    def printInorder(node):
        if node == None:
            return
        printInorder(node.left)
        print(node.data, end = " ")
        printInorder(node.right)
        
    test_cases = int(input())
    for _ in range (test_cases):
        N = int(input())
        pre = list(map(int, input().split()))
        preMirror = list(map(int, input().split()))
        res = Solution().constructBinaryTree(pre, preMirror, N)
        if printInorder(res) != None:
            print(printInorder(res)[:len(printInorder(res))-2])
        print()
# } Driver Code Ends