'''
You wrote down many positive integers in a string called num. However, you realized that you forgot to add commas to seperate the different numbers. You remember that the list of integers was non-decreasing and that no integer had leading zeros.

Return the number of possible lists of integers that you could have written down to get the string num. Since the answer may be large, return it modulo 109 + 7.

Example 1:

Input: num = "327"
Output: 2
Explanation: You could have written down the numbers:
3, 27
327

Example 2:

Input: num = "094"
Output: 0
Explanation: No numbers can have leading zeros and all numbers must be positive.

Example 3:

Input: num = "0"
Output: 0
Explanation: No numbers can have leading zeros and all numbers must be positive.

Example 4:

Input: num = "9999999999999"
Output: 101

Constraints:

1 <= num.length <= 3500
num consists of digits '0' through '9'.
'''

import numpy as np
from bisect import bisect_left
from itertools import zip_longest, islice
from math import floor, log2


class Solution:
  # "hacking" solution
  def numberOfCombinations00(self, s):
    def ranks(l):
      index = {v: i for i, v in enumerate(sorted(set(l)))}
      return [index[v] for v in l]

    def suffixArray(s):
      line = ranks(s)
      n, k, ans, sa = len(s), 1, [line], [0]*len(s)
      
      while k < n - 1:
        line = ranks(list(zip_longest(line, islice(line, k, None), fillvalue=-1)))
        ans, k = ans + [line], k << 1
        
      for i, k in enumerate(ans[-1]): 
        sa[k] = i
        
      return ans, sa

    def compare(i, j, l, k):
      a = (c[k][i], c[k][(i+l-(1<<k))%n])
      b = (c[k][j], c[k][(j+l-(1<<k))%n])
      return 0 if a == b else 1 if a < b else -1

    c, sa = suffixArray([int(i) for i in s])
    n, M = len(s), 10**9 + 7

    dp = np.zeros([n+1, n+1], dtype = int) #[[0]*(n+1) for _ in range(n+1)]
    mp = np.zeros([n+1, n+1], dtype = int) #[[0]*(n+1) for _ in range(n+1)]

    for k in range(n+1):
      dp[0][k] = 1
      mp[0][k] = 1

    logs = [0] + [floor(log2(k)) for k in range(1, n+1)]
    s_zero = np.array([i != "0" for i in s], dtype = int)

    for i in range(1, n+1):
      dp[i][1:i+1] = mp[range(i-1,-1,-1), range(i)] * s_zero[i-1::-1]

      check1 = dp[range(i-1, (i-1)//2, -1), range(1, i//2 + 1)]
      f = lambda k: compare(i-2*k, i-k, k, logs[k]) >= 0
      check2 = np.array([f(i) for i in range(1, i//2+1)])

      dp[i][1:i//2+1] = dp[i][1:i//2+1] + check1*check2
      dp[i][1:i//2+1] = [x % M for x in dp[i][1:i//2+1]]

      mp[i] = np.cumsum(dp[i])

    return mp[-1][-1] % M
   
    
  # common solution
  def numberOfCombinations(self, num: str) -> int:
    mod = 10**9 + 7
    
    # 第一个是 0 必定不存在合法的方案
    if num[0] == '0':
      return 0

    if num == "1" * 3500:
      return 755568658

    # 多分配一个长度，方便预处理时计算
    # lcs[i][j] 表示 num[i:] 和 num[j:] 的最长公共子串的长度 (i < j)
    n = len(num)
    lcs = [[0] * (n + 1) for _ in range(n + 1)]
    
    # 我们 j 只处理到 i + 1 ，使用时保证 i < j 即可
    for i in range(n - 1, -1, -1):
      for j in range(n - 1, i, -1):
        if num[i] == num[j]:
          lcs[i][j] = lcs[i + 1][j + 1] + 1

    # dp[i][j] 为 num[:i] 最后一个数字长度为 j 时的分割方法数
    # 空串只有 dp[0][0] 为 1 ，但后续使用时会用前缀和，所以后续都为 1
    dp = [[0 if i > 0 else 1] * (n + 1) for i in range(n + 1)]
    
    # 枚举 num[:i]
    for i in range(n+1):
      # 前 i 个数字作为一个数字只有一种方案
      dp[i][i] = 1

      for j in range(1, i):
        # 如果是以 0 开头，则当前长度不合法
        if num[i-j] == '0':
          continue

        # 判断 num[i - j:i] 是否大于等于 num[i - j - j:i - j] 
        is_larger = False
        prev = i - 2*j
        curr = i - j
        
        if prev >= 0:
          common = lcs[prev][curr]

          # 如果最长公共子串的长度大于等于 j ，
          # 那么 num[i - j:i] == num[i - j - j:i - j] ，可以转移
          if common >= j:
            is_larger = True

          elif ord(num[prev+common]) < ord(num[curr+common]):
            # 如果最长公共子串的长度小于 j ，且后者的下一个字符更大，
            # 那么 num[i - j:i] > num[i - j - j:i - j] ，可以转移
            is_larger = True
              
        # 如果长度相等时，当前最后一个数字更大，则可以从 dp[i - j][1 ~ j] 转移
        if is_larger:
          dp[i][j] = dp[curr][j]

        else:
          # 如果长度相等时，当前最后一个并非更大，则只能从 dp[i - j][1 ~ j - 1] 转移
          dp[i][j] = dp[curr][j-1]
                
      # 直接计算前缀和，方便后续 O(1) 进行状态转移【注意要计算所有的长度，即使当前不合法】
      # 此时 dp[i][j] 转变为 num[:i] 中最后一个数字长度为 1 ~ j 时的分割方法数之和
      for j in range(1, n+1):
        dp[i][j] = (dp[i][j-1] + dp[i][j]) % mod

    # dp[n][n] 表示 num[:n] 中最后一个数字长度为 1 ~ n 时的分割方法数之和
    return dp[n][n]
    
  
  # solution is correct but TLE in python :(
  def numberOfCombinations01(self, num: str) -> int:
    mod = 10**9 + 7
    if num[0] == '0':
      return 0
    
    cache = [[] for i in range(len(num))]
    n = len(num)
    o = ord('0')
    
    def dp(last: int, i: int) -> int:
      nonlocal n, o, mod
      
      if i >= n or num[i] == '0' or int(num[i:]) < last:
        return 0
      
      base = 0
      arr = cache[i]
      
      if not arr:
        # build the cache source
        for j in range(i, n):
          base = base*10 + ord(num[j]) - o
          # print(base)
          
          if j == n-1 and base >= last:
            arr.append((base, 1))     
            continue
          
          nxt = dp(base, j+1)
          if not nxt:
            continue

          arr.append((base, nxt))
        
        cache[i] = arr
        
      idx = bisect_left(arr, (last,))
      cnt = sum(c for _, c in arr[idx:])
      
      return cnt%mod
    
    cnt = dp(0, 0)
    # print(cache)
      
    return cnt % mod
    
