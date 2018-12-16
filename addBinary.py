class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        maxlen = max(len(a), len(b)) + 1
        a, b = '0'*(maxlen-len(a))+a, '0'*(maxlen-len(b))+b
        sum = ['0']*maxlen

        for i in range(maxlen-1, -1, -1):
            s = int(a[i]) + int(b[i]) + int(sum[i])
            if s in [0, 1]:
                sum[i] = str(s)
            elif s == 2:
                sum[i] = str(0)
                sum[i-1] = str(1)
            else:
                sum[i] = str(1)
                sum[i-1] = str(1)

        if sum[0] == '0':
            return ''.join(sum[1:])
        return ''.join(sum)


if __name__ == "__main__":
    print(Solution().addBinary('1111', '1111'))
