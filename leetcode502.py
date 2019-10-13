import heapq
class Solution:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        num = len(Profits)
        Compony = [(Profits[i],Capital[i]) for i in range(len(Profits))]
        compony = sorted(Compony,key=lambda x :x[1])

        profit=[]
        captital = []
        for i in range(num):
            a,b = compony[i]
            profit.append(a)
            captital.append(b)


        low_index = 0
        high_index = self.split(W,captital)

        self.max_heap=[]

        while k>0 and num>0:

            max_num = self.heap(low_index,high_index,profit)

            if max_num is None:
                return W

            W+=max_num
            low_index = high_index
            high_index = self.split(W,captital)
            k-=1
            num-=1
        print(W)
        return W


    def heap(self,low_index,high_index,Profit):
        print(low_index,high_index)

        if low_index<high_index:

            for i in range(low_index,high_index):
                heapq.heappush(self.max_heap,-Profit[i])
        if not self.max_heap:
            return None
        return -heapq.heappop(self.max_heap)


    def split(self,n,arr):
        low = 0
        high = len(arr)-1
        print(n,arr)

        while low<=high:

            mid = int((low + high) / 2)

            if arr[mid]>n:
                if arr[mid-1]<=n:
                    return mid
                high = mid-1
            else:
                low=mid+1

        return low

test=Solution()
test.findMaximizedCapital(11,11,[1,2,3],[10,11,11])