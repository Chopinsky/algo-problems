package challenges

func wordBreak(s string, wordDict []string) bool {
	root := &node{
		word:     "",
		children: make([]*node, 26),
	}

	for _, w := range wordDict {
		if len(w) == 0 {
			continue
		}

		root.insert(w, 0)
	}

	return search(root, s)
}

func search(root *node, w string) bool {
	var next *node
	curr := root
	idx := 0

	for curr != nil {
		next, idx = curr.search(w, idx, true)

		// fmt.Println(w, idx, next)

		if next == nil || idx < 0 {
			break
		}

		if next.word == w || search(root, w[idx:]) {
			return true
		}

		curr = next
	}

	return false
}

type node struct {
	word     string
	children []*node
}

func (n *node) insert(w string, idx int) {
	if idx == len(w)-1 {
		n.word = w
		return
	}

	c := int(w[idx] - 'a')
	if n.children[c] == nil {
		n.children[c] = &node{
			word:     "",
			children: make([]*node, 26),
		}
	}

	n.children[c].insert(w, idx+1)
}

func (n *node) search(w string, idx int, start bool) (*node, int) {
	if !start && len(n.word) > 0 {
		return n, idx + 1
	}

	if idx >= len(w) {
		return nil, -1
	}

	c := int(w[idx] - 'a')
	if n.children[c] == nil {
		return nil, -1
	}

	return n.children[c].search(w, idx+1, false)
}
