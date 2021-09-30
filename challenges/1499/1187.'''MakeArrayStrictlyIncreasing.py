'''
Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.

Example 1:

Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output: 1
Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].

Example 2:

Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
Output: 2
Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].

Example 3:

Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
Output: -1
Explanation: You can't make arr1 strictly increasing.
 

Constraints:

1 <= arr1.length, arr2.length <= 2000
0 <= arr1[i], arr2[i] <= 10^9
 
'''


from typing import List
from collections import defaultdict
from bisect import bisect_right


class Solution:
  '''
  the idea is that we don't need to keep all possible increamental 
  arrays up to position-i, we just need to keep the ending number,
  and the least number of operations to reach this state as the 
  states for dp -- for each number `num` in arr1, 
      dp[ending_number] = least_operations_to_this_state
  then we can build new possible states from the last states:
    1) for a state in dp, if `num` > `ending_number`, we don't
       need to take any actions, just 
       next[num] = min(next[num], dp[ending_number])
    2) or, we can take a number from arr2 to replace `num`, which 
       must be slightly larger than `ending_number`, and if we can
       find such number, then the new state is 
       next[alt_arr2_num] = min(next[alt_arr2_num], dp[ending_number]+1)
   we keep iterating over all numbers in arr1 to find all possible
   states, and take the one with minimum operations
  '''
  def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
    ln = len(arr1)
    if ln == 1:
      return 0
    
    arr2 = sorted(set(arr2))
    
    # dp defines the {key:value} pairs, where key is the last element
    # in a valid array so far, and value is the number of operations
    # to reach this optimal array setup
    dp = { -1: 0 }
    
    # iterate over all numbers in arr1 to build up setups by adding `num` 
    # to the possible valid setups we obtain so far, and update them: 2 
    # ways of constructing the next valid array setup: if `num` is larger
    # than the original setup's final number, we take no action at all, 
    # take the minimum op number to reach this end state; or, if we replace
    # `num` with a number from arr2, which is slightly larger than the end
    # state number, we can construct a new end state with this number from
    # arr2 and optimal operation+1.
    for num in arr1:
      # no valid states to this point
      if not dp:
        break

      tmp = defaultdict(lambda: float('inf'))
      
      for last in dp:
        # for arrays ending with last, we take the minimum steps
        if num > last:
          tmp[num] = min(tmp[num], dp[last])
          
        # for arrays ending with arr2[repl_idx], we take the optimal steps + 1
        # from existing setups
        repl_idx = bisect_right(arr2, last)
        if repl_idx < len(arr2):
          val = arr2[repl_idx]
          tmp[val] = min(tmp[val], dp[last]+1)
      
      # update the end states
      dp = tmp
    
    if dp:
      return min(dp.values())
    
    return -1
