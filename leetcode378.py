import heapq
class Solution:

    def kthSmallest(self, matrix, k):

        n = len(matrix)
        max_heap = []
        for i in range(n):
            heapq.heappush(max_heap,(matrix[i].pop(0),i))
        result = 0
        while result<k:
            m,index = heapq.heappop(max_heap)
            result+=1
            if matrix[index] :
                print(matrix[index])
                heapq.heappush(max_heap,(matrix[index].pop(0),index))
        print(m)
        return m

test = Solution()
test.kthSmallest([[-1,0,9],[10,11,13],[12,13,15]],8)




