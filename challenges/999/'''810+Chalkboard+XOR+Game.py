'''
You are given an array of integers nums represents the numbers written on a chalkboard.

Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first. If erasing a number causes the bitwise XOR of all the elements of the chalkboard to become 0, then that player loses. The bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is 0.

Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to 0, then that player wins.

Return true if and only if Alice wins the game, assuming both players play optimally.

Example 1:

Input: nums = [1,1,2]
Output: false
Explanation: 
Alice has two choices: erase 1 or erase 2. 
If she erases 1, the nums array becomes [1, 2]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 2 = 3. Now Bob can remove any element he wants, because Alice will be the one to erase the last element and she will lose. 
If Alice erases 2 first, now nums become [1, 1]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 1 = 0. Alice will lose.

Example 2:

Input: nums = [0,1]
Output: true

Example 3:

Input: nums = [1,2,3]
Output: true

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] < 2^16
'''


from typing import List, Dict, Set
from collections import Counter


class Solution:
  '''
  player who has even number of elements in `nums` will always have the move -- i.e. win,
  so there's no need to iterate over the game, just check if alice instantly win, or if
  she has even number of elements at the beginning of the game
  '''
  def xorGame(self, nums: List[int]) -> bool:      
    res = 0    
    counter = Counter(nums)
    
    for n, cnt in counter.items():
      if not cnt % 2:
        res ^= 0
      else:
        res ^= n

    return not res or not len(nums) % 2
  
    
  def xorGame0(self, nums: List[int]) -> bool:
    def xor_sum(c: Dict[int, int]) -> int:
      res = 0
      for n, cnt in c.items():
        if not cnt % 2:
          res ^= 0
        else:
          res ^= n
          
      return res
    
    counter = Counter(nums)
    cache = {}
    # print(counter)
    
    def play(curr_sum: int, curr_nums: Set[int]) -> bool:
      if not curr_nums or not curr_sum:
        return True 
      
      key = ''
      for n in sorted(curr_nums):
        if counter[n] > 0:
          key += f'{n}:{counter[n]},'
      
      # print(curr_sum, counter, key)
      if (curr_sum, key) in cache:
        return cache[curr_sum, key]
            
      for n in curr_nums:
        # erase n will cause instant lose, skip n
        if not n^curr_sum:
          continue
          
        counter[n] -= 1
        if not counter[n]:
          curr_nums.discard(n)
          
        res = play(n^curr_sum, curr_nums)
        
        counter[n] += 1
        curr_nums.add(n)
        
        if not res:
          return True
      
      return False
    
    return play(xor_sum(counter), set(counter.keys()))
  