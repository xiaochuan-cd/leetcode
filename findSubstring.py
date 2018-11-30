class Solution:

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        out = []
        m1, m2 = {}, {}
        left = []
        cnt1, cnt2 = 0, 0

        if not words:
            return out

        for i in words:
            m1[i] = m1.get(i, 0) + 1
            cnt1 += 1

        lenw = len(words[0])

        for i in range(lenw):
            j = i
            while j < len(s):
                cur = s[j:j+lenw]
                if cur in m1:
                    m2[cur] = m2.get(cur, 0) + 1
                    cnt2 += 1
                    left.append(cur)
                    if m2[cur] > m1[cur] or cnt1 == cnt2:
                        if cnt1 == cnt2:
                            li = j-lenw*cnt1+lenw
                            if m1 == m2:
                                out.append(li)
                        m2[left[0]] -= 1
                        cnt2 -= 1
                        del left[0]
                else:
                    m2, cnt2, left = {}, 0, []
                # while
                j += lenw
            # for
            m2, cnt2, left = {}, 0, []

        return out


if __name__ == "__main__":
    print(Solution().findSubstring(
        "wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
