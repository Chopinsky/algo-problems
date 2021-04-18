'''
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

Example 1:

Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Example 3:

Input: matrix = [[904]], target = 0
Output: 0

Constraints:

1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
'''

class Solution:
  # Time complexity: O(MN^2)
  # 1) calculate prefix sum for each row
  # 2) then from col-i to col-j where j >= i, we calculate sum
  #    of sub-matrix (0, i, k, j) from (0, i, k-1, j) and prefix sum
  #    for row-k
  # 3) then the count of sub-matrix added to target equals the number
  #    of previously calculated sub-matrix that added to `currSum - target`
  # 4) add the currSum to the dict so we can keep track of the sums
  def numSubmatrixSumTarget(self, mat: List[List[int]], target: int) -> int:
    h, w = len(mat), len(mat[0])

    # calc each row's prefix sum for columns
    for i in range(h):
      for j in range(1, w):
        mat[i][j] += mat[i][j-1]

    ans = 0

    # for each column window [i, j] where j >= i, calculate matrix sum
    # for (0, i, k, j) where k is in [0, w); then we can know how many
    # submatrix exists for (k'+1, i, k, j) by looking at how many of the
    # (0, i, k', j) sums to `currSum - target`
    for i in range(w):
      for j in range(i, w):
        # dict to store prefix sums of the sub-matrix
        sumDict = collections.defaultdict(int)
        sumDict[0] = 1   # submatrix itself == 1 count
        currSum = 0

        for k in range(h):
          # get the current sub-matrix's total sum by adding the sum of the
          # cells in this row and between column [i, j]
          currSum += mat[k][j] - (mat[k][i-1] if i > 0 else 0)
          # get the number of the existing sub-matrix sums to the desired value
          ans += sumDict[currSum - target]
          # update the sub-marix sum's dict
          sumDict[currSum] += 1

    return ans


  def numSubmatrixSumTarget1(self, mat: List[List[int]], target: int) -> int:
    h, w = len(mat), len(mat[0])
    ans = 0

    dp = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
      row = 0
      for j in range(w):
        row += mat[i][j]
        dp[i][j] = dp[i-1][j] + row

        res = self.count(dp, target, i, j, h, w)
        # print(i, j, res, dp[i][j])
        ans += res

    # print(dp)

    return ans


  def count(self, dp: List[List[int]], target: int, x: int, y: int, h: int, w: int) -> int:
    base = dp[x][y]
    count = 1 if base == target else 0

    for j in range(y):
      if target == base - dp[x][j]:
        count += 1

    for i in range(x):
      if target == base - dp[i][y]:
        count += 1

    for i in range(x):
      for j in range(y):
        if target == base + dp[i][j] - dp[x][j] - dp[i][y]:
          count += 1

    return count
