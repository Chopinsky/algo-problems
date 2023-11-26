'''
2949. Count Beautiful Substrings II

You are given a string s and a positive integer k.

Let vowels and consonants be the number of vowels and consonants in a string.

A string is beautiful if:

vowels == consonants.
(vowels * consonants) % k == 0, in other terms the multiplication of vowels and consonants is divisible by k.
Return the number of non-empty beautiful substrings in the given string s.

A substring is a contiguous sequence of characters in a string.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Consonant letters in English are every letter except vowels.

Example 1:

Input: s = "baeyh", k = 2
Output: 2
Explanation: There are 2 beautiful substrings in the given string.
- Substring "baeyh", vowels = 2 (["a",e"]), consonants = 2 (["y","h"]).
You can see that string "aeyh" is beautiful as vowels == consonants and vowels * consonants % k == 0.
- Substring "baeyh", vowels = 2 (["a",e"]), consonants = 2 (["b","y"]).
You can see that string "baey" is beautiful as vowels == consonants and vowels * consonants % k == 0.
It can be shown that there are only 2 beautiful substrings in the given string.
Example 2:

Input: s = "abba", k = 1
Output: 3
Explanation: There are 3 beautiful substrings in the given string.
- Substring "abba", vowels = 1 (["a"]), consonants = 1 (["b"]).
- Substring "abba", vowels = 1 (["a"]), consonants = 1 (["b"]).
- Substring "abba", vowels = 2 (["a","a"]), consonants = 2 (["b","b"]).
It can be shown that there are only 3 beautiful substrings in the given string.
Example 3:

Input: s = "bcdf", k = 1
Output: 0
Explanation: There are no beautiful substrings in the given string.

Constraints:

1 <= s.length <= 5 * 10^4
1 <= k <= 1000
s consists of only English lowercase letters.
'''

from collections import defaultdict


class Solution:
  '''
  # extreme state compression ...
  precursor #0: build a prefix sum array, where prefix[i] stores the number of vowels in subarray s[:i+1];
  precursor #1: build a list of candidate numbers, which will be the possible number of vowels in a subarray
                that meet all the criterials -- vowel_count == consonet_count; (vowel_count^2) % k == 0; 
                note that for such a number, say `x`, which denotes to a subarray of length `2x`, all subarray 
                with length `m*x` where m is in [1, 2, 3, ...] can also be added into the same bucket
  compression #1: at index-i, we have (vc_i, cc_i), where vc_i == count of vowels in the current string; cc_i == count 
                  of consonent in the current string; for any future index-j, only (vc_j, cc_j) with 
                  `diff = vc_i-cc_i = vc_j-cc_j` will have the equal number of vowels and consonent in the 
                  s[i+1:j]; so the first state is `diff`
  compression #2: for a candidate vowels count of `vc`, where vc*vc % k == 0, any longer length vc_long that
                  satisfy vc_long % vc == 0 will also satisfy (vc_long*vc_long) % k == 0, see precursor #1;
                  so for all future index-j that has the same remainder for `j % (2*vc)` will make a desired
                  subarray of s[i+1:j];

  now, store indices in a list, where both `diff` and `(c, mod_c)` are equal, and any pair in this list will be a 
  beautiful array; use `hash_map[diff, c, mod_c]` to create a counter for the state and easy-update of the index
  pair counts.
  '''
  def beautifulSubstrings(self, s: str, k: int) -> int:
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    cand, prefix = [], []
    n, total = len(s), 0
    
    for ch in s:
      pv = prefix[-1] if prefix else 0
      if ch in vowels:
        pv += 1
        
      prefix.append(pv)
      
    if prefix[-1] == 0 or prefix[-1] == n:
      return total
    
    top = min(prefix[-1], n-prefix[-1])
    sv = [val for val in range(top+1)]
    
    for c in range(2, top+1):
      if sv[c] < c or (c*c) % k > 0:
        continue
      
      cand.append(c)
      for c0 in range(2*c, top+1, c):
        if sv[c0] < c0:
          continue
          
        sv[c0] = c
      
    h = defaultdict(int)
    for i, vc in enumerate(prefix):
      # print('iter:', i, (vc, cc))
      cc = i + 1 - vc
      diff = vc - cc
      
      # any subarray with `diff` works for k == 1, only state
      # that matters is the `diff`, which is to satisfy the `vc == cc` 
      # condition, or condition #1;
      if k == 1:
        total += h[diff]
        h[diff] += 1
        if vc == cc:
          total += 1
          
        continue
      
      # if k > 1, only some subarray length is possible, loop
      # over all possible lengths to calculate and update the 
      # previous seen states
      for c in cand:
        # add all previous subarrays that fall into the same state
        mod = i % (2*c)
        total += h[diff, c, mod]
        h[diff, c, mod] += 1
        
        # subarray s[:i+1] meets the requirement
        if vc == cc and vc % c == 0:
          total += 1
          
    return total
  