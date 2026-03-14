class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        new = [[0 for _ in range(n)] for _ in range(n)]
        for r in range(n):
            for c in range(n):
                new[r][c] = matrix[n-1-c][r] 
        for r in range(n):
            for c in range(n):
                matrix[r][c] = new[r][c] 