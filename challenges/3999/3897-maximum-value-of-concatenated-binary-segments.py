'''
3897-maximum-value-of-concatenated-binary-segments
'''


top = 2*10**4
v0 = [1]*(top+1)
v1 = [0]*(top+1)
b0 = 2
b1 = 1
mod = 10**9+7

# precompute the values of v0 and v1
for i in range(1, top+1):
  v0[i] = b0
  v1[i] = b1

  b0 = (b0<<1) % mod
  b1 = ((b1<<1) | 1) % mod


class Solution:
  def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
    arr = sorted(zip(nums1, nums0), key=lambda x: (-x[0], x[1]))
    # all 1s will always go first
    a0 = [pair for pair in arr if pair[1] == 0]
    # the rest sorted by the number of 1s
    a1 = [pair for pair in arr if pair[1] > 0]
    # rebuild the list
    arr = a0 + a1
    val = 0
    # print('init:', arr)

    # all 0s, resulting value is 0
    if arr[0][0] == 0:
      return 0

    for oc, zc in arr:
      # shift value by oc+zc bits: the number of 0s and 1s
      val = (val * v0[oc+zc]) % mod
      # the value to be appended: int("1"*oc + "0"*zc, 2) % mod 
      add = (v1[oc] * v0[zc]) % mod
      # append the added value
      val = (val + add) % mod
      # print('iter:', (oc, zc), val, add)

    return val
        