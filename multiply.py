class Solution:

    def add(self, a, b):

        return str(int(a)+int(b))

        # i, j, va, vb, f, s = 0, 0, 0, 0, 0, ''

        # while i < len(a) or j < len(b):
        #     va, vb = 0, 0
        #     if i < len(a):
        #         va = a[len(a)-i-1]
        #     if j < len(b):
        #         vb = b[len(b)-j-1]

        #     f, r = divmod(int(va)+int(vb)+f, 10)
        #     s = str(r) + s

        #     i, j = i + 1, j+1

        # if f:
        #     s = str(f)+s

        # return s

    def mul(self, a, c):
        if a == '0':
            return '0'
        s = '0'*c
        return a+s

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        sumw = '0'
        for ki, i in enumerate(num1):
            sumx = '0'
            for kj, j in enumerate(num2):
                sumx = self.add(sumx, self.mul(
                    str(int(i)*int(j)), len(num2)-kj-1))
            sumw = self.add(self.mul(sumx, len(num1)-ki-1), sumw)

        return sumw


if __name__ == "__main__":
    print(Solution().multiply(
        '2322267896718392316129976729818262698599361122', '7348839706916210946024927859077721504476398931'))
    # print(Solution().multiply('0', '9133'))
    # print(Solution().multiply('1000000000', '1000000000'))
    # print(Solution().multiply('2', '0'))
    # print(Solution().multiply('2', '3'))
    # print(Solution().multiply('123', '456'))
