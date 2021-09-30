'''
Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 109 + 7.

Example 1:

Input: arr = [1,2], k = 3
Output: 9

Example 2:

Input: arr = [1,-2,1], k = 5
Output: 2

Example 3:

Input: arr = [-1,-2], k = 7
Output: 0

Constraints:

1 <= arr.length <= 10 ** 5
1 <= k <= 10 ** 5
-10**4 <= arr[i] <= 10**4
'''

class Solution:
  def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
    n0 = len(arr)
    if n0 == 1:
      return arr[0]*k if arr[0] > 0 else 0

    arr = arr*2 if k > 1 else arr
    presum = [v for v in arr]
    n = len(arr)

    for i in range(1, n):
      presum[i] += presum[i-1]

    arr_sum = presum[n0-1]
    ans = k * arr_sum
    small = 0

    for i, v in enumerate(presum):
      max_sum = v - small if i > 0 else v
      if arr_sum > 0 and k > 2:
        max_sum += (k-2) * arr_sum

      if max_sum > ans:
        ans = max_sum

      small = min(v, small)

    # print(n0, presum, ans)
    mod = 10 ** 9 + 7

    return max(0, ans) % mod
