import heapq
class Solution:
    def smallestDistancePair(self, nums, k):
        max_heap = []

        length = len(nums)
        for i in range(length):
            for j in range(i+1,length):
                heapq.heappush(max_heap,-abs(nums[i]-nums[j]))
                if len(max_heap)>k:
                    heapq.heappop(max_heap)

        result = heapq.heappop(max_heap)
        print(-result)
        return -result

test = Solution()
test.smallestDistancePair([1,3,1],1)





