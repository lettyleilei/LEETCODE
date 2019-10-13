import heapq
class Solution:
    def reorganizeString(self, S) :
        dic={}
        for s in S:
            if s in dic:
                dic[s]+=1
            else:
                dic[s]=1
        max_heap = []
        for x in dic:
            heapq.heappush(max_heap,(-dic[x],x))

        result=''


        num,x= heapq.heappop(max_heap)
        if -num>(len(S)+1)/2:
            return result
        else:
            heapq.heappush(max_heap,(num,x))
            while len(result)<len(S):
                print('s',max_heap)
                print(result)
                num1,x1=heapq.heappop(max_heap)
                result+=x1
                if max_heap:
                    print(max_heap)
                    num2,x2 = heapq.heappop(max_heap)
                    print(num1,x1,num2,x2)
                    result=result+x2
                    if num2 < -1:
                        heapq.heappush(max_heap, (num2 + 1, x2))
                if num1<-1:
                    heapq.heappush(max_heap,(num1+1,x1))
                print('m',max_heap)

        print(result)
        return result



test = Solution()
test.reorganizeString('aaabbbcccc'
                      '')
