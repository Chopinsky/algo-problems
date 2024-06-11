'''
3181. Maximum Total Reward Using Operations II

You are given an integer array rewardValues of length n, representing the values of rewards.

Initially, your total reward x is 0, and all indices are unmarked. You are allowed to perform the following operation any number of times:

Choose an unmarked index i from the range [0, n - 1].
If rewardValues[i] is greater than your current total reward x, then add rewardValues[i] to x (i.e., x = x + rewardValues[i]), and mark the index i.
Return an integer denoting the maximum total reward you can collect by performing the operations optimally.

Example 1:

Input: rewardValues = [1,1,3,3]

Output: 4

Explanation:

During the operations, we can choose to mark the indices 0 and 2 in order, and the total reward will be 4, which is the maximum.

Example 2:

Input: rewardValues = [1,6,4,3,2]

Output: 11

Explanation:

Mark the indices 0, 2, and 1 in order. The total reward will then be 11, which is the maximum.

Constraints:

1 <= rewardValues.length <= 5 * 10^4
1 <= rewardValues[i] <= 5 * 10^4
'''

from typing import List

class Solution:
  '''
  the key to solve this problem relies on the relization that for any `val`, for any existing and 
  valid sequence that sums to [0, val), we can append `val` to such sequence and obtain a new sequence
  that sums to the range of [val, 2*val) with a 1-to-1 mapping. 

  sort the array, and we can use bit representation for each 64 segement of the "sums" that a previously
  obtained sequences can sum to, this allows us to quickly mark the next segment of "sums" with the 
  addition of a new value.

  the result will be the position of the largest bit in the bit array, which represents the biggest value
  any valid sequence can sum to.
  '''
  def maxTotalReward(self, values: List[int]) -> int:
    cap = 64
    mask = (1<<cap)-1
    values = sorted(set(values))
    arr_size = 2*(1 + values[-1]//cap)
    bits = [0]*arr_size
    bits[0] |= 1
    # print('init', values, (arr_size, bits))
    
    def get_max_reward():
      i = arr_size-1
      while i > 0 and bits[i] == 0:
        i -= 1
      
      reward_bit = bits[i]
      shift = 0
      
      while reward_bit > 0:
        reward_bit >>= 1
        shift += 1
        
      return i*cap + shift - 1
      
    def update(val: int):
      offset, mod = divmod(val, cap)
      
      # loop over existing sequence with sums smaller than the
      # value to append to, and `i` is the index of the bit segment
      # containing sums if the bit at `64*i+shift` is 1
      for i in range(1+offset):
        base_bit = bits[i]
        
        # the last segment, mask the lower part to only keep the lower 
        # bits that are valid
        if i == offset:
          base_bit &= (1<<mod)-1
          
        # nothing to do in this range
        if base_bit == 0:
          continue
          
        # update the lower segment at the target location
        lower = (base_bit<<mod) & mask
        bits[i+offset] |= lower
        
        # update the upper segment at the target location (shift to
        # the next index because of cap overflow)
        upper = base_bit >> (cap-mod)
        bits[i+offset+1] |= upper
    
    for val in values:
      update(val)
    
    return get_max_reward()
        