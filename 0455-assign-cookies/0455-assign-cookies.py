class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        child_i = 0
        cookie_i = 0

        while child_i < len(g) and cookie_i < len(s):
            if s[cookie_i] >= g[child_i]:
                child_i += 1
            cookie_i += 1

        return child_i
