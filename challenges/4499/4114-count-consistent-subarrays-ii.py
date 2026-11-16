'''
4114-count-consistent-subarrays-ii
'''


class Solution:
  def countConsistent(self, nums: list[int]) -> int:
    n = len(nums)
    l = [-1] * n
    st = []

    for i, val in enumerate(nums):
      # pop elements from the stack to find the leftmost index
      # such that the element at that index is a submask of the current element
      # and the smallest in the (st[-1], i] range
      while st and (nums[st[-1]] & val) == val and val < nums[st[-1]]:
        st.pop()

      if st:
        l[i] = st[-1] 
      # else l[i] = -1 since no such index exists

      st.append(i)

    res = 0
    st = []

    for i in range(n-1, -1, -1):
      val = nums[i]

      # pop elements from the stack to find the rightmost index
      # such that the element at that index is a submask of the current element
      # and the smallest in the (st[-1], i] range
      while st and (nums[st[-1]] & val) == val and val < nums[st[-1]]:
        st.pop()

      r = st[-1] if st else n
      res += (i-l[i]) * (r-i)
      st.append(i)

    return res
        