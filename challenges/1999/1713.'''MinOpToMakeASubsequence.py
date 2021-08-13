from typing import List
from bisect import bisect_left

class Solution:
  '''
  idea is to find the longest increasing index in b, where the index
  refers to the index of the number appearing in a. 

  in the problem, we want to find a partial subsequence that appears in
  both a and b, and we want the subsequence to be the longest; to do that, 
  we can convert all numbers in b to the index of the same number in a, 
  and the subsequence of partial a in b must be an increasing index subsequence;
  so after conversion, we just need to find the LIS (longest increasing subsequence) 
  in the converted array.
  '''
  def minOperations(self, a: List[int], b: List[int]) -> int:
    # create the number to index mapping
    idx = {x: i for i, x in enumerate(a)}

    # convert numbers in b to indexs in a
    arr = [idx[x] if x in idx else -1 for x in b]

    # print(idx, arr)

    lis = []
    for num in arr:
      # number not found in a, skip
      if num < 0:
        continue

      # a new longest subsequence of indexs, update
      if not lis or num > lis[-1]:
        lis.append(num)
        continue

      # update the lis array
      idx = bisect_left(lis, num)
      lis[idx] = num

    # print(lis)

    # operations == a's length - longest common subsequence's length
    return len(a) - len(lis)

s = Solution()
ans = s.minOperations([6,4,8,1,3,2], [4,7,6,2,3,8,6,1])

print("Answer is:", ans)
