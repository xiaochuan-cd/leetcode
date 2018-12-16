class Solution:
    def layout(self, words, curlen, maxWidth, last=False):
        if len(words) == 1:
            return words[0] + ' '*(maxWidth-len(words[0]))
        if last:
            r = ' '.join(words)
            return r + ' '*(maxWidth-len(r))
        space = maxWidth - curlen
        space0 = space//(len(words)-1)
        space1 = space % (len(words)-1)
        ret = ""
        for i in range(len(words)-1):
            ret += words[i] + ' ' + ' '*space0
            if space1:
                ret += ' '
                space1 -= 1
        ret += words[-1]
        return ret

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        ret, s, curlen = [], 0, 0
        for k, v in enumerate(words):
            if curlen + 1 + len(v) > maxWidth:
                if s == k:
                    ret.append(self.layout(
                        words[s:k+1], curlen, maxWidth))
                    s, curlen = k + 1, 0
                else:
                    ret.append(self.layout(
                        words[s:k], curlen, maxWidth))
                    s, curlen = k, len(v)
            else:
                if curlen:
                    curlen += 1
                curlen += len(v)
        if words[s:]:
            ret.append(self.layout(
                words[s:], curlen, maxWidth, True))

        return ret


if __name__ == "__main__":
    print(Solution().fullJustify(["a"], 1))
    print(Solution().fullJustify(
        ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
         "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20))
