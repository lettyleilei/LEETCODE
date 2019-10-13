import heapq
class Solution:
    def kSmallestPairs(self, nums1 ,nums2 ,k) :
        result = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                heapq.heappush(result,(-(nums1[i]+nums2[j]),nums1[i],nums2[j]))
                if len(result)>k:
                    heapq.heappop(result)

        r =  []
        for _ in range(min(len(result),k)):
            _,num1,num2 = heapq.heappop(result)
            r.insert(0,[num1,num2])
        print(r)
        return r




test = Solution()
test.kSmallestPairs([1,2],[3],3)