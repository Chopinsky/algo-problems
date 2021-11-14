'''
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Example 1:


Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
Example 3:

Input: firstList = [], secondList = [[4,8],[10,12]]
Output: []
Example 4:

Input: firstList = [[1,7]], secondList = [[3,10]]
Output: [[3,7]]
 

Constraints:

0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 10^9
endi < starti+1
0 <= startj < endj <= 10^9
endj < startj+1
'''


from typing import List


class Solution:
  def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
    if not first or not second:
      return []
    
    ans = []
    i, j = 0, 0
    m, n = len(first), len(second)
    
    while i < m and j < n:
      # print(i, j)
      
      if first[i][1] < second[j][0]:
        # ans.append(first[i])
        i += 1
        continue
        
      if second[j][1] < first[i][0]:
        # ans.append(second[j])
        j += 1
        continue
      
      s = max(first[i][0], second[j][0])
      
      if first[i][1] <= second[j][1]:
        e = first[i][1]
        if first[i][1] < second[j][1]:
          second[j][0] = first[i][1] + 1
        else:
          j += 1
          
        i += 1
        
      else:
        e = second[j][1]
        if second[j][1] < first[i][1]:
          first[i][0] = second[j][1] + 1
        else:
          i += 1
        
        j += 1
        
      ans.append([s, e])
        
    return ans
    