class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ans = []
        # Max = max(candies)
        for item in candies:
            ans.append(item+extraCandies >= max(candies))
        return ans