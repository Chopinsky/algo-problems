'''
There is a pizza with 3n slices of varying size, you and your friends will take slices of pizza as follows:

You will pick any pizza slice.
Your friend Alice will pick next slice in anti clockwise direction of your pick. 
Your friend Bob will pick next slice in clockwise direction of your pick.
Repeat until there are no more slices of pizzas.
Sizes of Pizza slices is represented by circular array slices in clockwise direction.

Return the maximum possible sum of slice sizes which you can have.

Example 1:

Input: slices = [1,2,3,4,5,6]
Output: 10
Explanation: Pick pizza slice of size 4, Alice and Bob will pick slices with size 3 and 5 respectively. Then Pick slices with size 6, finally Alice and Bob will pick slice of size 2 and 1 respectively. Total = 4 + 6.

Example 2:

Input: slices = [8,9,8,6,1,1]
Output: 16
Output: Pick pizza slice of size 8 in each turn. If you pick slice with size 9 your partners will pick slices of size 8.

Example 3:

Input: slices = [4,1,2,5,8,3,1,9,7]
Output: 21

Example 4:

Input: slices = [3,1,2]
Output: 3
 

Constraints:

1 <= slices.length <= 500
slices.length % 3 == 0
1 <= slices[i] <= 1000
'''

class Solution:
  def maxSizeSlices(self, slices: List[int]) -> int:
    @lru_cache(None)
    def dp(i: int, j: int, rem: int) -> int:
      if rem == 0:
        return 0
      
      if rem == 1:
        return max(slices[i:j+1])
      
      # won't have enough pieces left to finish
      # the required amount
      if j-i+1 < 2*rem-1:
        return -1
      
      return max(
        # if we take pizza at j
        slices[j] + dp(i, j-2, rem-1),  
        # if we don't take pizza at j, take all 
        # remainders from the nums[i:j-1] range
        dp(i, j-1, rem),                
      )
      
    ln = len(slices)
    pieces = ln//3
    
    return max(
      # edge case: take last piece, excluding the 1st piece as it's
      # taking by alice
      dp(1, ln-3, pieces-1) + slices[-1],
      # don't take the last piece, take `pieces` from the remainder
      # of the array
      dp(0, ln-2, pieces)
    )
      
  
  def maxSizeSlices1(self, slices: List[int]) -> int:
    memo = {}
    
    def pick(s: List[int]) -> int:
      if not s:
        return 0
      
      if len(s) == 3:
        return max(s)
      
      key = ""
      for n in s:
        key += f'{n},'
        
      if key in memo:
        return memo[key]
      
      best = 0
      ln = len(s)
      
      for i in range(ln):
        if s[i] <= s[(i+1)%ln] and s[i] <= s[i-1]:
          continue
        
        if i == 0:
          best = max(best, s[i]+pick(s[2:-1]))
          continue
          
        if i == len(s)-1:
          best = max(best, s[i]+pick(s[1:-2]))
          continue
          
        best = max(best, s[i]+pick(s[:i-1]+s[i+2:]))
      
      memo[key] = best
      return best
      
    return pick(slices)
  
