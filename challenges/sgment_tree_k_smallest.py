import sys
from typing import List

# Increase recursion limit for deep recursion in tree construction
sys.setrecursionlimit(2000)

class Node:
    def __init__(self, count=0, left=None, right=None):
        self.count = count
        self.left = left
        self.right = right


class PersistentSegmentTree:
    def __init__(self, arr: List[int]):
        # 1. Coordinate Compression and Mapping
        self.original_values = sorted(list(set(arr)))
        self.val_to_rank = {val: i for i, val in enumerate(self.original_values)}
        self.max_rank = len(self.original_values)
        self.roots = [None] * (len(arr) + 1)
        
        # 2. Build Persistent Trees (Prefix Frequency)
        self.roots[0] = self._build_empty_tree(0, self.max_rank - 1)
        
        for i, val in enumerate(arr):
            rank = self.val_to_rank[val]
            # Create a new root from the previous one, inserting the new element's rank
            self.roots[i + 1] = self._update(self.roots[i], 0, self.max_rank - 1, rank, 1)

    def _build_empty_tree(self, start, end):
        """Creates a skeletal Segment Tree node."""
        if start > end:
            return None

        node = Node()
        if start != end:
            mid = (start + end) // 2
            node.left = self._build_empty_tree(start, mid)
            node.right = self._build_empty_tree(mid + 1, end)

        return node
    
    def _update(self, prev_node, start, end, idx, diff):
        """Creates a new node by copying and updating the path from the previous tree."""
        if start > end:
            return None
            
        # Create a new node by copying the old one's data
        new_node = Node(prev_node.count + diff) 
        
        if start == end:
            return new_node
        
        mid = (start + end) // 2
        
        if idx <= mid:
            # New left node, right node remains a link to the previous tree's right node
            new_node.left = self._update(prev_node.left if prev_node.left else self._build_empty_tree(start, mid), 
                                         start, mid, idx, diff)
            new_node.right = prev_node.right if prev_node.right else self._build_empty_tree(mid + 1, end)
        else:
            # New right node, left node remains a link to the previous tree's left node
            new_node.left = prev_node.left if prev_node.left else self._build_empty_tree(start, mid)
            new_node.right = self._update(prev_node.right if prev_node.right else self._build_empty_tree(mid + 1, end), 
                                          mid + 1, end, idx, diff)
        return new_node

    def query_kth(self, l: int, r: int, k: int):
        """Finds the k-th smallest element (1-indexed) in the range A[l:r]."""
        # The query range is A[l...r]. The frequencies are T[r+1] - T[l].
        # T[r+1] is root (r+1), T[l] is root (l)
        
        # k is the 1-based rank, for median (odd size N) k = (N // 2) + 1
        
        # The first root (index 0) is an empty tree (prefix up to -1)
        root_r_plus_1 = self.roots[r + 1]
        root_l = self.roots[l]
        
        # Traverse both trees simultaneously
        return self._find_kth(root_l, root_r_plus_1, 0, self.max_rank - 1, k)

    def _find_kth(self, node_l, node_r, start, end, k):
        """Finds the k-th element by traversing the difference between two trees."""
        if start == end:
            # The rank is found. Return the original value.
            return self.original_values[start]
        
        mid = (start + end) // 2
        
        # Calculate the frequency count in the left child range [start, mid]
        # count_r - count_l gives the number of elements in range [l, r] with ranks in [start, mid]
        left_count = (node_r.left.count if node_r.left else 0) - (node_l.left.count if node_l.left else 0)
        
        if k <= left_count:
            # The k-th element is in the left sub-range (ranks start to mid)
            return self._find_kth(node_l.left, node_r.left, start, mid, k)
        else:
            # The k-th element is in the right sub-range (ranks mid+1 to end)
            # Subtract the count of the left sub-range from k
            return self._find_kth(node_l.right, node_r.right, mid + 1, end, k - left_count)

# --- Example Usage ---

arr = [1, 5, 2, 6, 3, 7, 4]
pst = PersistentSegmentTree(arr)

# Range query for the median: A[1] to A[5] (i.e., [5, 2, 6, 3, 7])
# Length of range is 5. Median rank k = (5 // 2) + 1 = 3rd smallest element.
l, r = 1, 5  # 0-indexed: arr[1] to arr[5] inclusive
N = r - l + 1
k_median = (N + 1) // 2

median_val = pst.query_kth(l, r, k_median)
print(f"Array: {arr}")
print(f"Range: A[{l}:{r}] = {arr[l:r+1]}")
print(f"Median (k={k_median}): {median_val}")

# Range query for 4th smallest element: A[0] to A[6] (entire array)
# Length is 7. k = 4th smallest element.
l, r = 0, 6
N = r - l + 1
k_fourth = 4
fourth_smallest = pst.query_kth(l, r, k_fourth)
print(f"\nRange: A[{l}:{r}] = {arr[l:r+1]}")
print(f"4th Smallest (k={k_fourth}): {fourth_smallest}")