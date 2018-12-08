class Solution:

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        value = [0]*(len(num1)+len(num2))

        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                value[i+j+1] += int(num1[i])*int(num2[j])

        carry = 0
        for i in range(len(value)-1, -1, -1):
            value[i] += carry
            carry, value[i] = divmod(value[i], 10)

        i = 0
        while i != len(value)-1 and value[i] == 0:
            i += 1

        return ''.join([str(x) for x in value[i:]])


if __name__ == "__main__":
    # print(Solution().multiply(
    #     '2322267896718392316129976729818262698599361122', '7348839706916210946024927859077721504476398931'))
    # print(Solution().multiply('0', '9133'))
    # print(Solution().multiply('1000000000', '1000000000'))
    # print(Solution().multiply('2', '0'))
    print(Solution().multiply('0', '0'))
    # print(Solution().multiply('123', '456'))
