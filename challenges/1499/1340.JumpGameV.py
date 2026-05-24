'''
Given an array of integers arr and an integer d. In one step you can jump from index i to index:

i + x where: i + x < arr.length and 0 < x <= d.
i - x where: i - x >= 0 and 0 < x <= d.
In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) < k < max(i, j)).

You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
Output: 4
Explanation: You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.
Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 > 9.
Similarly You cannot jump from index 3 to index 2 or index 1.

Example 2:

Input: arr = [3,3,3,3,3], d = 3
Output: 1
Explanation: You can start at any index. You always cannot jump to any index.

Example 3:

Input: arr = [7,6,5,4,3,2,1], d = 1
Output: 7
Explanation: Start at index 0. You can visit all the indicies.

Example 4:

Input: arr = [7,1,7,1,7,1], d = 2
Output: 2

Example 5:

Input: arr = [66], d = 1
Output: 1


Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 10^5
1 <= d <= arr.length
'''

from typing import List
import math


class Solution:
  def maxJumps(self, arr: List[int], d: int) -> int:
    n = len(arr)
    jumps = [1]*n
    cand = sorted((h, i) for i, h in enumerate(arr))

    while cand:
      _, i = cand.pop()
      val = jumps[i]

      # check left:
      l = i-1
      while l >= 0 and i-l <= d and arr[l] < arr[i]:
        jumps[l] = max(jumps[l], val+1)
        l -= 1

      # check right:
      r = i+1
      while r < n and r-i <= d and arr[r] < arr[i]:
        jumps[r] = max(jumps[r], val+1)
        r += 1

    return max(jumps)

  def maxJumps(self, arr: List[int], d: int) -> int:
    n = len(arr)
    if n <= 1:
      return n

    dp = [1] * n
    stack = []

    def update(i: int, h: int):
      # iterate numbers in the queue until all numbers in it are taller
      # than the current number
      while len(stack) > 0 and arr[stack[-1]] < h:
        left = [stack.pop()]

        # must take out all the equal values as well, this (platform) is
        # where both i-th number and the stack[-1]-th number can jump onto
        while len(stack) > 0 and arr[stack[-1]] == arr[left[0]]:
          left.append(stack.pop())

        last = stack[-1] if len(stack) > 0 else -1

        for j in left:
          if i >= 0 and i - j <= d:
            dp[i] = max(dp[i], dp[j]+1)

          if last >= 0 and j - last <= d:
            dp[last] = max(dp[last], dp[j]+1)

    # for each number in the array, update the mono-dec queue, and udpate
    # the number of nodes we can jump on for both this number, as well as
    # the last number in the queue after all the pop(s)
    for i, h in enumerate(arr):
      update(i, h)
      stack.append(i)

    # clean up the remaining numbers in the stack
    update(-1, math.inf)
    return max(dp)
