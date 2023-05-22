class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        arr = []
        m = {}
        i = 0
        for n in nums:
            if n not in m:
                m[n] = i
                i += 1
                arr.append([n, 0])
            arr[m[n]][1] += 1

        arr.sort(key=itemgetter(1),reverse=True)
        ans = []
        print(arr)
        for i in range(k):
            ans.append(arr[i][0])
        return ans