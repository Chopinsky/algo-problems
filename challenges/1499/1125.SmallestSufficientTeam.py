'''
In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.

Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.

It is guaranteed an answer exists.

Example 1:

Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]

Example 2:

Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]
'''


from typing import List, Tuple
from functools import lru_cache


class Solution:
  def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
    n = len(people)
    skill_id = { s: i for i, s in enumerate(req_skills)}
    
    skills = [0] * n
    for i, ps in enumerate(people):
      for s in ps:
        if s in skill_id:
          skills[i] |= (1 << skill_id[s])
    
    prefix_skills = [skills[i] for i in range(n)]
    for i in range(n-2, -1, -1):
      prefix_skills[i] |= prefix_skills[i+1]
    
    # print(skill_id)
    # print('skills', skills)
    
    @lru_cache(None)
    def dp(i: int, req: int) -> Tuple[int, int]:
      # out of the bound, or the remainder teams won't fulfil the requirements
      if i >= n or (req ^ (req & prefix_skills[i]) > 0):
        return (0, 0)
      
      # this person has all the remainder required skills for the team,
      # just add the person and done
      if skills[i] & req == req:
        return (1<<i, 1)
      
      # the person doesn't have the needed skills
      if skills[i] & req == 0:
        return dp(i+1, req)

      t0, c0 = dp(i+1, req ^ (req & skills[i]))
      t1, c1 = dp(i+1, req)
      # print("rec", i, req, c0, t0, c1, t1)
      
      if (not c1) or (c0 > 0 and c0+1 <= c1):
        return (t0|(1<<i), c0+1)
      
      return (t1, c1)
      
    min_team, _ = dp(0, (1 << len(req_skills)) - 1)
    # print("{0:b}".format(min_team))
    team = []
    
    for i in range(n):
      if min_team & (1 << i) > 0:
        team.append(i)
    
    return team
  