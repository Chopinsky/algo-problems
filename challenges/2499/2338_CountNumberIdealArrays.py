'''
You are given two integers n and maxValue, which are used to describe an ideal array.

A 0-indexed integer array arr of length n is considered ideal if the following conditions hold:

Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
Every arr[i] is divisible by arr[i - 1], for 0 < i < n.
Return the number of distinct ideal arrays of length n. Since the answer may be very large, return it modulo 109 + 7.

Example 1:

Input: n = 2, maxValue = 5
Output: 10
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (5 arrays): [1,1], [1,2], [1,3], [1,4], [1,5]
- Arrays starting with the value 2 (2 arrays): [2,2], [2,4]
- Arrays starting with the value 3 (1 array): [3,3]
- Arrays starting with the value 4 (1 array): [4,4]
- Arrays starting with the value 5 (1 array): [5,5]
There are a total of 5 + 2 + 1 + 1 + 1 = 10 distinct ideal arrays.

Example 2:

Input: n = 5, maxValue = 3
Output: 11
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (9 arrays): 
   - With no other distinct values (1 array): [1,1,1,1,1] 
   - With 2nd distinct value 2 (4 arrays): [1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2]
   - With 2nd distinct value 3 (4 arrays): [1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3]
- Arrays starting with the value 2 (1 array): [2,2,2,2,2]
- Arrays starting with the value 3 (1 array): [3,3,3,3,3]
There are a total of 9 + 1 + 1 = 11 distinct ideal arrays.

Constraints:

2 <= n <= 10^4
1 <= maxValue <= 10^4
'''

from collections import defaultdict
from math import comb


class Solution:
  '''
  this problem is complex, because it's built from 2 sub-problems:
  1) count the number of strictly increamental digits at length n, and
  2) count the number of ways to place n digits in an array of length m

  first, we need to generate the number of ways to create an array of length-n,
  and its elements are increamental, and also arr[i]%arr[i-1] == 0; we only 
  care about the last number in each of these arrays, so we can increamentally
  build the array counter based on the last digit of such arrays;

  next, we need to find n indexs from an array of m, such that each uniq number will 
  occupy array from such index till next number's index (i.e. a continuous subarray
  filled with only this number); since the 1st number should always be at index-0, the
  problem reduces to find (n-1) indexs from (m-1) choices.

  finally, compound problem-1 and problem-2, we will reach the final answer; the real tricky
  part is that we should realize that for max_value = 10000, the longest array with
  unique numbers has a length of 14, i.e. 2^13 < 10000 < 2^14. 
  '''
  def idealArrays(self, n: int, maxValue: int) -> int:
    if maxValue == 1:
      return 1
    
    '''
    Part-1: find the number of ways to construct array of length n, and
            all digits in the array is increamental and arr[i]%arr[i-1] == 0
    '''
    mod, ln = 10**9 + 7, 1
    uniq_arr_counter = defaultdict(int)
    uniq_arr_counter[1] = maxValue
    tail_digit_arr, nxt_arr = defaultdict(int), defaultdict(int)
    
    for i in range(maxValue):
      tail_digit_arr[i+1] = 1
    
    # build the count of strictly increamental array, with the
    # last digit ending as `d0` and length of `ln+1`
    while ln < n and tail_digit_arr:
      for d, c in tail_digit_arr.items():
        for d0 in range(d+d, maxValue+1, d):
          nxt_arr[d0] = (nxt_arr[d0] + c) % mod
          
      tail_digit_arr, nxt_arr = nxt_arr, tail_digit_arr
      nxt_arr.clear()
      ln += 1
      
      if tail_digit_arr:
        uniq_arr_counter[ln] = sum(tail_digit_arr.values())
        
    '''
    Part-2: find number of ways to place n-digits in an array of length m,
            then compound the ways of obtaining these n-digits to get the
            final answer
    '''
    
    # now the problem has become: how to choose `ln-1` index from
    # an array of length `n-1`, i.e. we want to count the number
    # of ways to generate the index of the first digit in the array:
    #    d0: 0, d(1): x1, d(2): x2, ..., d(ln): xln, 
    # where x1, x2, ..., xln can be any number from [1, n], and
    # for each length `ln`, and with `cnt` ways of uniq digits in 
    # an array of this length.
    count = 0
    for ln, cnt in uniq_arr_counter.items():
      count = (count + comb(n-1, ln-1) * cnt) % mod
      
    return count
    