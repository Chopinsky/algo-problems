'''
3686-Number-of-Stable-Subsequences
'''

from typing import List


class Solution:
  def countStableSubsequences(self, nums: List[int]) -> int:
    mod = 10**9 + 7
    ends_in_one_even = 0
    ends_in_two_evens = 0
    ends_in_one_odd = 0
    ends_in_two_odds = 0

    for num in nums:
      if num%2 == 0:
        new_one_even = (1 + ends_in_one_odd + ends_in_two_odds)
        new_two_evens = ends_in_one_even
        ends_in_one_even = (ends_in_one_even + new_one_even) % mod
        ends_in_two_evens = (ends_in_two_evens + new_two_evens) % mod
        
      else:
        new_one_odd = (1 + ends_in_one_even + ends_in_two_evens)
        new_two_odds = ends_in_one_odd
        ends_in_one_odd = (ends_in_one_odd + new_one_odd) % mod
        ends_in_two_odds = (ends_in_two_odds + new_two_odds) % mod

    return (ends_in_one_even + ends_in_two_evens + ends_in_one_odd + ends_in_two_odds) % mod

  def countStableSubsequences(self, nums: List[int]) -> int:
    mod = 10**9 + 7
    odd = [1, 0, 0]
    even = [0, 0, 0]

    for val in nums:
      if val%2 == 1:
        odd[2] += odd[1]
        odd[1] += (odd[0] + sum(even)) % mod
      else:
        even[2] += even[1]
        even[1] += (even[0] + sum(odd)) % mod

    return (sum(odd) + sum(even) - 1) % mod

      

        