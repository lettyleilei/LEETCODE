class Solution:
    def majorityElement(self, nums):
        def MA(lo, hi):
            if lo == hi:
                return nums[lo]
            mid = int((hi - lo) / 2) + lo
            left = MA(lo, mid)
            right = MA(mid + 1, hi)

            if left == right:
                return left

            left_sum = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_sum = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            if left_sum > right_sum:
                return left

            return right

        return MA(0, len(nums) - 1)
