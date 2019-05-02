package problems

import (
	"fmt"

	d "../Utils"
)

var m = make(map[rune][]int)

// NMS ...
type NMS struct {
	source string
	words  []string
	output int
}

// CreateNMS ...
func CreateNMS() *NMS {
	return &NMS{}
}

// Build ...
func (p *NMS) Build(test int) {
	switch test {
	default:
		p.source = "abcde"
		p.words = []string{"a", "bb", "acd", "ace", "ae", "abb", "bcdde"}
		p.output = 4

	}
}

// Run ...
func (p *NMS) Run() {
	for i, r := range p.source {
		m[r] = append(m[r], i)
	}

	count := 0
	size := len(p.source)
	for _, w := range p.words {
		if p.search(w, size) {
			count++
		}
	}

	fmt.Println("Calculated result: ", count)
	fmt.Println("Expected result: ", p.output)
}

func (p *NMS) search(word string, size int) bool {
	wordSize := len(word)
	if wordSize > size {
		return false
	}

	pos := -1
	found := false
	store := make(map[rune]int)

	var arySize, start int

	for i, r := range word {
		if ary, ok := m[r]; ok {
			arySize = len(ary)

			// no more match left
			if arySize == 0 {
				return false
			}

			// no more match behind the current pos can be found
			if pos > ary[arySize-1] {
				return false
			}

			if pos < 0 {
				// first rune
				pos = ary[0]
				store[r] = 0
			} else {
				start = 0
				found = false

				// update the starting index
				if last, ok := store[r]; ok {
					start = last + 1
				}

				// find the first rune after the current position
				for j := start; j < arySize; j++ {
					if ary[j] > pos {
						pos = ary[j]
						store[r] = j
						found = true
						break
					}
				}

				// can't find the rune again in the source string
				if !found {
					return false
				}
			}

			d.Debug(fmt.Sprintln(word, " - ", r, pos, store), 0)

			// not enough subsequences to match with
			if size-pos < wordSize-i {
				return false
			}
		} else {
			return false
		}
	}

	return true
}
