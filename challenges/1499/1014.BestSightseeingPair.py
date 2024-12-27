'''
You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

Example 1:

Input: values = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11

Example 2:

Input: values = [1,2]
Output: 2

Constraints:

2 <= values.length <= 5 * 10 ^ 4
1 <= values[i] <= 1000
'''


from typing import List


class Solution:
  def maxScoreSightseeingPair(self, values: List[int]) -> int:
    n = len(values)
    prev = values[-1] - (n-1)
    best = -float('inf')
    
    for i in range(n-2, -1, -1):
      best = max(best, values[i]+i+prev)
      prev = max(prev, values[i]-i)
    
    return best
        
  def maxScoreSightseeingPair(self, values: List[int]) -> int:
    high = 0
    best = 0
    
    for i, v in enumerate(values):
      if i == 0:
        high = values[0]
        continue
        
      pair = v - i + high
      best = max(best, pair)
      high = max(high, v+i)
      
    return best
  