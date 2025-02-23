'''
3408-design-task-manager
'''

from typing import List
from heapq import heappush, heappop


class TaskManager:
  def __init__(self, tasks: List[List[int]]):
    self.users = {}
    self.priority = {}
    self.tasks = []
    
    for u, t, p in tasks:
      self.add(u, t, p)

  def check(self):
    print('init:', self.users, self.priority, self.tasks)

  def add(self, userId: int, taskId: int, priority: int) -> None:
    self.users[taskId] = userId
    self.priority[taskId] = priority
    heappush(self.tasks, (-priority, -taskId))
    # self.check()

  def edit(self, taskId: int, newPriority: int) -> None:
    if taskId not in self.priority or self.priority[taskId] == newPriority:
      return
  
    self.priority[taskId] = newPriority
    heappush(self.tasks, (-newPriority, -taskId))
    # self.check()

  def pop(self):
    def can_pop() -> bool:
      if not self.tasks:
        return False

      taskId = -self.tasks[0][1]
      if taskId not in self.users or taskId not in self.priority:
        return True

      if self.priority[taskId] != -self.tasks[0][0]:
        return True

      return False

    while can_pop():
      heappop(self.tasks)

  def rmv(self, taskId: int) -> None:
    if taskId not in self.users or taskId not in self.priority:
      return

    del self.users[taskId]
    del self.priority[taskId]
    self.pop()

  def execTop(self) -> int:
    self.pop()
    if not self.priority or not self.users or not self.tasks:
      return -1

    _, taskId = heappop(self.tasks)
    taskId = -taskId
    user = self.users[taskId]
    self.rmv(taskId)

    return user
    


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()