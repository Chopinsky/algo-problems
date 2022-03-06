'''
You are given a 0-indexed binary string s which represents a sequence of train cars. s[i] = '0' denotes that the ith car does not contain illegal goods and s[i] = '1' denotes that the ith car does contain illegal goods.

As the train conductor, you would like to get rid of all the cars containing illegal goods. You can do any of the following three operations any number of times:

Remove a train car from the left end (i.e., remove s[0]) which takes 1 unit of time.
Remove a train car from the right end (i.e., remove s[s.length - 1]) which takes 1 unit of time.
Remove a train car from anywhere in the sequence which takes 2 units of time.
Return the minimum time to remove all the cars containing illegal goods.

Note that an empty sequence of cars is considered to have no cars containing illegal goods.

 

Example 1:

Input: s = "1100101"
Output: 5
Explanation: 
One way to remove all the cars containing illegal goods from the sequence is to
- remove a car from the left end 2 times. Time taken is 2 * 1 = 2.
- remove a car from the right end. Time taken is 1.
- remove the car containing illegal goods found in the middle. Time taken is 2.
This obtains a total time of 2 + 1 + 2 = 5. 

An alternative way is to
- remove a car from the left end 2 times. Time taken is 2 * 1 = 2.
- remove a car from the right end 3 times. Time taken is 3 * 1 = 3.
This also obtains a total time of 2 + 3 = 5.

5 is the minimum time taken to remove all the cars containing illegal goods. 
There are no other ways to remove them with less time.
Example 2:

Input: s = "0010"
Output: 2
Explanation:
One way to remove all the cars containing illegal goods from the sequence is to
- remove a car from the left end 3 times. Time taken is 3 * 1 = 3.
This obtains a total time of 3.

Another way to remove all the cars containing illegal goods from the sequence is to
- remove the car containing illegal goods found in the middle. Time taken is 2.
This obtains a total time of 2.

Another way to remove all the cars containing illegal goods from the sequence is to 
- remove a car from the right end 2 times. Time taken is 2 * 1 = 2. 
This obtains a total time of 2.

2 is the minimum time taken to remove all the cars containing illegal goods. 
There are no other ways to remove them with less time.
 

Constraints:

1 <= s.length <= 2 * 10^5
s[i] is either '0' or '1'.
'''


class Solution:
  def minimumTime(self, s: str) -> int:
    n = len(s)
    prefix = [i+1 for i in range(n)]
    suffix = [n-i for i in range(n)]
    
    # update the suffix array
    for i in range(n-1, -1, -1):
      if i == n-1:
        suffix[i] = int(s[i])
        continue
        
      if s[i] == '0':
        suffix[i] = suffix[i+1]
      else:
        suffix[i] = min(suffix[i], 2+suffix[i+1])
      
    for i in range(n):
      if i == 0:
        prefix[i] = int(s[i])
        continue
        
      if s[i] == '0':
        prefix[i] = prefix[i-1]
      
    min_time = min(prefix[-1], suffix[0])
    # print(min_time, prefix, suffix)
    
    for i in range(1, n):
      # print(i, prefix[i-1], suffix[i])
      min_time = min(min_time, prefix[i-1]+suffix[i])
      
    return min_time

  def minimumTime0(self, s: str) -> int:
    ans = len(s)
    ops = []
    
    for cart in s:
      ops.append(-1 if cart == '0' else 1)

    min_op = 0
    accu = 0
    
    for op in ops:
      accu += op
      min_op = min(min_op, accu)
      
      if accu > 0:
        accu = 0
        
    return ans + min_op
  