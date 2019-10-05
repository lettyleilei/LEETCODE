class Solution:
    def kClosest(self, points, K):
        nums = []
        for p in range(len(points)):
            nums.append(points[p][0]**2+points[p][1]**2)


        def find2(point,num, k):

            p = num[0]
            p1 = 0
            for i in range(1, len(num)):
                if num[i] < p:
                    p1 += 1
                    num[p1], num[i] = num[i], num[p1]
                    point[p1], point[i] = point[i], point[p1]

            num[p1], num[0] = num[0], num[p1]
            point[p1], point[0] = point[0], point[p1]
            print(p1,point)
            if p1 == k - 1:
                return point[:p1+1]
            elif p1 > k - 1:
                return find2(point[:p1],num[:p1], k)
            else:
                return point[:p1+1]+find2(point[p1+1:],num[p1 + 1:], k - 1 - p1)

        print(find2(points,nums, K))

test = Solution()
test.kClosest([[3,3],[-2,4],[5,-1]],2)