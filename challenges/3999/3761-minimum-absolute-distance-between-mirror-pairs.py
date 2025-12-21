'''
3761-minimum-absolute-distance-between-mirror-pairs
'''

from typing import List


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1
        last = {}

        for i, val in enumerate(nums):
            if val in last:
                dist = i-last[val]
                res = dist if res < 0 else min(res, dist)

            rval = int(str(val)[::-1])
            # print('iter:', val, rval)
            last[rval] = i

        return res
