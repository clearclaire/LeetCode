class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        a, b, c = 0, 1, 1
        if n <= 1:
            return n
        elif n == 2:
            return c

        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c
        