'''
You are given an integer n representing the length of an unknown array that you are trying to recover. You are also given an array sums containing the values of all 2n subset sums of the unknown array (in no particular order).

Return the array ans of length n representing the unknown array. If multiple answers exist, return any of them.

An array sub is a subset of an array arr if sub can be obtained from arr by deleting some (possibly zero or all) elements of arr. The sum of the elements in sub is one possible subset sum of arr. The sum of an empty array is considered to be 0.

Note: Test cases are generated such that there will always be at least one correct answer.

 

Example 1:

Input: n = 3, sums = [-3,-2,-1,0,0,1,2,3]
Output: [1,2,-3]
Explanation: [1,2,-3] is able to achieve the given subset sums:
- []: sum is 0
- [1]: sum is 1
- [2]: sum is 2
- [1,2]: sum is 3
- [-3]: sum is -3
- [1,-3]: sum is -2
- [2,-3]: sum is -1
- [1,2,-3]: sum is 0
Note that any permutation of [1,2,-3] and also any permutation of [-1,-2,3] will also be accepted.
Example 2:

Input: n = 2, sums = [0,0,0,0]
Output: [0,0]
Explanation: The only correct answer is [0,0].
Example 3:

Input: n = 4, sums = [0,0,5,5,4,-1,4,9,9,-1,4,3,4,8,3,8]
Output: [0,-1,4,5]
Explanation: [0,-1,4,5] is able to achieve the given subset sums.

Constraints:

1 <= n <= 15
sums.length == 2n
-104 <= sums[i] <= 10^4
'''


from typing import List
from collections import Counter


class Solution:
  def recoverArray0(self, n: int, sums: List[int]) -> List[int]:
    result = []
    sums.sort()

    while len(sums) > 1:
      # either diff or -diff will be one of the numbers
      # in the original array
      diff = sums[-1] - sums[-2]
      counter = Counter(sums)

      # dividing the sums into 2 parts: if diff is the number,
      # then (diff, sum+diff) must be valid as well
      excluding = []
      including = []
      
      for val in sums:
        # the number is (over-)spent, skip
        if counter[val] <= 0:
          continue
          
        # divide the pair to different sets
        excluding.append(val)
        including.append(val+diff)
        counter[val] -= 1
        counter[val+diff] -= 1

      if 0 in excluding:
        # 0 in the excluding set and it's valid
        result.append(diff)
        sums = excluding
      else:
        # 0 in the including set and it's valid
        result.append(-1*diff)
        sums = including
        
    return result
      
      
  def recoverArray(self, n: int, sums: List[int]) -> List[int]:
    sums.sort()
    
    def iterate(arr: List[int], rem: int) -> List[int]:
      if rem == 1 and 0 in arr:
        return [max(arr, key=abs)]
      
      cand = []
      d = arr[-1] - arr[-2]
      
      for dr in [-1, 1]:
        cnt, sums_excl_d = Counter(arr), []
        diff = d * dr

        # illegal case -- should always have the empty array's sum,
        # aka 0, in the arr, otherwise this is not a legal test case,
        # so we just skip it
        if cnt[0] == 0:
          return []
        
        # finding pairs with greedy matching
        for num in arr[::dr]:
          # already used up, skip
          if cnt[num] <= 0:
            continue
          
          # can't find a pair, not the correct dir, stop
          if cnt[num+diff] == 0:
            break
            
          # found a pair, add to possible solution
          cnt[num] -= 1
          cnt[num+diff] -= 1
          sums_excl_d.append(num)
          
        # we shall have exactly 2^(rem-1) values left in the
        # sums_excl_d, otherwise we won't have an all-matching 
        # sums arr
        if len(sums_excl_d) == (1 << (rem-1)):
          nxt_cand = iterate(sums_excl_d[::dr], rem-1)
          nxt_cand.append(diff)
          
          if len(nxt_cand) > len(cand):
            cand = nxt_cand
        
      # print(cand)
      return cand
      
    return iterate(sums, n)
      