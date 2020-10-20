package challenges

import (
	"fmt"
	"strconv"
	"strings"
)

// Node ...
type Node struct {
	Val       int
	Neighbors []*Node
}

/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Neighbors []*Node
 * }
 */

func cloneGraph(node *Node) *Node {
	if node == nil {
		return node
	}

	return makeGraph(node, make(map[int]*Node), make(map[string]bool))
}

func makeGraph(root *Node, cache map[int]*Node, edges map[string]bool) *Node {
	next := clone(root)
	cache[next.Val] = next

	if len(root.Neighbors) == 0 {
		return next
	}

	for _, n := range root.Neighbors {
		k := toNodeKey(root.Val, n.Val)

		// the edge has already been created
		if edges[k] {
			continue
		}

		// the node already exists
		if another, ok := cache[n.Val]; ok {
			another.Neighbors = append(another.Neighbors, next)
			next.Neighbors = append(next.Neighbors, another)
			edges[k] = true
			continue
		}

		// not created yet
		makeGraph(n, cache, edges)
	}

	return next
}

func clone(node *Node) *Node {
	return &Node{
		Val:       node.Val,
		Neighbors: make([]*Node, 0, len(node.Neighbors)),
	}
}

func toNodeKey(i, j int) string {
	if i > j {
		i, j = j, i
	}

	return fmt.Sprintf("%d,%d", i, j)
}

func fromKey(key string) (int, int) {
	keys := strings.Split(key, ",")
	i, _ := strconv.Atoi(keys[0])
	j, _ := strconv.Atoi(keys[1])
	return i, j
}
