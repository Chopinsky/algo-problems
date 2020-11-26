package challenges

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func smallestFromLeaf(root *TreeNode) string {
	rel := make(map[*TreeNode]*TreeNode)
	rel[root] = nil

	zero := byte('a')
	nodes := findLeaf(root, rel, make([]*leaf, 0, 16), 0)
	chars := make([]byte, 0, len(nodes))

	var bestChar, rootChar byte

	// for _, n := range nodes {
	//   fmt.Println(n.node.Val, n.level)
	// }

	for len(nodes) > 0 {
		next := make([]*leaf, 0, len(nodes))
		bestChar = 0
		rootChar = 0

		for _, n := range nodes {
			if n == nil {
				continue
			}

			char := byte(n.node.Val) + zero
			if bestChar > 0 && char > bestChar {
				continue
			}

			if bestChar == 0 {
				bestChar = char
			}

			if char < bestChar {
				next = next[len(next):]
				rootChar = 0
				bestChar = char
			}

			if parent, ok := rel[n.node]; ok {
				if parent == nil {
					rootChar = char
				} else {
					n.node = parent
					next = append(next, n)
				}
			}
		}

		nodes = next
		chars = append(chars, bestChar)

		if rootChar > 0 && rootChar == bestChar {
			break
		}
	}

	// fmt.Println(chars)

	return string(chars)
}

func findLeaf(root *TreeNode, rel map[*TreeNode]*TreeNode, store []*leaf, level int) []*leaf {
	if root.Left == nil && root.Right == nil {
		last := len(store) - 1

		if last < 0 || root.Val <= store[last].node.Val {
			for last >= 0 {
				if root.Val < store[last].node.Val {
					last--
				}

				break
			}

			store = store[:(last + 1)]
			store = append(store, &leaf{
				node:  root,
				level: level,
			})
		}

		return store
	}

	if root.Left != nil {
		rel[root.Left] = root
		store = findLeaf(root.Left, rel, store, level+1)
	}

	if root.Right != nil {
		rel[root.Right] = root
		store = findLeaf(root.Right, rel, store, level+1)
	}

	return store
}

type leaf struct {
	node  *TreeNode
	level int
}
