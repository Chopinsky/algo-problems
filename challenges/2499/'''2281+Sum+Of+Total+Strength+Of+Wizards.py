'''
As the ruler of a kingdom, you have an army of wizards at your command.

You are given a 0-indexed integer array strength, where strength[i] denotes the strength of the ith wizard. For a contiguous group of wizards (i.e. the wizards' strengths form a subarray of strength), the total strength is defined as the product of the following two values:

The strength of the weakest wizard in the group.
The total of all the individual strengths of the wizards in the group.
Return the sum of the total strengths of all contiguous groups of wizards. Since the answer may be very large, return it modulo 109 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: strength = [1,3,1,2]
Output: 44
Explanation: The following are all the contiguous groups of wizards:
- [1] from [1,3,1,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1
- [3] from [1,3,1,2] has a total strength of min([3]) * sum([3]) = 3 * 3 = 9
- [1] from [1,3,1,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1
- [2] from [1,3,1,2] has a total strength of min([2]) * sum([2]) = 2 * 2 = 4
- [1,3] from [1,3,1,2] has a total strength of min([1,3]) * sum([1,3]) = 1 * 4 = 4
- [3,1] from [1,3,1,2] has a total strength of min([3,1]) * sum([3,1]) = 1 * 4 = 4
- [1,2] from [1,3,1,2] has a total strength of min([1,2]) * sum([1,2]) = 1 * 3 = 3
- [1,3,1] from [1,3,1,2] has a total strength of min([1,3,1]) * sum([1,3,1]) = 1 * 5 = 5
- [3,1,2] from [1,3,1,2] has a total strength of min([3,1,2]) * sum([3,1,2]) = 1 * 6 = 6
- [1,3,1,2] from [1,3,1,2] has a total strength of min([1,3,1,2]) * sum([1,3,1,2]) = 1 * 7 = 7
The sum of all the total strengths is 1 + 9 + 1 + 4 + 4 + 4 + 3 + 5 + 6 + 7 = 44.
Example 2:

Input: strength = [5,4,6]
Output: 213
Explanation: The following are all the contiguous groups of wizards: 
- [5] from [5,4,6] has a total strength of min([5]) * sum([5]) = 5 * 5 = 25
- [4] from [5,4,6] has a total strength of min([4]) * sum([4]) = 4 * 4 = 16
- [6] from [5,4,6] has a total strength of min([6]) * sum([6]) = 6 * 6 = 36
- [5,4] from [5,4,6] has a total strength of min([5,4]) * sum([5,4]) = 4 * 9 = 36
- [4,6] from [5,4,6] has a total strength of min([4,6]) * sum([4,6]) = 4 * 10 = 40
- [5,4,6] from [5,4,6] has a total strength of min([5,4,6]) * sum([5,4,6]) = 4 * 15 = 60
The sum of all the total strengths is 25 + 16 + 36 + 36 + 40 + 60 = 213.

Constraints:

1 <= strength.length <= 10^5
1 <= strength[i] <= 10^9
'''

from typing import List


class Solution:
  def totalStrength(self, strength: List[int]) -> int:
    mod = 10**9 + 7
    prefix = []
    prefix_accum = []
    stack = [(-1, -1)]
    accum = []
    solve = []
    
    for i, val in enumerate(strength):
      # update the prefix-sums
      prefix.append((val + (prefix[-1] if prefix else 0)) % mod)
      prefix_accum.append(((i+1)*val + (prefix_accum[-1] if prefix_accum else 0)) % mod)
      
      # if wizard @ i has a larger strength than any of the previously checked wizards, then
      # his contribution equals the `<accumulated min-strength> * <ith-strength> + <previous-sum>`
      if val > stack[-1][0]:
        # setup states for accumulated min-strength stack
        accum.append(((i-stack[-1][1])*val + (accum[-1] if accum else 0)) % mod)
        stack.append((val, i))
        
        # update the contribution from position-i
        solve.append((accum[-1]*val + (solve[-1] if solve else 0)) % mod)
        # print('append:', i, val, accum)
        
      # if wizard @ i has a smaller strength than some previous wizards, reset the strength sum
      # the new sum will come from 3 parts -- 1) the strength sums of the remaining m-wizards; 
      # 2) add the sum from 1) with the strength sums between [m, i]; 3) add the strength added 
      # by the ith wizard, i.e. `<ith-strength> * <all-strengh-sums-between-m-and-i>`
      else:
        while stack and stack[-1] >= val:
          stack.pop()
          
        last = stack[-1][1]
        # print("??", i, val, last)
        
        if last >= 0:
          p0 = solve[last]
          p1 = accum[last] * (prefix[i] - prefix[last])
          p2 = (prefix_accum[-1] - prefix_accum[last] - (last+1) * (prefix[i] - prefix[last])) * val
        else:
          p0 = 0
          p1 = 0
          p2 = prefix_accum[-1] * val
          
        # setup states for accumulated min-strength stack
        accum.append(((i-last) * val + (accum[last] if last >= 0 else 0)) % mod)
        stack.append((val, i))
        
        # update the contribution from position-i
        solve.append((p0 + p1 + p2) % mod)
      
    # print(solve)
    res = 0
    for t in solve:
      res = (res + t) % mod
      
    return res
    