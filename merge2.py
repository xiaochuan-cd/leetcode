class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        k = m+n-1
        while m > 0 or n > 0:
            if m > 0 and n > 0:
                nums1[k] = max(nums1[m-1], nums2[n-1])
                if nums1[k] == nums1[m-1]:
                    m -= 1
                else:
                    n -= 1
            elif m > 0:
                nums1[k] = nums1[m-1]
                m -= 1
            else:
                nums1[k] = nums2[n-1]
                n -= 1
            k -= 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    Solution().merge(nums1, 3, nums2, 3)
    print(nums1)
