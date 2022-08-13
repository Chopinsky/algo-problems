'''
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]

Constraints:

1 <= s.length <= 104
s consists of lower-case English letters.
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] consists of lower-case English letters.
'''


from typing import List
from collections import defaultdict, Counter, deque


class Solution:
  def findSubstring(self, s: str, words: List[str]) -> List[int]:
    ans = []
    n = len(s)
    m = len(words)
    k = len(words[0])
    dic = Counter(words)
    # print(dic)
    
    def search(idx: int):
      stack = deque([])
      seen = defaultdict(int)
      
      while idx+k <= n:
        w = s[idx:idx+k]
        if w not in dic:
          stack.clear()
          seen.clear()
        
        else:
          while stack and seen[w] >= dic[w]:
            w0, _ = stack.popleft()
            seen[w0] -= 1
            
          stack.append((w, idx))
          seen[w] += 1
          # print(stack)
          
        idx += k
        if len(stack) == m:
          ans.append(stack[0][1])
      
    for i in range(k):
      search(i)
      
    return ans


  def findSubstring(self, s: str, words: List[str]) -> List[int]:
    ans = []
    size = len(words[0])
    count = len(words)
    win_size = size * count
    freq = defaultdict(int)

    #create freq map of words 
    for word in words:
      freq[word] += 1

    '''
    # checking substrings with starting points from:
      [
         [0, size, 2*size, 3*size, .... ],
         [1, 1+size, 1+2*size, 1+3*size, ... ],
         ...
         [size-1, 2*size-1, 3*size-1, ... ]
      ]
      then we can jump over already validated portions
    '''
    for i in range(size):
      start = i
      
      while start+win_size-1 < len(s):
        curr = s[start:start+win_size]
        j = count
        seen = {}
        
        while j > 0:
          # get the next word to check
          word = curr[size*(j-1):size*j]
          word_count = seen[word] + 1 if word in seen else 1
          
          if (word not in freq) or (word_count > freq[word]):
            break
            
          seen[word] = word_count
          j -= 1
          
        if j == 0:
          ans.append(start)
          
        start += size * max(j, 1)
    
    return ans
    
    
  def findSubstring0(self, s: str, words: List[str]) -> List[int]:
    ans = []
    if len(s) == 0 or len(words) == 0:
      return ans

    count = len(words)
    size = len(words[0])
    total = 0
    dic = defaultdict(int)
    
    for w in words:
      dic[w] += 1
      total += 1
    
    checked = set()
    # print(dic, total)
    
    def check(start: int):
      nonlocal s, size, total
      
      # not going to work
      if s[start:start+size] not in dic:
        return
      
      # print("checking:", s, start)
      
      running = defaultdict(set)
      i = start
      count = 0
      win_open = start
      open_word = s[start:start+size]
      
      while i <= len(s)-size:
        word = s[i:i+size]
        checked.add(i)
        
        # print("seeing:", i)
        
        if dic[word] > 0:
          if len(running[word]) > 0 and len(running[word]) == dic[word]:
            if count == total and word == open_word:
              running[word].discard(win_open)
              running[word].add(i)
              
              win_open += size
              i += size
              
              ans.append(win_open)
              open_word = s[win_open:win_open+size]
              
              continue
              
            j = min(running[word])
            # print("before back up:", checked, running[word])
            
            for k in range(j+1, i+1):
              checked.discard(k)
            
            return
            
          else:
            running[word].add(i)
            count += 1
            i += size
            
            # print(win_open, count)
            
            if count == total:
              ans.append(win_open)
          
        else:
          break
        
      return

    for i in range(len(s)-count*size+1):
      if i in checked:
        continue
        
      check(i)
      # print(i, checked)
    
    return ans
    
