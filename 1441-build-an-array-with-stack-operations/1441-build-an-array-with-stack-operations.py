class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(1, n + 1):
            ans.append("Push")
            if i not in target:
                ans.append("Pop")
            if i == target[-1]:
                return ans
        return ans
            