'''
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

Example 2:

Input: arr = [1,1,1,1,1]
Output: 10

Example 3:

Input: arr = [2,3]
Output: 0

Example 4:

Input: arr = [1,3,5,7,9]
Output: 3

Example 5:

Input: arr = [7,11,12,9,5,2,7,17,22]
Output: 8
 

Constraints:

1 <= arr.length <= 300
1 <= arr[i] <= 10^8
'''


from typing import List
from collections import defaultdict


class Solution:
  '''
  the idea is for arr[i:j] whose XOR sum is 0, any (i, j, k) will form the 2 arrays
  that has the same XOR sums; then we only need to count how many prefix XOR sums
  we have gotten so far, and add the index diffs to the total counts
  '''
  def countTriplets(self, arr: List[int]) -> int:
    prefix = [0]
    n = len(arr)
    
    for i in range(n):
      prefix.append(prefix[-1] ^ arr[i])
      
    count = defaultdict(int)
    total = defaultdict(int)
    ans = 0
    
    for i in range(n+1):
      val = prefix[i]
      if i > 1:
        ans += count[val] * (i-1) - total[val]
        
      count[val] += 1
      total[val] += i
    
    return ans
  
  
  def countTriplets0(self, arr: List[int]) -> int:
    prexor = [0]
    n = len(arr)
    
    for i in range(n):
      prexor.append(prexor[-1] ^ arr[i])
      
    count = 0
    
    for i in range(n-1):
      for j in range(i+1, n):
        a = prexor[j] ^ prexor[i]
        for k in range(j, n):
          b = arr[j] if j == k else prexor[k+1] ^ prexor[j]
          if a == b:
            # print(a, b, i, j, k)
            count += 1
    
    return count
    