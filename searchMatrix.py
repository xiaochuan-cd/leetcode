
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        sp = (len(matrix), len(matrix[0]))
        lo, hi = 0, sp[0]*sp[1]
        while lo < hi:
            mid = (lo+hi)//2
            if matrix[mid//sp[1]][mid % sp[1]] < target:
                lo = mid+1
            else:
                hi = mid

        return 0 <= lo < sp[0]*sp[1] and matrix[lo//sp[1]][lo % sp[1]] == target


if __name__ == "__main__":
    print(Solution().searchMatrix(
        [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ], 34
    ))
