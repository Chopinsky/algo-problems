class Solution:
  def reverseBits(self, n: int) -> int:
    s = bin(n)[2:]
    s = "0"*(32-len(s)) + s
    # print('init:', s)

    res = 0
    mask = 1

    for ch in s:
      if ch == '1':
        res |= mask

      mask <<= 1

    return res


        