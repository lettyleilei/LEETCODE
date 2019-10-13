class Solution:
    def isPossible(self, nums) :
        if len(nums)<3:
            return False
        result=[[]]
        last = nums[0]

        result[0].append(last)

        cur = 0
        for i in range(1,len(nums)):
            if nums[i]==last:
                cur += 1
                # print(cur,result)
                if cur<=len(result) and result[-cur][-1] == nums[i]-1:
                    result[-cur].append(nums[i])
                else:

                    result.append([])

                    result[-1].append(nums[i])
                    # print('b',result)
            elif nums[i]==last+1:
                cur=1
                result[-1].append(nums[i])
            else:
                result.append([])

                result[-1].append(nums[i])
                # print('c',result)
            last=nums[i]
        print(result)
        for i in range(len(result)):
            if len(result[i])<3:

                return False
        return True


test = Solution()
test.isPossible([1,2,3,4,6,7,7,8,9,10,10,11])