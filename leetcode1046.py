class Solution:
    def lastStoneWeight(self, stones) :

        length = len(stones)
        for i in range(int(length / 2), -1, -1):
            self.heapSort(stones, length, i)

        i = length - 1
        while i > 1:

            stones[0], stones[i] = stones[i], stones[0]

            self.heapSort(stones, i, 0)

            stones[0], stones[i - 1] = stones[i - 1], stones[0]

            self.heapSort(stones, i - 1, 0)
            stones[i - 1] = abs(stones[i - 1] - stones[i])
            stones.pop()
            if stones[i - 1] == 0:
                stones.pop()
                self.heapSort(stones, i - 2, 0)
                i -= 2
            else:
                self.heapSort(stones, i - 1, 0)
                i = i - 1
            # print('c', stones)
        if i == 1:
            return abs(stones[0] - stones[1])
        return stones[0]

    def heapSort(self, arr, n, a):

        i = a
        j = i * 2 + 1
        while j <= n - 1:
            if j + 1 <= n - 1:
                if arr[j + 1] > arr[j]:
                    j = j + 1

            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i = j
                j = i * 2 + 1
            else:
                break