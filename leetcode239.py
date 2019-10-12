class Solution:
    def maxSlidingWindow(self, nums, k) :
        if not nums:
            return 0
        length = len(nums)
        result = []
        max_num = max(nums[:k])
        result.append(max_num)

        for i in range(1, length + 1 - k):
            if nums[i] != max_num:
                max_num = max(nums[i:i + k])
                result.append(max_num)
            else:
                max_num = max(max_num,nums[i+k-1])
                result.append(max_num)
        print(result)
        return result

test = Solution()
test.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)