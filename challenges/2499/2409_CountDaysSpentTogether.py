'''
2409. Count Days Spent Together

Alice and Bob are traveling to Rome for separate business meetings.

You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.

Return the total number of days that Alice and Bob are in Rome together.

You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

Example 1:

Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
Output: 3
Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.
Example 2:

Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
Output: 0
Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.

Constraints:

All dates are provided in the format "MM-DD".
Alice and Bob's arrival dates are earlier than or equal to their leaving dates.
The given dates are valid dates of a non-leap year.
'''


class Solution:
  def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
    def parse(s):
      dates = s.split('-')
      return int(dates[0]), int(dates[1])
    
    m1, d1 = parse(arriveAlice)
    m2, d2 = parse(leaveAlice)
    m3, d3 = parse(arriveBob)
    m4, d4 = parse(leaveBob)
    
    if m3 > m2 or (m3 == m2 and d3 > d2):
      return 0
    
    if m1 > m4 or (m4 == m1 and d1 > d4):
      return 0
    
    if m1 > m3 or (m1 == m3 and d1 > d3):
      am, ad = m1, d1
    else:
      am, ad = m3, d3
      
    if m2 < m4 or (m2 == m4 and d2 < d4):
      lm, ld = m2, d2
    else:
      lm, ld = m4, d4
    
    # print(am, ad, lm, ld)
    if am == lm:
      return ld-ad+1
    
    days = 0
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for m in range(am, lm+1):
      if m == am:
        days += months[m-1]-ad+1
        
      elif m == lm:
        days += ld
        
      else:
        days += months[m-1]
      
    return days
    