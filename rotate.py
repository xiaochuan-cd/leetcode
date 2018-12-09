class Solution:
    def rotate(self, m):
        """
        :type m: List[List[int]]
        :rtype: void Do not return anything, modify m in-place instead.
        """
        lvl, last = 0, len(m)-1
        while lvl < int(len(m)/2):
            for i in range(lvl, last):
                m[lvl][i], m[i][last] = m[i][last], m[lvl][i]
                m[lvl][i], m[last][last-i + lvl] = m[last][last-i+lvl], m[lvl][i]
                m[lvl][i], m[last-i + lvl][lvl] = m[last-i+lvl][lvl], m[lvl][i]
            lvl += 1
            last -= 1


if __name__ == "__main__":
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    Solution().rotate(m)
    for i in m:
        print(i)

    m = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]

    Solution().rotate(m)
    for i in m:
        print(i)
