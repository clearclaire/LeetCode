class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1]^num)
        # 누적합

        result = []
        for l, r in queries:
            result.append(prefix[r+1] ^ prefix[l])
        return result


        # emp = []
        # for aa in queries:
        #     initial = 0
        #     for bb in range(aa[0], aa[1]+1):
        #         initial ^= arr[bb]
        #     emp.append(initial)
        # return emp
    