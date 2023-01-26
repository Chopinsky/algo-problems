'''
Maximum Subarray Sum

We define the following:

A subarray of array  of length  is a contiguous segment from  through  where .
The sum of an array is the sum of its elements.
Given an  element array of integers, , and an integer, , determine the maximum value of the sum of any of its subarrays modulo m.

Example


The following table lists all subarrays and their moduli:

		sum	%2
[1]		1	1
[2]		2	0
[3]		3	1
[1,2]		3	1
[2,3]		5	1
[1,2,3]		6	0
The maximum modulus is .

Function Description

Complete the maximumSum function in the editor below.

maximumSum has the following parameter(s):

long a[n]: the array to analyze
long m: the modulo divisor
Returns
- long: the maximum (subarray sum modulo )

Input Format

The first line contains an integer , the number of queries to perform.

The next  pairs of lines are as follows:

The first line contains two space-separated integers  and (long), the length of  and the modulo divisor.
The second line contains  space-separated long integers .
Constraints

 the sum of  over all test cases 
Sample Input

STDIN       Function
-----       --------
1           q = 1
5 7         a[] size n = 5, m = 7
3 3 9 9 5
'''

class Solution:
  '''
  the trick is that sum(a[:i]) % m always yield a maximum subarray sum after modulo,
  however, there is cases where sum(a[:i])% m < sum(a[:j])%m, where i > j, in which
  case the max modulo for subarray a[j+1:i+1] will be (sum(a[:i])%m + m - sum(a[:j])%m) and
  this can be the answer;

  solution is to check prefix_sums for all `i` in [0, n-1], then sort the prefix sums, 
  and check the neighboring prefix_sums (this will yield the max `ps_small + m - ps_large` value),
  and if the index of these two subarries reverse (i.e., i > j), meaning we need to apply the 
  fomula above to get the answer
  '''
  def maximumSum(a, m):
    if m == 1 or not a or len(a) == 0:
      return 0
    
    # Write your code here
    n = len(a)
    max_mod = 0
    prefix_sums = []
    
    for i in range(n):
      prefix_sums.append(((a[i] + (prefix_sums[-1][0] if i > 0 else 0)) % m, i))
      max_mod = max(max_mod, prefix_sums[i][0])
    
    prefix_sums.sort()
    # print(max_mod)
    
    for i in range(1, n):
      if prefix_sums[i][0] == prefix_sums[i-1][0] or prefix_sums[i-1][1] <= prefix_sums[i][1]:
        continue
      
      subarr_mod = (prefix_sums[i-1][0] + m - prefix_sums[i][0]) % m
      max_mod = max(max_mod, subarr_mod)
        
    return max_mod
