
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # 通过二分查找较短的nums，找到一个位置。满足以下条件：
        # 左边部分数量等于右边部分数量。
        # A数组的左部最大<=B数组右部最小；B数组的左部最大<=A数组右部最小。

        la, lb = None, None
        if len(nums1) < len(nums2):
            la = nums1
            lb = nums2
        else:
            la = nums2
            lb = nums1

        m, n = len(la), len(lb)
        l, r = 0, m

        while l <= r:

            i = int((l + r) / 2)
            j = int((m + n + 1) / 2 - i)

            if i < m and lb[j-1] > la[i]:
                l = i + 1
            elif i > 0 and la[i-1] > lb[j]:
                r = i - 1
            else:

                if i == 0:
                    mxl = lb[j-1]
                elif j == 0:
                    mxl = la[i-1]
                else:
                    mxl = max(la[i-1], lb[j-1])

                if (m + n) % 2 == 1:
                    return mxl

                if i == m:
                    mir = lb[j]
                elif j == n:
                    mir = la[i]
                else:
                    mir = min(la[i], lb[j])

                return (mxl + mir) / 2.0

        return 0


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 3], [2]))
