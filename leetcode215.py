class Solution:
    def findKthLargest(self, nums,k):
        if k>len(nums):
            return None

        def find2(num,m):

            p =num[0]
            p1 = 0
            for i in range(1,len(num)):
                if num[i]>p:
                    p1 += 1
                    num[p1],num[i]=num[i],num[p1]

            num[p1],num[0]=num[0],num[p1]

            if p1==m-1:
                return num[p1]
            elif p1>m-1:
                return find2(num[:p1],m)
            else: return find2(num[p1+1:],m-1-p1)
        print(find2(nums,k))
test  =Solution()
test.findKthLargest([1],1)







    #     def find1(lo,hi):
    #         if lo==hi:
    #             return nums[lo]
    #
    #         mid = (hi-lo)/2+lo
    #         left = find(lo,mid)
    #         right= find(mid,hi)
    #         combine = []
    #         while left and right:
    #             if left[0]<right[0]:
    #                 combine.append(left.pop(0))
    #             else:
    #                 combine.append(right.pop(0))
    #
    #         while right:
    #             combine.append(right.pop(0))
    #         while left:
    #             combine.append(left.pop(0))
    #
    #         return combine
    #
    #     new = find(nums)
    #     return new[-k]



