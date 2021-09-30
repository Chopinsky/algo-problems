'''
Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]

Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0*0","0+0","0-0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []

Constraints:

1 <= num.length <= 10
num consists of only digits.
-2^31 <= target <= 2^31 - 1
'''


from typing import List
from collections import defaultdict


class Solution:
  def addOperators(self, nums: str, target: int) -> List[str]:
    n = len(nums)
    o = ord('0')
    cache = [None for _ in range(n)]
    
    def get_nums(i: int):
      nonlocal n, o
      if cache[i]:
        return cache[i]
      
      store = defaultdict(list)
      base = 0
      
      for j in range(i, n):
        base = base*10 + (ord(nums[j])-o)
        sb = str(base)
        
        if j < n-1:
          src = get_nums(j+1)
          # print(i, src)
          
          for m, c in src:
            for s in src[m, c]:
              # plus
              store[base, m+c].append(sb + '+' + s)
              # minus
              store[base, -m+c].append(sb + '-' + s)
              # times
              store[base*m, c].append(sb + '*' + s)
            
        else:
          store[base, 0].append(sb)
        
        if base == 0:
          break
        
      cache[i] = store
      return store
    
    arr = get_nums(0)
    ans = []
    
    for m, c in arr:
      if m+c == target:
        ans.extend(arr[m, c])
    
    return ans
  