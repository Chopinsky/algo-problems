'''
401. Binary Watch

A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

For example, the below binary watch reads "4:51".

Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.

For example, "01:00" is not valid. It should be "1:00".
The minute must consist of two digits and may contain a leading zero.

For example, "10:2" is not valid. It should be "10:02".

Example 1:

Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
Example 2:

Input: turnedOn = 9
Output: []

Constraints:

0 <= turnedOn <= 10
'''

from typing import List


h = {0:[0]}
m = {0:[0]}

def find(i: int, rem: int, arr: list, limit: int):
  n = len(arr)
  if rem > n-i or i >= n:
    return []

  if rem == 0:
    return [0]

  if rem == 1:
    return arr[i:]

  # base case: not using current hr digit
  ans = set(find(i+1, rem, arr, limit))

  # extra case: use current hr digit
  curr = arr[i]
  for t in find(i+1, rem-1, arr, limit):
    if curr+t >= limit:
      break

    ans.add(curr+t)

  return sorted(ans)

for ln in range(1, 11):
  h[ln] = find(0, ln, [1, 2, 4, 8], 12)

for ln in range(1, 11):
  m[ln] = find(0, ln, [1, 2, 4, 8, 16, 32], 60)

class Solution:
  def readBinaryWatch(self, cnt: int) -> List[str]:
    # print('init:', h, m)
    ans = []

    def format(th: int, tm: int) -> str:
      sh = str(th)
      sm = ("0" if tm < 10 else "") + str(tm)
      return f"{sh}:{sm}"

    for l0 in range(cnt+1):
      hl = h[l0]
      ml = m[cnt-l0]

      for th in hl:
        for tm in ml:
          ans.append(format(th, tm))

    return ans
        
  def readBinaryWatch(self, turnedOn: int) -> List[str]:
    if turnedOn == 0:
      return ['0:00']
    
    if turnedOn >= 9:
      return []
    
    h = [[] for _ in range(4)]
    h[0].append('0')
    
    m = [[] for _ in range(7)]
    m[0].append('00')
    
    def to_hour(val: int):
      if val == 0:
        return 0
      
      hour = 0
      mask = 1
      
      if val & mask > 0:
        hour += 1
        
      mask <<= 1
      if val & mask > 0:
        hour += 2
        
      mask <<= 1
      if val & mask > 0:
        hour += 4
        
      mask <<= 1
      if val & mask > 0:
        hour += 8
        
      return -1 if hour > 11 else hour
    
    def to_minute(val: int):
      if val == 0:
        return 0
      
      minute = 0
      mask = 1 
      
      if val & mask > 0:
        minute += 1
        
      mask <<= 1
      if val & mask > 0:
        minute += 2
        
      mask <<= 1
      if val & mask > 0:
        minute += 4
        
      mask <<= 1
      if val & mask > 0:
        minute += 8
        
      mask <<= 1
      if val & mask > 0:
        minute += 16
        
      mask <<= 1
      if val & mask > 0:
        minute += 32
        
      return -1 if minute > 59 else minute
      
    base = (1<<4) - 1
    while base > 0:
      cnt = (bin(base)[2:]).count('1')
      res = to_hour(base)
      if res >= 0:
        h[cnt].append(str(res))
      
      base -= 1
      
    base = (1<<6) - 1
    while base > 0:
      cnt = (bin(base)[2:]).count('1')
      res = to_minute(base)
      if res >= 0:
        s = str(res)
        if len(s) == 1:
          s = '0' + s
          
        m[cnt].append(s)
      
      base -= 1
    
    # print(h, m)
    ans = []
    for c0 in range(4):
      if not h[c0]:
        continue
      
      c1 = turnedOn - c0
      if c1 < 0:
        break
      
      if c1 > 6:
        continue
      
      for hval in h[c0]:
        for mval in m[c1]:
          ans.append(hval + ':' + mval)
    
    return ans
        
    