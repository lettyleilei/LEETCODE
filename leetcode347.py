class Solution:
    def topKFrequent(self, nums , k):
        countDict={}
        result = []
        for x in nums:
            if x in countDict:
                countDict[x]+=1
            else:
                countDict[x]=1

        countItem = []
        for i in countDict:
            countItem.append([i,countDict[i]])
        length = len(countItem)
        for i in range(int(length/2),-1,-1):
            self.heapSort(countItem,i,length)

        for j in range(k):

            countItem[0],countItem[-1] = countItem[-1],countItem[0]
            result.append(countItem.pop()[0])

            self.heapSort(countItem,0,length-1-j)
        print(result)
        return result



    def heapSort(self,arr,a,n):
        i=a
        j = i*2+1

        while j<n:
            if j+1<n:
                if arr[j+1][1]>arr[j][1]:
                    j+=1
            if arr[j][1]>arr[i][1]:
                arr[j],arr[i]=arr[i],arr[j]
                i=j
                j=i*2+1
            else:
                break

test = Solution()
test.topKFrequent([1],1)