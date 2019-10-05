class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        copy =[]
        num = len(matrix)
        for i in range(num/2):
            for j in range(num):
                copy.append(matrix[num-1-j][i])
                matrix[num-j][i]=matrix[num-1-i][num-1-i]
                matrix[num - 1 - i][num - 1 - i]=matrix[j][num-1-i]



