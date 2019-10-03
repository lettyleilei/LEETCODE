class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])
        for i in range(int((m + 1) / 2)):

            for j in range(i, n - 1 - i):
                result.append(matrix[i][j])

            for j in range(i, m - i):
                if n - i - 1 >= i:
                    result.append(matrix[j][n - 1 - i])

            for j in range(n - 2 - i, i, -1):

                if m - i - 1 > i:
                    result.append(matrix[m - 1 - i][j])
            for j in range(m - 1 - i, i, -1):
                if i + 1 < n - i:
                    result.append(matrix[j][i])
        return result