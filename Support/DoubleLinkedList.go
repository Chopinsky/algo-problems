package support

// Node ...
type Node struct {
	key   int
	value int
	freq  int
	prev  *Node
	next  *Node
}

// List ...
type List struct {
	head *Node
	tail *Node
}

// NewNode ...
func NewNode(key, val int) *Node {
	return &Node{
		key,
		val,
		1,
		nil,
		nil,
	}
}

// SetValue ...
func (node *Node) SetValue(val int) {
	node.value = val
}

// GetValue ...
func (node *Node) GetValue() int {
	return node.value
}

// Touch ...
func (node *Node) Touch() {
	node.freq++
}

// GetFreq ...
func (node *Node) GetFreq() int {
	return node.freq
}

// GetKey ...
func (node *Node) GetKey() int {
	return node.key
}

// NewList ...
func NewList(node *Node) *List {
	head := new(Node)
	tail := new(Node)

	head.prev = nil
	tail.next = nil

	if node != nil {
		head.next = node
		tail.prev = node

		node.next = tail
		node.prev = head
	} else {
		head.next = tail
		tail.prev = head
	}

	return &List{head, tail}
}

// IsEmpty ...
func (list *List) IsEmpty() bool {
	return list.head != nil && list.head.next != nil && list.head.next.next == nil
}

// PushFront ...
func (list *List) PushFront(node *Node) {
	if node == nil || list.head.next == nil {
		// bad...
		return
	}

	next := list.head.next
	list.head.next = node
	next.prev = node

	node.prev = list.head
	node.next = next
}

// Push ...
func (list *List) Push(node *Node) {
	if node == nil || list.tail.prev == nil {
		// bad...
		return
	}

	prev := list.tail.prev
	list.tail.prev = node
	prev.next = node

	node.next = list.tail
	node.prev = prev
}

// PopFront ...
func (list *List) PopFront() *Node {
	if list == nil || list.head == nil || list.head.next == nil {
		return nil
	}

	curr := list.head.next
	if curr.next == nil {
		// If tail node, no need to continue
		return nil
	}

	curr.Detach()
	return curr
}

// Pop ...
func (list *List) Pop() *Node {
	if list == nil || list.tail == nil || list.tail.prev == nil {
		return nil
	}

	curr := list.tail.prev
	if curr.prev == nil {
		// if head node, no need to continue
		return nil
	}

	curr.Detach()
	return curr
}

// Detach ...
func (node *Node) Detach() {
	if node.prev == nil || node.next == nil {
		// Can't detach a head or a tail node
		return
	}

	next := node.next
	prev := node.prev

	prev.next = next
	next.prev = prev

	node.prev = nil
	node.next = nil
}
