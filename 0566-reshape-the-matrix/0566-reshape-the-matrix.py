class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)* len(mat[0])!=r*c:
            return mat
        arr=[x for row in mat for x in row]
        return [arr[i*c:(i+1)*c] for i in range(r)]