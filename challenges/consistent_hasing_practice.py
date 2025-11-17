from hashlib import md5
from bisect import bisect_left, insort


def hash_node(key: str) -> int:
  return int(md5(key.encode("utf-8")).hexdigest(), 16)
  

class ConsistentHash:
  def __init__(self, initial_nodes=None):
    self.ring = []
    self.node_map = {}

    if initial_nodes:
      for node in initial_nodes:
        self.add(node)

  def add(self, key: str):
    h = hash_node(key)
    self.node_map[h] = key
    insort(self.ring, h)

  def remove(self, key: str):
    h = hash_node(key)
    if h in self.node_map:
      del self.node_map[h]
      self.ring.remove(h)

  def get_node_name(self, key: str) -> str:
    if not self.ring:
      raise Exception("No nodes available")

    h = hash_node(key)

    # Binary search for the closest node
    idx = bisect_left(self.ring, h)
    if idx == len(self.ring):
      idx = 0  # Wrap around

    return self.node_map[self.ring[idx]]
  