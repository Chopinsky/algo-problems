"""
3892-minimum-operations-to-achieve-at-least-k-peaks
"""

from functools import cache


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)
        INF = 10**18

        if k > n // 2:
            return -1

        if k == 0:
            return 0

        @cache
        def nei_ht(i: int) -> bool:
            left = nums[i - 1]
            right = nums[(i + 1) % n]
            return max(left, right)

        @cache
        def is_peak(i: int) -> bool:
            high = nei_ht(i)
            curr = nums[i]
            return curr > high

        @cache
        def cost(i: int) -> int:
            high = nei_ht(i)
            curr = nums[i]
            return high + 1 - curr if high >= curr else 0

        def count(first_peak: bool) -> int:
            prev2 = [INF] * (k + 1)
            prev1 = [INF] * (k + 1)
            prev1[0] = 0
            if first_peak:
                prev1[1] = cost(0)

            for i in range(1, n):
                val = cost(i)
                curr = [INF] * (k + 1)
                curr[0] = 0

                for j in range(1, k + 1):
                    curr[j] = min(curr[j], prev1[j])

                    if j == 1:
                        curr[j] = min(curr[j], prev1[0] + val)

                    elif (1 < i < n - 1) or (i == n - 1 and not first_peak):
                        curr[j] = min(curr[j], prev2[j - 1] + val)

                    if curr[j] >= INF:
                        break

                prev2, prev1 = prev1, curr

            return prev1[-1]

        peaks = [i for i in range(n) if is_peak(i)]
        if len(peaks) >= k:
            return 0

        low = min(count(False), count(True))

        return -1 if low >= INF else low
