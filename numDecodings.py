class Solution:

    def recursive(self, s, start=0):

        n = self.d.get(start, -1)
        if n != -1:
            self.num += n
            return

        n = self.num
        if len(s)-start == 0:
            return
        elif len(s)-start == 1:
            if 0 < int(s[start]) <= 9:
                self.num += 1
        else:
            if 0 < int(s[start]) <= 9:
                self.recursive(s, start+1)
            else:
                return
            if 0 < int(s[start:start+2]) <= 26:
                if len(s)-start == 2:
                    self.num += 1
                else:
                    self.recursive(s, start+2)
            else:
                return

        self.d[start] = self.num-n

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.d = {}
        self.num = 0
        self.recursive(s)
        return self.num


if __name__ == "__main__":
    print(Solution().numDecodings("01"))
