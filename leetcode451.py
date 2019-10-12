class Solution:
    def frequencySort(self, s):
        countdict = {}
        result = ''
        for x in s:
            if x in countdict:
                countdict[x]+=1
            else:
                countdict[x]=1

        countItem = []
        for x in countdict:
            countItem.append([x,countdict[x]])

        length = len(countItem)
        for i in range(int(length/2),-1,-1):
            self.heapSort(countItem,i,length)

        while countItem:
            countItem[0],countItem[-1] = countItem[-1],countItem[0]
            char = countItem.pop()
            result+=char[0] * char[1]
            length-=1
            self.heapSort(countItem,0,length)


        print(result)


    def heapSort(self,arr,a,n):
        i =a
        j = 2*i+1
        while j<n:
            if j+1<n:
                if arr[j+1][1]>arr[j][1]:
                    j+=1
            if arr[j][1]>arr[i][1]:
                arr[i],arr[j]=arr[j],arr[i]
                i = j
                j=i*2+1

            else:
                break

test = Solution()
test.frequencySort('bbbaaacccb')