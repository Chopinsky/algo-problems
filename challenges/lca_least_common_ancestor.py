'''
Efficient algorithms to find Least Common Ancestor (LCA) between 2 nodes in a tree.

Multiple approaches:
1. Simple Recursive (O(n) per query)
2. Binary Lifting (O(n log n) preprocessing, O(log n) per query) - Best for multiple queries
3. Path-based (O(n) per query)
'''

from collections import defaultdict
from typing import List, Optional, Dict


class TreeNode:
    """Simple tree node representation"""
    def __init__(self, val: int):
        self.val = val
        self.children: List['TreeNode'] = []


class LCASimple:
    """
    Simple recursive approach for LCA.
    Time: O(n) per query
    Space: O(h) where h is height of tree
    Best for: Single or few queries
    """
    
    def __init__(self, root: TreeNode):
        self.root = root
    
    def find_lca(self, node1: int, node2: int) -> Optional[int]:
        """
        Find LCA of two nodes using simple recursive approach.
        
        Args:
            node1: First node value
            node2: Second node value
            
        Returns:
            LCA node value or None if not found
        """
        def dfs(node: TreeNode | None, target1: int, target2: int) -> tuple[bool, bool, Optional[int]]:
            """
            Returns: (found_target1, found_target2, lca_node)
            """
            if not node:
                return False, False, None
            
            found1 = (node.val == target1)
            found2 = (node.val == target2)
            
            # Search in children
            for child in node.children:
                f1, f2, lca = dfs(child, target1, target2)
                if lca is not None:
                    return True, True, lca

                found1 = found1 or f1
                found2 = found2 or f2
            
            # If both found at this node or in subtree, this is LCA
            if found1 and found2:
                return True, True, node.val

            return found1, found2, None
        
        _, _, lca = dfs(self.root, node1, node2)
        return lca


class LCABinaryLifting:
    """
    Binary Lifting approach for LCA.
    Time: O(n log n) preprocessing, O(log n) per query
    Space: O(n log n)
    Best for: Multiple queries (most efficient for many queries)
    """
    
    def __init__(self, n: int, edges: List[List[int]], root: int = 0):
        """
        Initialize LCA with binary lifting.
        
        Args:
            n: Number of nodes (0-indexed)
            edges: List of [u, v] edges
            root: Root node index
        """
        self.n = n
        self.log = (n).bit_length()  # log2(n) rounded up
        self.graph = defaultdict(list)
        self.root = root
        
        # Build graph
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        # Preprocessing arrays
        self.depth = [0] * n
        self.parent = [[-1] * self.log for _ in range(n)]
        
        # Build tree structure
        self._dfs(root, -1, 0)
        self._build_parents()
    
    def _dfs(self, u: int, parent: int, d: int):
        """DFS to compute depth and immediate parent"""
        self.depth[u] = d
        self.parent[u][0] = parent
        
        for v in self.graph[u]:
            if v != parent:
                self._dfs(v, u, d + 1)
    
    def _build_parents(self):
        """Build binary lifting table"""
        for k in range(1, self.log):
            for u in range(self.n):
                prev_parent = self.parent[u][k - 1]
                if prev_parent != -1:
                    self.parent[u][k] = self.parent[prev_parent][k - 1]
    
    def find_lca(self, u: int, v: int) -> int:
        """
        Find LCA of nodes u and v using binary lifting.
        
        Args:
            u: First node index
            v: Second node index
            
        Returns:
            LCA node index
        """
        # Make u the deeper node
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        
        # Lift u to same depth as v
        for k in range(self.log - 1, -1, -1):
            if self.depth[u] - (1 << k) >= self.depth[v]:
                u = self.parent[u][k]
        
        # If u == v, one is ancestor of the other
        if u == v:
            return u
        
        # Lift both nodes until their parents are the same
        for k in range(self.log - 1, -1, -1):
            if self.parent[u][k] != self.parent[v][k]:
                u = self.parent[u][k]
                v = self.parent[v][k]
        
        # Parent of u (or v) is the LCA
        return self.parent[u][0]
    
    def get_distance(self, u: int, v: int) -> int:
        """Get distance between two nodes"""
        lca = self.find_lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[lca]
    
    def kth_ancestor(self, u: int, k: int) -> int:
        """
        Find k-th ancestor of node u.
        Returns -1 if k-th ancestor doesn't exist.
        """
        if k > self.depth[u]:
            return -1
        
        for i in range(self.log):
            if k & (1 << i):
                u = self.parent[u][i]
                if u == -1:
                    return -1
        return u


class LCAPathBased:
    """
    Path-based approach for LCA.
    Time: O(n) per query
    Space: O(n)
    Best for: Understanding the concept, single queries
    """
    
    def __init__(self, n: int, edges: List[List[int]], root: int = 0):
        """
        Initialize LCA with path-based approach.
        
        Args:
            n: Number of nodes (0-indexed)
            edges: List of [u, v] edges
            root: Root node index
        """
        self.n = n
        self.graph = defaultdict[int, List[int]](list)
        self.root = root
        
        # Build graph
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
    
    def find_lca(self, u: int, v: int) -> int:
        """
        Find LCA by finding paths from root to both nodes.
        
        Args:
            u: First node index
            v: Second node index
            
        Returns:
            LCA node index
        """
        def get_path(node: int) -> List[int]:
            """Get path from root to node"""
            path = []
            parent_map = {}
            
            # Build parent map using BFS
            queue = [self.root]
            visited = {self.root}
            parent_map[self.root] = -1
            
            while queue:
                curr = queue.pop(0)
                if curr == node:
                    break

                for neighbor in self.graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        parent_map[neighbor] = curr
                        queue.append(neighbor)
            
            # Reconstruct path
            while node != -1:
                path.append(node)
                node = parent_map[node]
            
            return path[::-1]  # Reverse to get root-to-node path
        
        path_u = get_path(u)
        path_v = get_path(v)
        
        # Find last common node
        lca = self.root
        min_len = min(len(path_u), len(path_v))
        
        for i in range(min_len):
            if path_u[i] == path_v[i]:
                lca = path_u[i]
            else:
                break
        
        return lca


class LCATarjan:
    """
    Tarjan's offline LCA algorithm.
    Time: O(n + q) where q is number of queries
    Space: O(n)
    Best for: Multiple offline queries (all queries known in advance)
    """
    
    def __init__(self, n: int, edges: List[List[int]], root: int = 0):
        self.n = n
        self.graph = defaultdict[int, List[int]](list)
        self.root = root
        
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        self.parent = list[int](range(n))
        self.rank = [0] * n
        self.visited = [False] * n
        self.ancestor = list[int](range(n))
    
    def find(self, x: int) -> int:
        """Union-Find find with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int):
        """Union-Find union by rank"""
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
    
    def find_lca_offline(self, queries: List[tuple[int, int]]) -> Dict[tuple[int, int], int]:
        """
        Find LCA for all queries using Tarjan's algorithm.
        
        Args:
            queries: List of (u, v) query pairs
            
        Returns:
            Dictionary mapping (u, v) -> lca
        """
        # Build query list for each node
        query_map = defaultdict[int, List[int]](list)
        result = dict[tuple[int, int], int]()
        
        for u, v in queries:
            query_map[u].append(v)
            query_map[v].append(u)
            result[(u, v)] = -1
            result[(v, u)] = -1
        
        def dfs(u: int):
            self.visited[u] = True
            self.ancestor[u] = u
            
            for v in self.graph[u]:
                if not self.visited[v]:
                    dfs(v)
                    self.union(u, v)
                    self.ancestor[self.find(u)] = u
            
            # Process queries
            for v in query_map[u]:
                if self.visited[v]:
                    lca = self.ancestor[self.find(v)]
                    result[(u, v)] = lca
                    result[(v, u)] = lca
        
        dfs(self.root)

        return result


# Example usage and test cases
if __name__ == "__main__":
    # Example tree:
    #       0
    #      / \
    #     1   2
    #    /|\   \
    #   3 4 5   6
    #  /       / \
    # 7       8   9
    
    edges = [
        [0, 1], [0, 2],
        [1, 3], [1, 4], [1, 5],
        [2, 6],
        [3, 7],
        [6, 8], [6, 9]
    ]
    n = 10
    
    print("=== Binary Lifting LCA (Recommended for multiple queries) ===")
    lca_binary = LCABinaryLifting(n, edges, root=0)
    
    test_cases = [
        (7, 4),  # LCA should be 1
        (8, 9),  # LCA should be 6
        (7, 8),  # LCA should be 0
        (3, 5),  # LCA should be 1
        (1, 2),  # LCA should be 0
    ]
    
    for u, v in test_cases:
        lca = lca_binary.find_lca(u, v)
        dist = lca_binary.get_distance(u, v)
        print(f"LCA({u}, {v}) = {lca}, Distance = {dist}")
    
    print("\n=== Path-based LCA ===")
    lca_path = LCAPathBased(n, edges, root=0)
    for u, v in test_cases[:3]:
        lca = lca_path.find_lca(u, v)
        print(f"LCA({u}, {v}) = {lca}")
    
    print("\n=== Tarjan's Offline LCA ===")
    lca_tarjan = LCATarjan(n, edges, root=0)
    results = lca_tarjan.find_lca_offline(test_cases)
    for (u, v), lca in results.items():
        if u < v:  # Print each pair once
            print(f"LCA({u}, {v}) = {lca}")
