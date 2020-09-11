package challenges

// StreamChecker ...
type StreamChecker struct {
	root *scNode
	ptrs []*scNode
}

type scNode struct {
	word     bool
	children []*scNode
}

func (n *scNode) insert(src string, idx int) {
	if idx == len(src) {
		n.word = true
		return
	}

	c := src[idx] - 'a'

	if n.children[c] == nil {
		n.children[c] = &scNode{
			word:     false,
			children: make([]*scNode, 26),
		}
	}

	n.children[c].insert(src, idx+1)
}

func (n *scNode) query(c byte) *scNode {
	return n.children[c-'a']
}

// Constructor ...
func Constructor(words []string) StreamChecker {
	s := StreamChecker{
		root: &scNode{
			word:     false,
			children: make([]*scNode, 26),
		},
		ptrs: []*scNode{},
	}

	for _, w := range words {
		s.root.insert(w, 0)
	}

	return s
}

// Query ...
func (t *StreamChecker) Query(l byte) bool {
	next := make([]*scNode, 0, len(t.ptrs))
	found := false

	nextscNode := t.root.children[l-'a']
	if nextscNode != nil {
		next = append(next, nextscNode)
		found = nextscNode.word
	}

	for _, n := range t.ptrs {
		nextscNode = n.query(l)
		if nextscNode != nil {
			next = append(next, nextscNode)

			if !found {
				found = nextscNode.word
			}
		}
	}

	t.ptrs = next

	return found
}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * obj := Constructor(words);
 * param_1 := obj.Query(letter);
 */
