package challenges

import "sort"

func minimumLengthEncoding(words []string) int {
	if len(words) == 1 {
		return len(words[0]) + 1
	}

	sort.Slice(words, func(i, j int) bool {
		return len(words[i]) > len(words[j])
	})

	root := &trieNode{
		children: make([]*trieNode, 26),
	}

	var count int

	for _, w := range words {
		if !root.insert(w, len(w)-1) {
			count += len(w) + 1
		}
	}

	return count
}

type trieNode struct {
	children []*trieNode
}

func (n *trieNode) insert(word string, idx int) bool {
	if idx < 0 {
		return true
	}

	ch := int(word[idx] - 'a')
	found := true

	if n.children[ch] == nil {
		n.children[ch] = &trieNode{
			children: make([]*trieNode, 26),
		}

		found = false
	}

	if idx > 0 {
		found = n.children[ch].insert(word, idx-1) && found
	}

	return found
}
