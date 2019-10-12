class Solution:
    def kthSmallest(self, matrix, k):

        n = len(matrix)
        result = []

        while matrix[-1][-1] is not None:
            result.append(matrix[-1][-1])
            i,j = n-1,n-1
            self.sort(i,j,matrix)
            print(matrix)
        return result[-k]

    def sort(self,i,j,matrix):
        while   i>0 and j>0 :
            if i-1>0 and j-1>0 and matrix[i-1][j] is not None and matrix[i][j-1] is not None:
                if matrix[i-1][j]>matrix[i][j-1]:
                    matrix[i][j] =matrix[i-1][j]
                    matrix[i - 1][j]=None

                    i=i-1
                else:
                    matrix[i][j] = matrix[i ][j-1]
                    matrix[i][j - 1]=None

                    j = j - 1
            elif i-1>0 and  matrix[i-1][j] is not None:
                matrix[i][j] = matrix[i - 1][j]
                matrix[i - 1][j]=None

                i = i - 1
            elif j-1>0 and matrix[i][j-1] is not None:
                matrix[i][j] = matrix[i][j - 1]
                matrix[i][j - 1]=None
                j = j - 1
            else:
                break

            print(i,j)
            print(matrix)


test = Solution()
test.kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8)




