import heapq
class Solution:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        num = len(Profits)
        max_heap=[]
        min_heap =[]

        for i in range(num):
            if Capital[i]<=W:
                heapq.heappush(max_heap,(-Profits[i],Capital[i]))
            else:
                heapq.heappush(min_heap,(Capital[i],Profits[i]))

        while k>0 and max_heap :
            print(max_heap,min_heap)
            profit,_ = heapq.heappop(max_heap)
            print(W,profit)
            W-=profit
            while min_heap :
                print(min_heap)
                top ,_=min_heap[0]
                if top<=W:
                    capital,profit = heapq.heappop(min_heap)
                    heapq.heappush(max_heap,(-profit,capital))
                else:break
            k-=1
        print(W)

        return W





test=Solution()
test.findMaximizedCapital(3,0,[1,2,3],[0,1,2])