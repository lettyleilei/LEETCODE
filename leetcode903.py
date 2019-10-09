# class Solution:
#
#     def numPermsDISequence(self, S):
#         self.result = 0
#         num = len(S)
#         L = [i for i in range(num + 1)]
#
#         def dfs(s, l, r):
#
#             if not s:
#                 self.result +=1
#                 return
#             if s[0] == 'D':
#                 low = self.findX(l, r[-1])
#                 # print('low',s, l, r,low)
#                 if  low==-1:
#                     return
#                 for i in range(low + 1):
#                     dfs(s[1:], l[:i] + l[i + 1:], r + [l[i]])
#             else:
#                 high = self.findX(l, r[-1])
#                 # print('high', s, l, r, high)
#                 if high ==num-1:
#                     return
#                 for i in range(high + 1, len(l)):
#                     dfs(s[1:], l[:i] + l[i + 1:], r + [l[i]])
#         for i in range(num + 1):
#             dfs(S, L[:i] + L[i + 1:], [i])
#
#         # print(result)
#         return self.result%1000000007
#
#     def findX(self, List, n):
#         if not List:
#             return None
#         length = len(List)
#
#         mid = int(length / 2)
#         if List[mid] > n:
#             back = self.findX(List[:mid], n)
#             if back is None:
#                 return -1
#             return back
#         else:
#             back = self.findX(List[mid + 1:], n)
#             if back is None:
#                 return mid
#             return back + mid + 1

'''first try:out of time'''

'''second try'''
class Solution:
    def numPermsDISequence(self, S):
        self. Dtime = 0
        self.S = S
        for x in S:
            if x=='D':
                self.Dtime+=1

        num = len(S)
        self.item = [ i for i in range(num+1)]
        self.result=0

        if S[0]=='D':
            for x in range(1,num+1):
                self.find(x)

        else:
            for x in range(num):
                self.find(x)
        print(self.result)
        # return self.result


    def dfs(self,l,array,ID):
        if not l :
            ID.append(array)
        for i in range(len(l)):
            self.dfs(l[:i]+l[i+1:],array+[l[i]],ID)

    def verify(self,last,Iarray,Darray):
        s=self.S
        array=[]
        array.append(last)
        while s :

            if s[0]=='D':
                d = Darray[0]
                if d<last:
                    last=d
                    array.append(last)
                    Darray = Darray[1:]

                else:
                    return
            else:
                i = Iarray[0]
                if i>last:
                    last =i
                    array.append(last)
                    Iarray=Iarray[1:]
                else:
                    return
            s=s[1:]
            print('array',array)
        self.result+=1


    def find(self, x):
        new_item = self.item[:x] + self.item[x + 1:]
        D = new_item[:self.Dtime]
        I = new_item[self.Dtime:]
        self.Iarray = []
        self.Darray = []
        self.dfs(I, [], self.Iarray)
        self.dfs(D, [], self.Darray)
        print(self.Darray,self.Iarray)
        for i  in range(len(self.Iarray)):
            for j  in range(len(self.Darray)):
                print(self.Iarray[i],self.Darray[j])
                self.verify(x, self.Iarray[i],self.Darray[j])


test = Solution()
test.numPermsDISequence('DDI')

