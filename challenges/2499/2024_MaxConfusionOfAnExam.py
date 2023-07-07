'''
A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

Example 1:

Input: answerKey = "TTFF", k = 2
Output: 4
Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
There are four consecutive 'T's.
Example 2:

Input: answerKey = "TFFT", k = 1
Output: 3
Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
In both cases, there are three consecutive 'F's.
Example 3:

Input: answerKey = "TTFTTFTT", k = 1
Output: 5
Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT". 
In both cases, there are five consecutive 'T's.
 

Constraints:

n == answerKey.length
1 <= n <= 5 * 10^4
answerKey[i] is either 'T' or 'F'
1 <= k <= n
'''

from bisect import bisect_left


class Solution:
  def maxConsecutiveAnswers(self, keys: str, k: int) -> int:
    n = len(keys)
    if k >= keys.count('T') or k >= keys.count('F'):
      return n
    
    def max_count(key: str) -> int:
      longest = 0
      count = 0
      l, r = 0, 0
      
      while r < n:
        if keys[r] == key:
          count += 1
          
        r += 1
        ln = r-l
        
        while l < r and ln-count > k:
          if keys[l] == key:
            count -= 1
            
          l += 1
          ln -= 1
            
        # print(key, (l, r), ln, count)
        if ln-count <= k:
          longest = max(longest, ln)
      
      return longest
      
    return max(max_count('T'), max_count('F'))
        

  def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
    left, longest = 0, 0
    tcnt, fcnt = 0, 0
    
    # the idea is to keep either T count or F count in the 
    # window to be smaller than k, such that we can turn the
    # min number of (T, F) to the other in this window
    for right in range(len(answerKey)):
      # adding the latest char to the window
      if answerKey[right] == "T":
        tcnt += 1
      else:
        fcnt += 1

      # can't turning all chars in this window to 
      # either 'T' or 'F', must shift left bound
      # of the window
      if tcnt > k and fcnt > k:
        if answerKey[left] == "T":
          tcnt -= 1
        else:
          fcnt -= 1

        left += 1

      # update the largest window size
      longest = max(longest, right-left+1)

    return longest
      
      
  def maxConsecutiveAnswers0(self, keys: str, k: int) -> int:
    n = len(keys)
    t_cnt = keys.count('T')
    f_cnt = n - t_cnt
    
    # we can change every answer to either T or F, whichever
    # has the most count
    if min(t_cnt, f_cnt) <= k:
      return n
    
    t = [0]
    f = [0]
    tlong, flong = 0, 0
    
    for i, val in enumerate(keys):
      if val == 'T':
        t.append(t[-1]+1)
        f.append(f[-1])
      else:
        t.append(t[-1])
        f.append(f[-1]+1)
      
      # print(i, val)
      
      # if turnning T to F
      if t[-1] <= k:
        flong = max(flong, i+1)
      else:
        j = bisect_left(t, t[-1]-k)
        flong = max(flong, i+1-j)
        # print('t->f:', j, i+1-j)
      
      # if turning F to T
      if f[-1] <= k:
        tlong = max(tlong, i+1)
      else:
        j = bisect_left(f, f[-1]-k)
        tlong = max(tlong, i+1-j)
        # print('f->t:', j, i+1-j)
        
    # print(t, f)
    return max(tlong, flong)
    