class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-stones[i] for i in range(len(stones))]
        heapq.heapify(stones)
        while len(stones)>1:
            a=heapq.heappop(stones)
            b=heapq.heappop(stones)
            # print(a,b)
            if abs(a-b)!=0:
                heapq.heappush(stones,-abs(a-b))
        if len(stones)==1:
            return abs(stones[0])
        else:
            return 0
            
        