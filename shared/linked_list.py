class Node:
  def __init__(self, val: int = 0):
    self.val = val
    self.next = None


  def attach(self, next: 'Node'):
    self.next = next


  def print(self):
    print(self.val, end=' -> ' if self.next else '\n')

    if self.next:
      self.next.print()


class TestLinkedList:
  @staticmethod
  def create_linked_list(count: int = 5):
    vals = [i for i in range(count)]
    head = None
    last = None

    for val in vals:
      node = Node(val)
      if not head:
        head = node

      if last:
        last.attach(node) 

      last = node

    return head

  
  @staticmethod
  def reverse_list(head: 'Node'):
    if not head:
      return None

    last = None
    curr = head

    while curr:
      # print('reversing:', curr.val)
      nxt = curr.next
      curr.next = last
      last = curr
      curr = nxt

    return last


  @staticmethod
  def print_chain(head: 'Node'):
    curr = head
    while curr:
      print(curr.val, end=' -> ' if curr.next else '\n')
      curr = curr.next


head = TestLinkedList.create_linked_list()
head.print()

new_head = TestLinkedList.reverse_list(head)
new_head.print()
