package shared

// Comparable ...
type Comparable interface {
	Compare(Comparable) int
}

// Color ...
type Color bool

// String ...
func (r Color) String() string {
	if r {
		return "Red"
	}

	return "Black"
}

const (
	// Red ...
	Red Color = false
	// Black ...
	Black Color = true
)

// TNode ...
type TNode struct {
	Left  *TNode
	Right *TNode
	Color Color
	Val   Comparable
}

// LLRBTree ...
type LLRBTree struct {
	Root  *TNode
	Count int
}

/* internal helper functions */
func (n *TNode) color() Color {
	if n == nil {
		return Black
	}

	return n.Color
}

func (n *TNode) leftRotate() *TNode {
	if n.Right == nil {
		return n
	}

	root := n.Right
	n.Right = root.Left
	root.Left = n

	root.Color = n.Color
	n.Color = Red

	return root
}

func (n *TNode) rightRotate() *TNode {
	if n.Left == nil {
		return n
	}

	root := n.Left
	n.Left = root.Right
	root.Right = n

	root.Color = n.Color
	n.Color = Red

	return root
}

func (n *TNode) flipColors() {
	n.Color = !n.Color

	if n.Left != nil {
		n.Left.Color = !n.Left.Color
	}

	if n.Right != nil {
		n.Right.Color = !n.Right.Color
	}
}

/* helper functions end */
