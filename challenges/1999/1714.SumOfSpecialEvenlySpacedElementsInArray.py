'''
You are given a 0-indexed integer array nums consisting of 
n non-negative integers.

You are also given an array queries, where queries[i] = [x_i, y_i]. 
The answer to the i-th query is the sum of all nums[j] 
where x_i <= j < n and (j - x_i) is divisible by y_i.

Return an array answer where answer.length == queries.length and 
answer[i] is the answer to the i-th query modulo 10^9 + 7.

Example 1:

Input: nums = [0,1,2,3,4,5,6,7], queries = [[0,3],[5,1],[4,2]]

Output: [9,18,10]

Explanation: The answers of the queries are as follows:

1) The j indices that satisfy this query are 0, 3, and 6. nums[0] 
+ nums[3] + nums[6] = 9

2) The j indices that satisfy this query are 5, 6, and 7. nums[5] 
+ nums[6] + nums[7] = 18

3) The j indices that satisfy this query are 4 and 6. nums[4] + nums[6] = 10

Example 2:

Input: nums = [100,200,101,201,102,202,103,203], queries = [[0,7]]

Output: [303]

Constraints:

n == nums.length
1 <= n <= 5 * 10^4
0 <= nums[i] <= 10^9
1 <= queries.length <= 1.5 * 10^5
0 <= x_i < n
1 <= y_i <= 5 * 10^4
'''


from typing import List
from heapq import heappush, heappop


class Solution:
  def sum_special_elements(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    n = len(nums)
    prefix = [nums[i] for i in range(n)]
    odd_even = [nums[i] for i in range(n)]
    odd_tail, even_tail = nums[0], nums[1]

    for i in range(1, n):
      prefix[i] += prefix[i-1]
      if i > 1:
        odd_even[i] += odd_even[i-2]
        if i % 2:
          odd_tail = odd_even[i]
        else:
          even_tail = odd_even[i]

    q = []
    ans = [0] * len(queries)
    mod = 1_000_000_007

    for i, [l, d] in enumerate(queries):
      if d == 1:
        ans[i] = prefix[-1] if not l else prefix[-1] - prefix[l-1]
        ans[i] %= mod

      elif d == 2:
        if l % 2:
          ans[i] = odd_tail if l == 1 else odd_tail - odd_even[l-2]
        else:
          ans[i] = even_tail if l == 0 else even_tail - odd_even[l-2]

        ans[i] %= mod

      else:
        q.append((l, d, i))

    if not q:
      return ans

    q.sort()
    # print(q)
    j = 0
    stack = []

    for i, val in enumerate(nums):
      while j < len(q) and i >= q[j][0]:
        _, d, idx = q[j]
        heappush(stack, (i+d, d, idx))
        ans[idx] += val
        j += 1

      while stack and stack[0][0] == i:
        _, d, idx = heappop(stack)
        ans[idx]+= val
        heappush(stack, (i+d, d, idx))

    return ans


s = Solution()
t = [
  [[0,1,2,3,4,5,6,7], [[0,3],[5,1],[4,2]], [9,18,10]],
  [[100,200,101,201,102,202,103,203], [[0,7]], [303]],
]


for n, q, ans in t:
  res = s.sum_special_elements(n, q)
  print('\n=================\nTest case:', n, q)
  print('Expected:', ans)
  print('Gotten  :', res)
