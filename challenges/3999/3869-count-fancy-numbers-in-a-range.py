'''
3869-count-fancy-numbers-in-a-range
'''

from functools import lru_cache


class Solution:
  def is_good(self, num: int):
    val = str(num)
    inc = True
    dec = True

    for i in range(1, len(val)):
      if val[i] <= val[i-1]:
        inc = False

      if val[i] >= val[i-1]:
        dec = False

    return inc or dec

  @lru_cache(None)
  def solve(self, n: int, good_sums: set[int]) -> int:
    if n <= 0:
      return 0
    
    s = str(n)
    ln = len(s)
    
    @lru_cache(None)
    def dp(pos: int, last: int, dirc: int, d_sum: int, tight: bool, started: bool) -> int:
      if pos == ln:
        # not started, not a valid sequence
        if not started:
          return 0
          
        # good sequence if direction is valid (1 or -1 or 0), or the digit sum is good (in the set)
        if dirc != 2 or d_sum in good_sums:
          return 1

        # not a good sequence
        return 0
      
      limit = int(s[pos]) if tight else 9
      ans = 0
      
      for d in range(limit+1):
        ntight = tight and (d == limit)
        
        if not started:
          if d == 0:
            # still not started
            ans += dp(pos+1, -1, 0, 0, ntight, False)
          else:
            # starting the sequence
            ans += dp(pos+1, d, 0, d, ntight, True)

          continue
        
        ndirc = dirc

        # update direction: 1: ascending, -1: descending, 2: invalid
        if dirc != 2:
          # start of the sequence, direction is not determined yet
          if dirc == 0:
            if d > last:
              ndirc = 1
            elif d < last:
              ndirc = -1
            else:
              ndirc = 2
          
          # middle of the ascending sequence
          elif dirc == 1:
            if d <= last:
              ndirc = 2
          
          # middle of the descending sequence
          else:
            if d >= last:
              ndirc = 2
        
        ans += dp(pos+1, d, ndirc, d_sum+d, ntight, True)
      
      return ans
    
    return dp(0, -1, 0, 0, True, False)

  def countFancy(self, l: int, r: int) -> int:
    good_sums = set[int]([val for val in range(1, 200) if self.is_good(val)])
    return self.solve(r, good_sums) - self.solve(l-1, good_sums)


  def countFancy(self, l: int, r: int) -> int:
    good = [False]*146

    def is_sum_good(val: int) -> bool:
      val = str(val)
      inc = True
      dec = True

      for i in range(1, len(val)):
        if val[i] <= val[i-1]:
          inc = False

        if val[i] >= val[i-1]:
          dec = False

      return inc or dec

    for val in range(136):
      if val < 10:
        good[val] = True
        continue

      good[val] = is_sum_good(val)

    # print('sum good:', good)
    q = list(range(10))
    g = set(range(10))
    hd = 0

    # generate ascending nums
    while hd < len(q):
      curr = q[hd]
      ld = curr % 10
      for d in range(ld+1, 10):
        nxt = curr*10 + d
        q.append(nxt)
        g.add(nxt)

      hd += 1

    q = list(range(10))
    hd = 0

    # generage descending nums
    while hd < len(q):
      curr = q[hd]
      ld = curr % 10
      for d in range(ld):
        nxt = curr*10 + d
        q.append(nxt)
        g.add(nxt)

      hd += 1

    g = sorted(g)
    bnd = [r, l-1]
    res = [0, 0]
    # print('good:', g)

    for k in range(2):
      n = bnd[k]
      if n < 0:
        continue

      s = str(n)
      ln = len(s)
      maxi = ln*9

      dp = [[[0 for _ in range(2)] for _ in range(maxi+1)] for _ in range(ln+1)]
      dp[0][0][1] = 1

      for i in range(ln):
        for j in range(maxi+1):
          for m in range(2):
            if not dp[i][j][m]:
              continue

            if m == 1:
              lim = ord(s[i]) - ord('0')
            else:
              lim = 9

            # print('iter:', lim)
            for d in range(lim+1):
              nt = 1 if m == 1 and d == lim else 0
              # print('update:', i+1, j+d, nt)
              dp[i+1][j+d][nt] += dp[i][j][m]

      total = 0
      for b in range(maxi+1):
        if good[b]:
          total += sum(dp[ln][b])

      res[k] = total

    ans = res[0] - res[1]
    for i in range(len(g)):
      x = g[i]
      if x >= l and x <= r:
        tmp = x
        ss = 0

        while tmp > 0:
          ss += tmp % 10
          tmp //= 10

        if not good[ss]:
          ans += 1

    return ans
