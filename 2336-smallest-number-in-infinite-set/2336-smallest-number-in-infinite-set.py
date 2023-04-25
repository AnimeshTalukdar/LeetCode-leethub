class SmallestInfiniteSet:

    def __init__(self):
        self.heap=[]
        self.hash={}
        for i in range(1,1020):
            self.addBack(i)

    def popSmallest(self) -> int:
        del self.hash[self.heap[0]]
        return heapq.heappop(self.heap)
        

    def addBack(self, num: int) -> None:
        if num not in self.hash:
            heapq.heappush(self.heap,num)
            self.hash[num]=1
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)