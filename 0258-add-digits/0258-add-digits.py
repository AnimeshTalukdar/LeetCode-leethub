class Solution:
    def sumdigits(self,num):
        ans = 0
        for char in str(num):
            ans+=int(char)
        return ans
        
    def addDigits(self, num: int) -> int:
        while num>9:
            num = self.sumdigits(num)
        return num
        