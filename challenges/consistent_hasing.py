import hashlib
import bisect


def hash_value(key: str) -> int:
    """Return a 32-bit hash of a string."""
    return int(hashlib.md5(key.encode("utf-8")).hexdigest(), 16)


class ConsistentHashRing:
    def __init__(self, replicas=100):
        """
        replicas = number of virtual nodes per real node.
        More replicas => better distribution but more memory.
        """
        self.replicas = replicas
        self.ring = []          # sorted list of hash points
        self.nodes = {}         # hash point -> node_name

    def add_node(self, node_name: str):
        """Add a node with multiple virtual replicas."""
        for i in range(self.replicas):
            v_node_key = f"{node_name}#{i}"
            h = hash_value(v_node_key)
            self.nodes[h] = node_name
            bisect.insort(self.ring, h)

    def remove_node(self, node_name: str):
        """Remove node and its virtual replicas."""
        to_remove = []
        for h, n in self.nodes.items():
            if n == node_name:
                to_remove.append(h)

        for h in to_remove:
            del self.nodes[h]
            self.ring.remove(h)

    def get_node(self, key: str) -> str:
        """Return the node responsible for a given key."""
        if not self.ring:
            raise Exception("No nodes in the ring")

        h = hash_value(key)
        pos = bisect.bisect(self.ring, h)

        # Wrap around the ring
        if pos == len(self.ring):
            pos = 0

        h_node = self.ring[pos]
        return self.nodes[h_node]


ring = ConsistentHashRing(replicas=50)

# Add nodes
ring.add_node("nodeA")
ring.add_node("nodeB")
ring.add_node("nodeC")

# Get which node stores a key
print(ring.get_node("user:12345"))
print(ring.get_node("order:9981"))

# Add a new node → minimal key movement
ring.add_node("nodeD")
print("After adding nodeD:")
print(ring.get_node("user:12345"))
print(ring.get_node("order:9981"))

