import copy
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_matrix = copy.deepcopy(matrix)
        for i in range(len(self.prefix_matrix)):
            s = 0
            for j in range(1,len(self.prefix_matrix[i])):
                self.prefix_matrix[i][j] = self.prefix_matrix[i][j]+self.prefix_matrix[i][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0
        print(row1,col1,row2,col2)
        for i in range(row1,row2+1):
            print(self.prefix_matrix[i][col2],self.prefix_matrix[i][col1-1])
            s+=self.prefix_matrix[i][col2]
            if col1-1>=0:
                s-=self.prefix_matrix[i][col1-1]
        return s


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# 2 1 4 3
# [3, 0, 1, 4, 2]
# [5, 6, 3, 2, 1]
# [1, 2, 0, 1, 5]
# [4, 1, 0, 1, 7]
# [1, 0, 3, 0, 5]



# [3, 0, 1, 4, 2]
# [5, 6, 3, 2, 1]
# [1, 2, 0, 1, 5]
# [4, 1, 0, 1, 7]
# [1, 0, 3, 0, 5]


