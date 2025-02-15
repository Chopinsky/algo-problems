'''
3271-hash-divided-string
'''

class Solution:
  def stringHash(self, s: str, k: int) -> str:
    def hash_substr(sub: str) -> str:
      # print('hash:', sub)
      total = sum(ord(ch)-ord('a') for ch in sub) % 26
      return chr(total + ord('a'))
    
    result = ""
    n = len(s)

    for i in range(0, n, k):
      result += hash_substr(s[i:i+k])

    return result
