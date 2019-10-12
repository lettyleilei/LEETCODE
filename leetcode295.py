class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.

        """
        self.array = []
        self.length = 0
    def addNum(self, num: int) -> None:
        index =self.split(num)
        self.array.insert(index,num)
        print(self.array)
        self.length+=1
    def split(self,num):
        if not self.array:
            return 0
        low = 0
        high = self.length-1


        while low<=high :

            mid = int((high +low)/ 2)

            print(self.array,low, mid, high)
            if self.array[mid]<num:
                low = mid+1
            elif self.array[mid]>num :
                high = mid-1
            else:
                return mid


        return low
    def findMedian(self) -> float:
        mid= int((self.length+1)/2)
        print(mid,self.array)
        if self.length%2==1:
            print(self.array[mid-1])
            return self.array[mid-1]
        else:
            print((self.array[mid-1]+self.array[mid])/2)
            return (self.array[mid-1]+self.array[mid])/2

test = MedianFinder()
test.addNum(1)
test.addNum(2)
test.findMedian()
test.addNum(3)
test.findMedian()
test.addNum(4)
test.findMedian()
test.addNum(5)
test.findMedian()