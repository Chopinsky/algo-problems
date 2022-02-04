'''
Given an array of digits digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order. If there is no answer return an empty string.

Since the answer may not fit in an integer data type, return the answer as a string. Note that the returning answer must not contain unnecessary leading zeros.

Example 1:

Input: digits = [8,1,9]
Output: "981"
Example 2:

Input: digits = [8,6,7,1,0]
Output: "8760"
Example 3:

Input: digits = [1]
Output: ""
 

Constraints:

1 <= digits.length <= 10^4
0 <= digits[i] <= 9
'''


from typing import List


class Solution:
  def largestMultipleOfThree(self, digits: List[int]) -> str:
    rem1, rem2 = [], []
    store = []
    
    for val in digits:
      if val % 3 == 0:
        store.append(str(val))
      elif val % 3 == 1:
        rem1.append(str(val))
      else:
        rem2.append(str(val))
    
    if len(rem1) == len(rem2):
      store.extend(rem1)
      store.extend(rem2)
    else:
      rem1.sort(reverse=True)
      rem2.sort(reverse=True)
      ln1, ln2 = len(rem1), len(rem2)
      
      if ln1 > ln2:
        short = rem2
        long = rem1[:ln2]
        rem = rem1[ln2:]
        
      else:
        short = rem1
        long = rem2[:ln1]
        rem = rem2[ln1:]
        
      ln_rem = len(rem) % 3
      # print('rem:', rem, ln_rem)
      store.extend(long)
      
      if ln_rem == 0:
        store.extend(short)
        store.extend(rem)
      elif ln_rem == 2 and short:
        short.pop()
        store.extend(short)
        store.extend(rem)
      else:
        store.extend(short)
        if ln_rem < len(rem):
          store.extend(rem[:-ln_rem])
      
    # print(counter, store)
    store.sort(reverse=True)
    if store and store[0] == '0':
      return '0'
    
    return ''.join(store)
  