
class Solution:
    def recursive(self, s, ret, st=0, pre=[]):

        left = len(s) - st
        if left == 0 and len(pre) == 4:
            ret.append('.'.join(pre))
            return

        if len(pre) >= 4 or left == 0:
            return

        if left == 1:
            if len(pre) == 3:
                ret.append('.'.join(pre+[s[st:]]))
            return
        elif left == 2:
            if len(pre) == 2:
                ret.append('.'.join(pre+[s[st]]+[s[st+1]]))
            if len(pre) == 3 and s[st] != '0':
                ret.append('.'.join(pre+[s[st:]]))
            return
        else:
            pre.append(s[st])
            self.recursive(s, ret, st+1, pre)
            pre.pop()
            if s[st] != '0':
                pre.append(s[st:st+2])
                self.recursive(s, ret, st+2, pre)
                pre.pop()
                if int(s[st:st+3]) <= 255:
                    pre.append(s[st:st+3])
                    self.recursive(s, ret, st+3, pre)
                    pre.pop()

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        ret = []
        self.recursive(s, ret)
        return ret


if __name__ == "__main__":
    print(Solution().restoreIpAddresses("1111"))
