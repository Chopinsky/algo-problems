package shared

// Node ...
type Node struct {
	Val       int
	Neighbors []*Node
}

func cloneGraph(node *Node) *Node {
	graph := make([]*Node, 101)

	stack := make([]*Node, 0, 101)
	stack = append(stack, node)

	head := createNode(node.Val)
	graph[node.Val] = head

	var curr, next, ne *Node

	for len(stack) > 0 {
		curr, stack = stack[0], stack[1:]
		val, n := curr.Val, curr.Neighbors

		if n == nil || len(n) == 0 {
			continue
		}

		clone := graph[val]
		if graph[val] != nil {
			continue
		}

		clone = createNode(val)

		for i := 0; i < len(n); i++ {
			ne = n[i]

			if graph[ne.Val] != nil {
				next = graph[ne.Val]
			} else {
				next = createNode(ne.Val)
				graph[ne.Val] = next
				stack = append(stack, ne)
			}

			// clone
			clone.Neighbors = append(clone.Neighbors, next)
		}
	}

	return head
}

func createNode(val int) *Node {
	return &Node{
		Val:       val,
		Neighbors: make([]*Node, 0, 100),
	}
}
