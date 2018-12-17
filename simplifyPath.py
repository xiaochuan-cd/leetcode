class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        st, st1 = [], []
        for i in path:
            if st1:
                if st1[-1] == '/' and i == '/':
                    continue
                elif st1[-1] == '/' and i != '/':
                    st1.append(i)
                elif st1[-1] != '/' and i != '/':
                    st1.append(i)
                elif st1[-1] != '/' and i == '/':
                    cur = ''.join(st1)
                    if cur[0] == '/':
                        cur = cur[1:]
                    st1.clear()
                    if cur == '.':
                        continue
                    elif cur == '..':
                        if st:
                            st.pop()
                    else:
                        st.append(cur if cur[0] == '/' else '/' + cur)
            else:
                st1.append(i)

        if st1:
            cur = ''.join(st1)
            if cur[0] == '/':
                cur = cur[1:]
            if cur:
                if cur != '..' and cur != '.':
                    st.append(cur if cur[0] == '/' else '/' + cur)
                if cur == '..' and st:
                    st.pop()

        r = ''.join(st)
        return r if r else '/'


if __name__ == "__main__":
    print(Solution().simplifyPath("/.."))
    print(Solution().simplifyPath("///eHx/.."))
