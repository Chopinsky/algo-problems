package p0

type graphNode struct {
	Val       int
	Neighbors []*graphNode
}

func cloneGraph(node *graphNode) *graphNode {
	if node == nil {
		return nil
	}

	group := make(map[int]*graphNode)
	stack := make([]*graphNode, 0, 101)
	stack = append(stack, node)

	var head, top, curr, nextNode *graphNode
	var visited bool

	for len(stack) > 0 {
		top, stack = stack[0], stack[1:]

		// fmt.Println("visiting", top.Val, top.Neighbors, visited[top.Val])

		if n, ok := group[top.Val]; ok {
			curr = n
		} else {
			curr = createNode(top.Val, group)
		}

		if head == nil {
			head = curr
		}

		for _, next := range top.Neighbors {
			if top.Val < next.Val {
				// fmt.Println("Building:", top.Val, "<->", next.Val)

				if n, ok := group[next.Val]; ok {
					nextNode = n
					visited = true
				} else {
					nextNode = createNode(next.Val, group)
					visited = false
				}

				nextNode.Neighbors = append(nextNode.Neighbors, curr)
				curr.Neighbors = append(curr.Neighbors, nextNode)

				if !visited {
					stack = append(stack, next)
				}
			}
		}
	}

	return head
}

func createNode(val int, group map[int]*graphNode) *graphNode {
	node := &graphNode{
		Val:       val,
		Neighbors: make([]*graphNode, 0, 100),
	}

	group[val] = node

	return node
}
