'''
Given two strings s and t, each of which represents a non-negative rational number, return true if and only if they represent the same number. The strings may use parentheses to denote the repeating part of the rational number.

A rational number can be represented using up to three parts: <IntegerPart>, <NonRepeatingPart>, and a <RepeatingPart>. The number will be represented in one of the following three ways:

<IntegerPart>
For example, 12, 0, and 123.
<IntegerPart><.><NonRepeatingPart>
For example, 0.5, 1., 2.12, and 123.0001.
<IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)>
For example, 0.1(6), 1.(9), 123.00(1212).
The repeating portion of a decimal expansion is conventionally denoted within a pair of round brackets. For example:

1/6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66).

Example 1:

Input: s = "0.(52)", t = "0.5(25)"
Output: true
Explanation: Because "0.(52)" represents 0.52525252..., and "0.5(25)" represents 0.52525252525..... , the strings represent the same number.
Example 2:

Input: s = "0.1666(6)", t = "0.166(66)"
Output: true
Example 3:

Input: s = "0.9(9)", t = "1."
Output: true
Explanation: "0.9(9)" represents 0.999999999... repeated forever, which equals 1.  [See this link for an explanation.]
"1." represents the number 1, which is formed correctly: (IntegerPart) = "1" and (NonRepeatingPart) = "".

Constraints:

Each part consists only of digits.
The <IntegerPart> does not have leading zeros (except for the zero itself).
1 <= <IntegerPart>.length <= 4
0 <= <NonRepeatingPart>.length <= 4
1 <= <RepeatingPart>.length <= 4
'''


from typing import Tuple


class Solution:
  def isRationalEqual(self, s: str, t: str) -> bool:
    debug = False
    
    def break_num(s: str) -> Tuple:
      s0 = s.split('.')
      if len(s0) == 1:
        return s0[0], '', '0'
      
      s1 = s0[1].split('(')
      if len(s1) == 1:
        return s0[0], s0[1], '0'
      
      ip = s0[0]
      nrp = s1[0]
      nrp_num = int(nrp if nrp else '0') 
      repeat = s1[1][:-1]
      ln = len(repeat)
      
      if ln > 1 and repeat == repeat[0] * ln:
        repeat = repeat[0]
      elif ln == 4 and repeat[:2] == repeat[2:]:
        repeat = repeat[:2]
        
      if repeat == '9':
        nxt_nrp = str(nrp_num + 1)
        repeat = '0'
        
        if debug:
          print(s, nrp, nxt_nrp)
        
        if not nrp or len(nxt_nrp) != len(str(nrp_num)):
          nrp = ''
          ip = str(int(ip)+1)
        else:
          nrp = '0'*(len(nrp)-len(nxt_nrp)) + nxt_nrp
      
      return ip, nrp, repeat
    
    def extend(nrp: str, rp: str, target: int) -> Tuple:
      while len(nrp) < target:
        nrp += rp[0]
        rp = rp[1:] + rp[0]
        
      return nrp, rp
    
    a0, a1, a2 = break_num(s)
    b0, b1, b2 = break_num(t)
    nrp_ln = max(len(a1), len(b1))
    
    if debug:
      print('before')
      print(a0, a1, a2)
      print(b0, b1, b2)
    
    a1, a2 = extend(a1, a2, nrp_ln)
    b1, b2 = extend(b1, b2, nrp_ln)
    
    if debug:
      print('after')
      print(a0, a1, a2)
      print(b0, b1, b2)
    
    return a0 == b0 and a1 == b1 and a2 == b2
    