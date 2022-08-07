'''
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3: 

Input: n = 5
Output: 68
 

Constraints:

1 <= n <= 2 * 10^4
'''


class Solution:
  '''
  alt solution: essentially we calculate sum(arr), where arr = (A ** n) * [1, 1, 1, 1, 1], 
  and A is:

  [
    [0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0],
  ]

  And we can calculate A ** n quickly with fast matrix multiplications
  '''
  def countVowelPermutation(self, n: int) -> int:
    rules = {
      0: [1],
      1: [0,2],
      2: [0,1,3,4],
      3: [2,4],
      4: [0]
    }
    
    curr, nxt = [1]*5, [0]*5
    mod = 10 ** 9 + 7
    
    for _ in range(1, n):
      for i in range(5):
        for j in rules[i]:
          nxt[j] = (nxt[j] + curr[i]) % mod
          
      curr, nxt = nxt, curr
      for i in range(5):
        nxt[i] = 0
    
    # print(curr)
    return sum(curr) % mod


  def countVowelPermutation(self, n: int) -> int:
    v = [1] * 5
    temp = [0] * 5
    
    while n > 1:
      temp[0] = v[1] + v[2] + v[4]
      temp[1] = v[0] + v[2]
      temp[2] = v[1] + v[3]
      temp[3] = v[2]
      temp[4] = v[2] + v[3]
      
      temp, v = v, temp
      n -= 1
      
    return sum(v) % (10**9 + 7)