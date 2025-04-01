'''
You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.

For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
Return the maximum points you can earn for the exam.

Example 1:

Input: questions = [[3,2],[4,3],[4,4],[2,5]]
Output: 5
Explanation: The maximum points can be earned by solving questions 0 and 3.
- Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
- Unable to solve questions 1 and 2
- Solve question 3: Earn 2 points
Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.
Example 2:

Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
Output: 7
Explanation: The maximum points can be earned by solving questions 1 and 4.
- Skip question 0
- Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
- Unable to solve questions 2 and 3
- Solve question 4: Earn 5 points
Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.
 

Constraints:

1 <= questions.length <= 10^5
questions[i].length == 2
1 <= pointsi, brainpoweri <= 10^5
'''

from typing import List


class Solution:
  def mostPoints(self, questions: List[List[int]]) -> int:
    n = len(questions)
    dp = [0]*n

    for i in range(n-1, -1, -1):
      point, skip_count = questions[i]
      skip = 0 if i == n-1 else dp[i+1]
      solve = point + (dp[i+skip_count+1] if i+skip_count+1 < n else 0)
      dp[i] = max(skip, solve)

    return dp[0]
        
  def mostPoints(self, questions: List[List[int]]) -> int:
    n = len(questions)
    dp = [0]*n
    
    for i in range(n-1, -1, -1):
      p, d = questions[i]
      last = dp[i+1] if i < n-1 else 0
      jumps = dp[i+d+1] if i+d+1 < n else 0
      dp[i] = max(last, p+jumps)
    
    # print(dp)
    return dp[0]


  def mostPoints(self, questions: List[List[int]]) -> int:
    n = len(questions)
    points = [0] * n
    
    for i in range(n-1, -1, -1):
      p, b = questions[i]
      past = points[i+1] if i < n-1 else 0
      curr = p + (0 if i+b+1 >= n else points[i+b+1])
      points[i] = max(past, curr)
      
    # print(points)
    return max(points)
    