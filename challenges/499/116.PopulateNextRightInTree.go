package challenges

// NextTreeNode ...
type NextTreeNode struct {
	Val   int
	Left  *NextTreeNode
	Right *NextTreeNode
	Next  *NextTreeNode
}

/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */

func connect(root *NextTreeNode) *NextTreeNode {
	walkNextTree(root, make(map[int]*NextTreeNode), 0)
	return root
}

func walkNextTree(root *NextTreeNode, stack map[int]*NextTreeNode, level int) {
	if root == nil {
		return
	}

	if node, ok := stack[level]; ok {
		node.Next = root
		stack[level] = root
	} else {
		stack[level] = root
	}

	walkNextTree(root.Left, stack, level+1)
	walkNextTree(root.Right, stack, level+1)
}
