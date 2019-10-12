import heapq


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []
        self.count = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.count += 1
        heapq.heappush(self.max_heap, -num)
        max_heap_top = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, -max_heap_top)
        if self.count & 1:
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_heap_top)

    def findMedian(self):
        """
        :rtype: float
        """
        # print(self.max_heap,self.min_heap)
        if self.count & 1:
            # print('a',-self.max_heap[0])
            return -self.max_heap[0]
        else:
            # print('b',(-self.max_heap[0] + self.min_heap[0]) / 2.0)
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0