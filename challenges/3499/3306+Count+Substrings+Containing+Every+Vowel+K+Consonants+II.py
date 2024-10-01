'''
3306. Count of Substrings Containing Every Vowel and K Consonants II
'''

class Solution:
  def countOfSubstrings(self, word: str, k: int) -> int:
    cnt = {
      'a': 0,
      'e': 0,
      'i': 0,
      'o': 0,
      'u': 0,
    }
    
    pos = {
      'a': 0,
      'e': 1,
      'i': 2,
      'o': 3,
      'u': 4,
    }
    
    mask = 0
    tgt = (1 << 5) - 1
    con = 0
    total = 0
    
    def update(ch: str, mask: int, is_add: bool) -> int:
      if ch not in cnt:
        return mask
      
      if is_add:
        cnt[ch] += 1
        if cnt[ch] == 1:
          mask |= (1<< pos[ch])
          
      else:
        cnt[ch] -= 1
        if not cnt[ch]:
          mask ^= (1 << pos[ch])
      
      return mask
    
    j, l = 0, 0
    n = len(word)
    
    for i in range(n-k-4):
      if i > 0:
        prev = word[i-1]
        if prev in cnt:
          mask = update(prev, mask, False)
        else:
          con -= 1
      
      if j < i:
        j = i
        mask = 0
        for ch in cnt:
          cnt[ch] = 0
        
      while j < n and (mask != tgt or con < k):
        ch = word[j]
        if ch in cnt:
          mask = update(ch, mask, True)
        else:
          con += 1
          
        j += 1
          
      l = max(l, j)
      while l < n and word[l] in cnt:
        l += 1
        
      # print('found:', (i, j, l), bin(mask)[2:], con)
      if mask == tgt and con == k:
        total += (l-j+1)
        
    return total
  
    