'''
You are given a string num representing the digits of a very large integer and an integer k. You are allowed to swap any two adjacent digits of the integer at most k times.

Return the minimum integer you can obtain also as a string.

Example 1:

Input: num = "4321", k = 4
Output: "1342"
Explanation: The steps to obtain the minimum integer from 4321 with 4 adjacent swaps are shown.
Example 2:

Input: num = "100", k = 1
Output: "010"
Explanation: It's ok for the output to have leading zeros, but the input is guaranteed not to have any leading zeros.
Example 3:

Input: num = "36789", k = 1000
Output: "36789"
Explanation: We can keep the number without any swaps.
 

Constraints:

1 <= num.length <= 3 * 10^4
num consists of only digits and does not contain leading zeros.
1 <= k <= 10^4
'''


from heapq import heappush, heappop


class Solution:
  def minInteger0(self, num: str, k: int) -> str:
    def build(num: str, k: int) -> str:
      if k <= 0:
        return num

      n = len(num)
      if k >= n*(n-1)//2: 
        return "".join(sorted(list(num)))

      # for each number, find the first index
      for val in range(10):
        idx = num.find(str(val))
        if 0 <= idx <= k:
          return str(num[idx]) + build(num[0:idx] + num[idx+1:], k-idx)

    return build(num, k)


  def minInteger(self, num: str, k: int) -> str:
    n = len(num)
    stack = []
    fenwick = [0] * (n+1)
    
    def update(idx: int): 
      idx += 1
      while idx < len(fenwick):
        fenwick[idx] += 1
        idx += (idx & -idx)
      
    def query(idx: int) -> int:
      total = 0
      while idx > 0:
        total += fenwick[idx]
        idx -= (idx & -idx)
      
      return total
    
    last = min(k+1, n)
    for i in range(last):
      heappush(stack, (num[i], i))
      
    popped = []
    seen = set()
    ans = ''
    
    while stack and k > 0:
      _, idx = heappop(stack)
      shift = idx - query(idx)
      
      if last < n and (shift == 0 or shift > k):
        heappush(stack, (num[last], last))
        last += 1
        
      if shift > k:
        heappush(popped, idx)
        continue
      
      # store.append(idx)
      ans += num[idx]
      seen.add(idx)
      update(idx)
      k -= shift
      
      # move any popped but inbound back into 
      # candidate stack
      while popped:
        idx = popped[0]
        shift = idx - query(idx)
        if shift > k:
          break
          
        heappop(popped)
        heappush(stack, (num[idx], idx))
      
      # print(num[idx], k, stack)
      
    for i in range(n):
      if i in seen:
        continue
        
      ans += num[i]
      
    return ans
    