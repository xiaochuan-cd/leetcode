import bisect


class Solution:

    def recursive(self, nums):
        if not nums:
            return -2
        if len(nums) == 1:
            return -1
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            return -1
        if nums[0] < nums[-1]:
            return -1

        rotate = int((len(nums)-1)/2)

        if nums[0] > nums[rotate]:
            rotate -= rotate - self.recursive(nums[0:rotate+1])
        elif nums[rotate+1] > nums[-1]:
            rotate += self.recursive(nums[rotate+1:]) + 1

        return rotate

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        rotate = self.recursive(nums)

        r = -1
        if rotate+1 > 0 and target >= nums[0]:
            r = bisect.bisect_left(nums, target, 0, rotate)
        else:
            r = bisect.bisect_left(nums, target, max(0, rotate + 1))

        return r if r < len(nums) and nums[r] == target else -1


if __name__ == "__main__":
    print(Solution().search([1,3,5,7,9,10,11], 5))
    print(Solution().search([1,3,5], 5))
    nums = [57,58,59,62,63,66,68,72,73,74,75,76,77,78,80,81,86,95,96,97,98,100,101,102,103,110,119,120,121,123,125,126,127,132,136,144,145,148,149,151,152,160,161,163,166,168,169,170,173,174,175,178,182,188,189,192,193,196,198,199,200,201,202,212,218,219,220,224,225,229,231,232,234,237,238,242,248,249,250,252,253,254,255,257,260,266,268,270,273,276,280,281,283,288,290,291,292,294,295,298,299,4,10,13,15,16,17,18,20,22,25,26,27,30,31,34,38,39,40,47,53,54]
    print(Solution().search(nums, 30))
    print(Solution().search([2,3,4,5,6,7,8,9,1], 3))
    nums = [284,287,289,293,295,298,0,3,8,9,10,11,12,15,17,19,20,22,26,29,30,31,35,36,37,38,42,43,45,50,51,54,56,58,59,60,62,63,68,70,73,74,81,83,84,87,92,95,99,101,102,105,108,109,112,114,115,116,122,125,126,127,129,132,134,136,137,138,139,147,149,152,153,154,155,159,160,161,163,164,165,166,168,169,171,172,174,176,177,180,187,188,190,191,192,198,200,203,204,206,207,209,210,212,214,216,221,224,227,228,229,230,233,235,237,241,242,243,244,246,248,252,253,255,257,259,260,261,262,265,266,268,269,270,271,272,273,277,279,281]
    print(Solution().search(nums, 235))
    print(Solution().search([5, 1, 3], 1))
    print(Solution().search([7, 8, 1, 2, 3, 4, 5, 6], 2))
    print(Solution().search([3, 4, 5, 6, 1, 2], 2))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
    print(Solution().search([6, 7, 8, 1, 2, 3, 4, 5], 13))
    print(Solution().search([1, 3], 3))
    print(Solution().search([3, 1], 1))
    print(Solution().search([0], 1))
    print(Solution().search([], 1))
