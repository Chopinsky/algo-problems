package p0

// WordDictionary ...
type WordDictionary struct {
	root *trie
}

type trie struct {
	word     string
	children []*trie
}

func (t *trie) insert(word string, idx int) {
	if idx == len(word) {
		t.word = word
		return
	}

	pos := int(word[idx] - 'a')
	if t.children[pos] == nil {
		t.children[pos] = &trie{
			word:     "",
			children: make([]*trie, 26),
		}
	}

	t.children[pos].insert(word, idx+1)
}

func (t *trie) search(word string, idx int) bool {
	if idx == len(word) {
		// fmt.Println("last ... ", word, idx, t.word)

		if idx > 0 && word[idx-1] == '.' && len(t.word) > 0 {
			return true
		}

		return len(t.word) > 0
	}

	if word[idx] == '.' {
		for _, next := range t.children {
			if next == nil {
				continue
			}

			// fmt.Println("wild card:", word, i, idx)

			if next.search(word, idx+1) {
				return true
			}
		}

		return false
	}

	pos := int(word[idx] - 'a')
	if t.children[pos] == nil {
		return false
	}

	return t.children[pos].search(word, idx+1)
}

// Constructor ... Initialize your data structure here.
func Constructor() WordDictionary {
	return WordDictionary{
		root: &trie{
			word:     "",
			children: make([]*trie, 26),
		},
	}
}

// AddWord ... Adds a word into the data structure.
func (t *WordDictionary) AddWord(word string) {
	t.root.insert(word, 0)
}

// Search ... Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
func (t *WordDictionary) Search(word string) bool {
	if len(word) == 0 {
		return true
	}

	return t.root.search(word, 0)
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */
