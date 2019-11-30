package problems

import (
	"fmt"

	d "../../Utils"
)

// SSS2 ...
type SSS2 struct {
	source    []string
	word      string
	output    [][]string
	testCount int
}

// CreateSSS2 ...
func CreateSSS2() *SSS2 {
	return &SSS2{}
}

// Build ...
func (p *SSS2) Build(test int) {
	switch test {
	case 1:
		p.source = []string{"havana"}
		p.word = "havana"
		p.output = [][]string{
			{"havana"},
			{"havana"},
			{"havana"},
			{"havana"},
			{"havana"},
			{"havana"},
		}

	case 2:
		p.source = []string{"bags", "baggage", "banner", "box", "cloths"}
		p.word = "bags"
		p.output = [][]string{
			{"baggage", "bags", "banner"},
			{"baggage", "bags", "banner"},
			{"baggage", "bags"},
			{"bags"},
		}

	case 3:
		p.source = []string{"havana"}
		p.word = "tatiana"
		p.output = [][]string{
			{}, {}, {}, {}, {}, {}, {},
		}

	default:
		p.source = []string{
			"mobile", "mouse", "moneypot", "monitor", "mousepad",
		}
		p.word = "mouse"
		p.output = [][]string{
			{"mobile", "moneypot", "monitor"},
			{"mobile", "moneypot", "monitor"},
			{"mouse", "mousepad"},
			{"mouse", "mousepad"},
			{"mouse", "mousepad"},
		}

	}

	p.ResetGlobals()
	p.testCount = 4
}

// Run ...
func (p *SSS2) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(calcSSS2(p.source, p.word), p.output)
			} else {
				calcSSS2(p.source, p.word)
			}
		}
	}
}

// ResetGlobals ...
func (p *SSS2) ResetGlobals() {
}

func calcSSS2(dict []string, word string) [][]string {
	if len(word) == 0 {
		return nil
	}

	// build the trie
	for i := range dict {
		root.push(dict[i], dict[i])
	}

	last := root
	res := make([][]string, 0, len(word))

	var store []string

	for i := range word {
		if last != nil {
			store, last = last.forwardOne(word[i:i+1], make([]string, 0, 3), 3)

			if d.DEBUG {
				if last != nil {
					fmt.Println(store, string(last.val), word[i:])
				} else {
					fmt.Println(store, "", word[i:])
				}
			}

			res = append(res, append([]string(nil), store...))
		} else {
			res = append(res, []string{})
		}
	}

	return res
}

const a = byte('a')

var root = &trieNode{
	val:      0,
	children: make([]*trieNode, 26),
}

type trieNode struct {
	val         byte
	src         string
	hasChildren bool
	children    []*trieNode
}

func (n *trieNode) push(val, src string) {
	head, rest := byte(val[0]), val[1:]
	idx := head - a

	var child *trieNode

	if n.children[idx] != nil {
		child = n.children[idx]
	} else {
		child = &trieNode{
			val:      head,
			children: make([]*trieNode, 26),
		}

		n.children[idx] = child
		n.hasChildren = true
	}

	if len(rest) > 0 {
		child.push(rest, src)
	} else {
		child.src = src
	}
}

func (n *trieNode) dfs(val string, store []string, limit int) []string {
	if len(store) == limit {
		return store
	}

	if len(val) == 0 {
		// we have found a value and the store is not full
		if len(n.src) > 0 {
			store = append(store, n.src)

			if len(store) == limit {
				return store
			}
		}

		// only continue the search if the node also contains children
		if n.hasChildren {
			var child *trieNode

			// search children, and from left to right
			for i := range n.children {
				child = n.children[i]

				if child != nil {
					store = child.dfs(val, store, limit)

					// if we have found enough, break now
					if len(store) == limit {
						return store
					}
				}
			}
		}

		return store
	}

	idx, rest := byte(val[0])-a, val[1:]
	next := n.children[idx]

	if next != nil {
		store = next.dfs(rest, store, limit)
	}

	return store
}

func (n *trieNode) forwardOne(val string, store []string, limit int) ([]string, *trieNode) {
	idx, rest := byte(val[0])-a, val[1:]
	next := n.children[idx]

	if next != nil {
		store = next.dfs(rest, store, limit)
		if next.hasChildren {
			return store, next
		}
	}

	return store, nil
}
