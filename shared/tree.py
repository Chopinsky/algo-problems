class Tree:
  def __init__():
    self.root = None

  def insert(val: int):
    if not self.root:
      self.root = Node(val)
      return

    self.root.insert(val)


class Node:
  def __init__(self, val: int):
    self.val = val
    self.left = None
    self.right = None


  def insert(self, val: int):
    if self.val == val:
      return

    if val < self.val:
      if not self.left:
        self.left = Node(val)
        return

      self.left.insert(val)
    else:
      if not self.right:
        self.right = Node(val)
        return

      self.right.insert(val)


  def find(self, val: int) -> Optional[Node]:
    if self.val == val:
      return self

    if val < self.val:
      if not self.left:
        return None

      return self.left.find(val)

    if not self.right:
      return None

    return self.right.find(val)


  def floor(self, val: int) -> Optional[Node]:
    if self.val == val:
      return self

    if val < self.val:
      if not self.left:
        return None

      return self.left.floor(val)

    if not self.right:
      return self

    fnode = self.right.floor(val)
    if not fnode:
      return self

    return fnode


  def ceil(self, val: int) -> Optional[Node]:
    if self.val == val:
      return self

    if val > self.val:
      if not self.right:
        return None

      return self.right.ceil(val)

    cnode = self.left.ceil(val)
    if not cnode:
      return self

    return cnode
