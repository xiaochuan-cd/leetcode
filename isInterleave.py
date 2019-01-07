class Solution:
    def isInterleave(self, s1, s2, s3):
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        rt = [[False for _ in range(l2+1)] for _ in range(l1+1)]
        rt[0][0] = True
        for i in range(l1+1):
            for j in range(l2+1):
                if j:
                    rt[i][j] = rt[i][j-1] and s3[i+j-1] == s2[j-1]
                if i and not rt[i][j]:
                    rt[i][j] = rt[i-1][j] and s3[i+j-1] == s1[i-1]
        return rt[l1][l2]

if __name__ == "__main__":
    print(Solution().isInterleave("aabcc", "dbbca","aadbbbaccc"))