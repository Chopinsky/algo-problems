'''
order and str are strings composed of lowercase letters. In order, no letter occurs more than once.

order was sorted in some custom order previously. We want to permute the characters of str so that they match the order that order was sorted. More specifically, if x occurs before y in order, then x should occur before y in the returned string.

Return any permutation of str (as a string) that satisfies this property.

Example:
Input: 
order = "cba"
str = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

Note:

order has length at most 26, and no character is repeated in order.
str has length at most 200.
order and str consist of lowercase letters only.
'''


class Solution:
  def customSortString(self, order: str, s: str) -> str:
    o = [0] * 26
    oa = ord('a')
    
    for ch in s:
      o[ord(ch)-oa] += 1
      
    ans = ""
    for ch in order:
      count = o[ord(ch)-oa]
      if count == 0:
        continue
        
      ans += ch * count
      o[ord(ch)-oa] = 0
      
    for i in range(26):
      if o[i] > 0:
        ans += chr(oa+i) * o[i]
      
    return ans
  
    
  def customSortString1(self, order: str, s: str) -> str:
    orders = [-1] * 26
    oa = ord('a')
    idx = 0
    
    for ch in order:
      orders[ord(ch)-oa] = idx
      idx += 1
      
    for i in range(26):
      if orders[i] >= 0:
        continue
        
      orders[i] = idx
      idx += 1
      
    chars = list(s)
    # print(orders, chars)
    
    chars.sort(key=lambda x: orders[ord(x)-oa])
    ans = "".join(chars)
    
    return ans
  