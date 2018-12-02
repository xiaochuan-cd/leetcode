class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """

        deck.sort(key=lambda x: (-x))

        r = []
        for i in deck:
            if len(r):
                r.insert(0, r.pop())
            r.insert(0, i)

        return r


if __name__ == "__main__":
    print(Solution().deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
