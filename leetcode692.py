import heapq
class Solution:
    def topKFrequent(self, words, k) :
        dic={}
        for x in words:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1

        max_heap = []
        for x in dic:
            heapq.heappush(max_heap,(-dic[x],x))

        result = []
        for i in range(k):
            _,x = heapq.heappop(max_heap)
            result.append(x)
        print(result)
        return result

test =Solution()
test.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],4)