package shared

import "fmt"

// RBTreeNode ...
type RBTreeNode struct {
	red    bool
	key    string
	val    int
	left   *RBTreeNode
	right  *RBTreeNode
	parent *RBTreeNode
}

// NewTreeRoot ...
func NewTreeRoot() *RBTreeNode {
	root := newNode("", 0, nil)
	root.red = false

	return root
}

// Insert ...
func (r *RBTreeNode) Insert(key string, val int) {
	if key == "" {
		return
	}

	if r.key == "" {
		r.key = key
		r.val = val
		return
	}

	r.insert(key, val)
}

// Find ...
func (r *RBTreeNode) Find(key string) (int, error) {
	if r.key == key {
		return r.val, nil
	}

	if key < r.key && r.left != nil {
		return r.left.Find(key)
	}

	if key > r.key && r.right != nil {
		return r.right.Find(key)
	}

	return 0, fmt.Errorf("the key: %s is not found", key)
}

// Delete ...
func (r *RBTreeNode) Delete(key string) (int, error) {
	return r.findDel(key, nil)
}

func newNode(key string, val int, parent *RBTreeNode) *RBTreeNode {
	return &RBTreeNode{
		red:    true,
		key:    key,
		val:    val,
		left:   nil,
		right:  nil,
		parent: parent,
	}
}

func (r *RBTreeNode) insert(key string, val int) {
	// equal value, we're done.
	if r.key == key {
		r.val = val
		return
	}

	var temp, child *RBTreeNode

	if key < r.key {
		if r.left != nil {
			if key <= r.left.key {
				r.left.insert(key, val)
				return
			}

			// detach the subtree / leaf
			temp = r.left
			temp.parent = nil
		}

		child = newNode(key, val, r)

		// insert the node
		r.left = child
		child.left = temp
	} else {
		if r.right != nil {
			if key >= r.right.key {
				r.right.insert(key, val)
				return
			}

			// detach the subtree / leaf
			temp = r.right
			temp.parent = nil
		}

		child = newNode(key, val, r)

		// insert the node
		r.right = child
		child.right = temp
	}

	// update the parent to fully reattach
	if temp != nil {
		temp.parent = child
	}

	child.balance()
}

func (r *RBTreeNode) balance() {
	parent := r.parent
	if parent == nil {
		// r is root, and root is always black
		r.red = false
		return
	}

	if !parent.red {
		// parent is black, r is red, we're done
		return
	}

	gparent := parent.parent
	if gparent == nil {
		// parent is root, set its color to black (root is always black)
		parent.red = false
		return
	}

	var uncle *RBTreeNode
	if gparent.left == parent {
		uncle = gparent.right
	} else {
		uncle = gparent.left
	}

	// case 1
	if uncle.red {
		// flip parent and uncle, set gparent to red
		parent.red = false
		uncle.red = false
		gparent.red = true

		// now balance gparent
		gparent.balance()
		return
	}

	// case 2: uncle is black, left-left
	if parent == gparent.left && r == parent.left {
		gparent.red, parent.red = parent.red, gparent.red
		r.rightRotate(gparent, parent)
		return
	}

	// case 3: uncle is black, left-right
	if parent == gparent.left && r == parent.right {
		r.leftRotate(gparent, parent)
		parent.rightRotate(gparent, r)
		return
	}

	// case 4: uncle is black, right-left
	if parent == gparent.right && r == parent.right {
		gparent.red, parent.red = parent.red, gparent.red
		parent.leftRotate(parent.parent, gparent)
		return
	}

	// case 5: uncle is black, right-right
	gparent.right = r
	parent.left = r.right
	r.right = parent

	gparent.red, r.red = r.red, gparent.red
	r.leftRotate(gparent.parent, gparent)
}

func (r *RBTreeNode) rightRotate(gp, p *RBTreeNode) {
	//TODO: implementation is incorrect, in the sense that the "parent" node
	//      is not right

	temp := &RBTreeNode{
		red:    gp.red,
		key:    gp.key,
		val:    gp.val,
		right:  gp.right,
		left:   p.right,
		parent: p,
	}

	gp = p
	gp.right = temp
	gp.left = r
}

func (r *RBTreeNode) leftRotate(gp, p *RBTreeNode) {
	//TODO: implementation is incorrect, in the sense that the "parent" node
	//      is not right

	gp.left = r
	p.right = r.left
	r.left = p
}

func (r *RBTreeNode) findDel(key string, p *RBTreeNode) (int, error) {
	if r.key == key {
		r.delBalance(p)
		return r.val, nil
	}

	if key < r.key && r.left != nil {
		return r.left.findDel(key, r)
	}

	if key > r.key && r.right != nil {
		return r.right.findDel(key, r)
	}

	return 0, fmt.Errorf("the key: %s is not found", key)
}

func (r *RBTreeNode) delBalance(p *RBTreeNode) {

}

// Iterate ...
func (r *RBTreeNode) Iterate() map[int][]*RBTreeNode {
	store := make(map[int][]*RBTreeNode)
	return store
}
