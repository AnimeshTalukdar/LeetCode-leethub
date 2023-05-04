import heapq
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R, D = [], []
        for i, char in enumerate(senate):
            if char == "R":
                heapq.heappush(R,i)
            else:
                heapq.heappush(D,i)

        i = 0
        n = len(senate)
        while len(R) != 0 and len(D) != 0:
            if i  == R[0]:
                heapq.heappop(R)
                heapq.heappush(R,i+n)
                heapq.heappop(D)
            elif i == D[0]:
                heapq.heappop(D)
                heapq.heappush(D,i+n)
                heapq.heappop(R)
            # print(i)
            # print(R,D)
            i += 1
            # if i==10:
            #     break
        if len(R) != 0:
            return "Radiant"
        return "Dire"
