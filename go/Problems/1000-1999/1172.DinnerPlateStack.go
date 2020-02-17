package problems

import (
	"fmt"

	d "../../Utils"
)

// DPS ...
type DPS struct {
	source    int
	output    int
	testCount int
}

// CreateDPS ...
func CreateDPS() *DPS {
	return &DPS{}
}

// Build ...
func (p *DPS) Build(test int) {
	p.ResetGlobals()
	p.testCount = 1

	switch test {
	default:
		p.source = 2
		p.output = 0

	}
}

var capacity int

// ResetGlobals ...
func (p *DPS) ResetGlobals() {
	capacity = 0
}

// Run ...
func (p *DPS) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				runDPS(p.source)
			} else {
				//runDPS(p.source)
			}
		}
	}
}

type stack struct {
	len  int
	vals []int
}

type node struct {
	pos   int
	left  *node
	right *node
}

type container struct {
	inner    []*stack
	nonFull  *node
	nonEmpty *node
}

func (c *container) push(val int) {
	idx := c.nonFull.findLeftNode()

	// fmt.Println("Insert to: ", idx)

	if idx == -1 {
		nextStack := &stack{
			len:  0,
			vals: make([]int, capacity),
		}

		nextStack.vals[0] = val
		nextStack.len++

		if nextStack.len < capacity {
			pos := len(c.inner)
			c.nonFull.insert(pos)
			c.nonEmpty.insert(pos)
		}

		c.inner = append(c.inner, nextStack)
		return
	}

	s := c.inner[idx]

	s.vals[s.len] = val
	s.len++

	if s.len == 1 {
		c.nonEmpty.insert(idx)
	}

	if s.len == capacity {
		c.nonFull = c.nonFull.remove(idx)
	}
}

func (c *container) pop() int {
	idx := c.nonEmpty.findRightNode()

	// fmt.Println("Pop from: ", idx)

	return c.popAtStack(idx)
}

func (c *container) popAtStack(idx int) int {
	if idx >= len(c.inner) || idx < 0 {
		return -1
	}

	s := c.inner[idx]
	if s.len == 0 {
		return -1
	}

	s.len--
	if s.len == 0 {
		c.nonEmpty = c.nonEmpty.remove(idx)
	}

	if s.len == capacity-1 {
		c.nonFull.insert(idx)
	}

	return s.vals[s.len]
}

func (root *node) remove(pos int) *node {
	var parent, child *node
	n, isLeft := root, false

	for {
		if pos == n.pos {
			if n.left != nil {
				child = n.left
			} else if n.right != nil {
				child = n.right
			} else {
				child = nil
			}

			if parent != nil {
				if isLeft {
					parent.left = child
				} else {
					parent.right = child
				}
			} else {
				if child != nil {
					return child
				}

				n.pos = -1
				return n
			}

			break
		}

		if pos < n.pos {
			// search left sub-tree
			if n.left != nil {
				parent = n
				isLeft = true
				n = n.left

				continue
			}

			// not found
			break
		}

		if pos > n.pos {
			if n.right != nil {
				parent = n
				isLeft = false
				n = n.right

				continue
			}

			break
		}
	}

	return root
}

func (root *node) insert(pos int) {
	if root.pos == -1 {
		root.pos = pos
		return
	}

	n := root
	for {
		// found in the tree, no need to insert
		if n.pos == pos {
			return
		}

		if pos < n.pos {
			if n.left != nil {
				n = n.left
				continue
			}

			n.left = &node{
				pos:   pos,
				left:  nil,
				right: nil,
			}

			return
		}

		if pos > n.pos {
			if n.right != nil {
				n = n.right
				continue
			}

			n.right = &node{
				pos:   pos,
				left:  nil,
				right: nil,
			}

			return
		}
	}
}

func (root *node) findRightNode() int {
	if root.pos == -1 {
		return -1
	}

	n := root
	for {
		if n.right != nil {
			n = n.right
			continue
		}

		break
	}

	return n.pos
}

func (root *node) findLeftNode() int {
	if root.pos == -1 {
		return -1
	}

	n := root
	for {
		if n.left != nil {
			n = n.left
			continue
		}

		break
	}

	return n.pos
}

func runDPS(cap int) {
	capacity = cap

	c := container{
		inner: make([]*stack, 0, cap),
		nonFull: &node{
			pos:   -1,
			left:  nil,
			right: nil,
		},
		nonEmpty: &node{
			pos:   -1,
			left:  nil,
			right: nil,
		},
	}

	c.push(1)
	c.push(2)
	c.push(3)
	c.push(4)
	c.push(5)

	if d.DEBUG {
		// initial stack states
		for i := range c.inner {
			s := c.inner[i]
			fmt.Println(s.vals)
		}
	}

	fmt.Println(c.popAtStack(0))

	c.push(20)
	c.push(21)

	fmt.Println(c.popAtStack(0))
	fmt.Println(c.popAtStack(2))

	fmt.Println(c.pop())
	fmt.Println(c.pop())
	fmt.Println(c.pop())
	fmt.Println(c.pop())
	fmt.Println(c.pop())
}
