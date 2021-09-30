'''
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.


Example 1:

Input: A = [1], K = 1
Output: 1

Example 2:

Input: A = [1,2], K = 4
Output: -1

Example 3:

Input: A = [2,-1,2], K = 3
Output: 3


Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
'''

class Solution:
  def shortestSubarray(self, a: List[int], k: int) -> int:
    prefix = 0
    q = collections.deque([(0, -1)])
    ans = -1

    for i in range(len(a)):
      prefix += a[i]

      # left subarray can surely meet the needs, pop it since
      # future entries won't be better than this range: [left[1], i]
      while q and prefix - q[0][0] >= k:
        left = q.popleft()
        if ans < 0 or (i - left[1] < ans):
          ans = i - left[1]

      # pop anything that's not going to make the range happen better
      # than this range: [i, j]
      while q and q[-1][0] >= prefix:
        q.pop()

      q.append((prefix, i))

    return ans


  def shortestSubarray1(self, a: List[int], k: int) -> int:
    prefix = [0] + [val for val in a]
    q = []
    ans = -1
    ln = len(a)

    for i in range(ln):
      if prefix[i+1] >= k:
        return 1

      prefix[i+1] += prefix[i]

      if prefix[i+1] >= k and (ans < 0 or i < ans):
        ans = i+1

      if q:
        diff = prefix[i+1]-k
        idx = bisect.bisect(q, (diff, ))

        # print(i, idx, diff)

        if idx >= 0 and idx < len(q):
          l0 = -1

          if diff == q[idx][0]:
            l0 = i - q[idx][1]
          elif idx > 0:
            l0 = i - q[idx-1][1]

          # print(q[idx-1], i)

          if l0 > 0 and (ans < 0 or l0 < ans):
            ans = l0

      while q and q[-1][0] >= prefix[i+1]:
        q.pop()

      q.append((prefix[i+1], i))

      # print(i, q)

    # print(prefix)

    return ans