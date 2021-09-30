'''
A string s of lowercase letters is given.  Then, we may make any number of moves.

In each move, we choose one of the first k letters (starting from the left), remove it, and place it at the end of the string.

Return the lexicographically smallest string we could have after any number of moves.

Example 1:

Input: s = "cba", k = 1
Output: "acb"
Explanation:
In the first move, we move the 1st character ("c") to the end, obtaining the string "bac".
In the second move, we move the 1st character ("b") to the end, obtaining the final result "acb".

Example 2:

Input: s = "baaca", k = 3
Output: "aaabc"
Explanation:
In the first move, we move the 1st character ("b") to the end, obtaining the string "aacab".
In the second move, we move the 3rd character ("c") to the end, obtaining the final result "aaabc".

Note:

1 <= k <= s.length <= 1000
s consists of lowercase letters only.
'''

class Solution:
  def orderlyQueue(self, s: str, k: int) -> str:
    if k == 1:
      ans = s
      n = len(s)
      base = s[1:] + s[:-1]
      # print(base)

      for i in range(n-1):
        # print(i, base[i:(i+n)])
        if base[i:(i+n)] < ans:
          ans = base[i:(i+n)]

      return ans

    #todo: find shortest permutation -- reconstruct string
    chars = [0] * 26
    oa = ord('a')

    for ch in s:
      chars[ord(ch)-oa] += 1

    ans = ""
    for i, c in enumerate(chars):
      ans += chr(oa+i) * c

    return ans
