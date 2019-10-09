class KthLargest:

    def __init__(self, k, nums):
        nums.sort()
        if len(nums)<k:
            self.nums=nums
        else:
            self.nums = nums[-k:]

        self.k = k


    def findIndex(self,val):
        low = 0
        high = len(self.nums) - 1

        while low <= high:

            mid = int((low + high) / 2)

            if self.nums[mid] < val:
                low = mid + 1
            else:
                high = mid - 1
        self.nums.insert(low, val)
        if len(self.nums)>self.k:
            self.nums.pop(0)
        print(self.nums)
        print(self.nums[0])
        return self.nums[0]
    def add(self, val) :
        if not val:
            if len(self.nums)<self.k:

                return None
            else:

                return self.nums[0]

        else:

            return self.findIndex(val)


k=KthLargest(1,[])
k.add(-3)
k.add(-2)
# k.add(10)
# k.add(9)
# k.add(4)