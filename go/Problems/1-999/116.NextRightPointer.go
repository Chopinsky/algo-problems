package problems

import (
	"fmt"
)

// NRP ...
type NRP struct {
	source    []int
	output    int
	testCount int
}

// CreateNRP ...
func CreateNRP() *NRP {
	return &NRP{}
}

// Build ...
func (p *NRP) Build(test int) {
	p.ResetGlobals()
	p.testCount = 1

	switch test {
	default:
		p.source = []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
		p.output = 0

	}
}

// ResetGlobals ...
func (p *NRP) ResetGlobals() {
}

// Run ...
func (p *NRP) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				printTree(calcNRP(p.source))
			} else {
				calcNRP(p.source)
			}
		}
	}
}

func calcNRP(tree []int) *treeNode {
	root := buildTree(tree, 0, len(tree))

	connTree(root, 0, make(map[int]*treeNode))

	return root
}

func printTree(root *treeNode) {
	tree := make(map[int][]*treeNode)
	level := 0

	iterTree(root, level, tree)

	for {
		if nodes, ok := tree[level]; ok {
			fmt.Println("\n>>>>> At level", level, "<<<<<")
			level++

			for i := range nodes {
				n := nodes[i]
				str := fmt.Sprintf("node: %d ", n.val)

				if n.next != nil {
					str += fmt.Sprintf("next node: %d", n.next.val)
				} else {
					str += fmt.Sprintf("next node: nil")
				}

				fmt.Println(str, ";")
			}

			continue
		}

		break
	}
}

func iterTree(root *treeNode, level int, store map[int][]*treeNode) {
	store[level] = append(store[level], root)

	if root.left != nil {
		iterTree(root.left, level+1, store)
	}

	if root.right != nil {
		iterTree(root.right, level+1, store)
	}
}

type treeNode struct {
	val   int
	left  *treeNode
	right *treeNode
	next  *treeNode
}

func buildTree(tree []int, rootIdx, size int) *treeNode {
	root := &treeNode{
		val:   tree[rootIdx],
		left:  nil,
		right: nil,
		next:  nil,
	}

	leftIdx, rightIdx := 2*rootIdx+1, 2*rootIdx+2

	if leftIdx < size {
		root.left = buildTree(tree, leftIdx, size)
	}

	if rightIdx < size {
		root.right = buildTree(tree, rightIdx, size)
	}

	return root
}

func connTree(root *treeNode, level int, store map[int]*treeNode) {
	if last, ok := store[level]; ok {
		last.next = root
	}

	store[level] = root

	if root.left != nil {
		connTree(root.left, level+1, store)
	}

	if root.right != nil {
		connTree(root.right, level+1, store)
	}
}
