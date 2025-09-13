'''
3681-maximum-xor-of-subsequences
'''

from typing import List


'''
To find the maximum XOR sum of a subsequence from an array, a common and efficient approach involves using a Trie (prefix tree).

Algorithm:
- Initialize a Trie: Create an empty Trie data structure. Each node in the Trie will represent a bit (0 or 1) and can have two children, one for 0 and one for 1.

- Insert elements into the Trie: For each number in the given array, insert its binary representation into the Trie. Start from the most significant bit (MSB) and traverse down to the least significant bit (LSB). If a path for a bit doesn't exist, create a new node.

- Find the maximum XOR:
  - For each number num in the array, perform a query in the Trie to find a number target such that num ^ target is maximized. 
  - Start from the root of the Trie.
  - For each bit of num (from MSB to LSB):
    - If the current bit of num is b, try to traverse the Trie along the path corresponding to 1 - b. This is because b ^ (1 - b) = 1, which maximizes the XOR for that bit position.
    - If the path for 1 - b exists, take it and append 1 to the current_xor_value.
    - If the path for 1 - b does not exist, you must take the path for b (since b ^ b = 0), and append 0 to the current_xor_value.

- The current_xor_value built during this traversal will be the maximum XOR value achievable with num and some number present in the Trie.

- Track the maximum: Keep track of the global maximum XOR value found across all num in the array.
'''
class Solution:
  def maxXorSubsequences(self, nums: List[int]) -> int:
    bs = []
    for val in nums:
      for b in bs:
        val = min(val , val^b)
      
      if val > 0:
        bs.append(val)
        bs.sort(reverse=True)

    maxVal = 0
    for b in bs:
      maxVal = max(maxVal , maxVal^b)

    return maxVal                
        
  def maxXorSubsequences(self, nums: List[int]) -> int:
    cand = sorted(set(nums))
    if not cand:
      return 0

    res = 0
    top = max(cand)

    while top > 0:
      res = max(res, res^top)
      for i in range(len(cand)):
        cand[i] = min(cand[i], cand[i]^top)

      top = max(cand)

    return res 
    
