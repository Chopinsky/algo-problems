'''
4119-minimum-set-bits-in-a-valid-integer
'''


class Solution:
  def minSetBits(self, nums: list[int], k: int) -> int:
    n = len(nums)
    m = n-k+1
    if m <= 0:
      return -1

    b = 31
    zero = [-1] * b
    masks = []

    for i in range(n):
      # add val to the AND
      for j in range(b):
        if (nums[i]>>j) & 1 == 0:
          zero[j] = i

      # pop val out of the subarr
      if i >= k-1:
        left = i-k+1
        x = 0

        for j in range(b):
          if zero[j] < left:
            x |= 1 << j

        # subarray AMD is 0
        if x == 0:
          return -1

        # add the subarr AND result
        masks.append(x)

    best = b

    def dfs(curr: int, used: int):
      nonlocal best

      # better solution exists
      if used >= best:
        return

      first = -1
      for idx, mask in enumerate(masks):
        if mask & curr == 0:
          first = idx
          break

      # used covers all branches already
      if first < 0:
        best = used
        return

      cand = masks[first]
      best_bit = 0
      best_gain = 0

      for j in range(b):
        bit = 1 << j
        if cand & bit:
          gain = 0
          for idx in range(first, m):
            if masks[idx] & curr == 0 and masks[idx] & bit:
              gain += 1

          if gain > best_gain:
            best_gain = gain
            best_bit = bit

      if best_bit:
        dfs(curr | best_bit, used + 1)

      for j in range(b):
        bit = 1 << j
        if (cand & bit) and bit != best_bit:
          dfs(curr | bit, used+1)

    dfs(0, 0)

    return best
