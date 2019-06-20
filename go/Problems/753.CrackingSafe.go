package problems

import (
	"fmt"
	"strconv"

	d "../Utils"
)

// var csStore map[string]int
var csKeys []string

// CS ...
type CS struct {
	n      int
	k      int
	output string
}

// CreateCS ...
func CreateCS() *CS {
	return &CS{}
}

// Build ...
func (p *CS) Build(test int) {
	switch test {
	case 1:
		p.n = 2
		p.k = 2
		p.output = "00110"

	case 2:
		p.n = 3
		p.k = 5
		p.output = "0001002003004011012013014021022023024031032033034041042043044111211311412212312413213313414214314422232242332342432443334344400"

	default:
		p.n = 1
		p.k = 2
		p.output = "01"

	}
}

// Run ...
func (p *CS) Run() {
	m := buildMap(p.n, p.k)

	/*
		///
		/// First method: recursive reduce
		///
		prefix := ""
		for i := 0; i < p.n; i++ {
			prefix += csKeys[0]
		}

		m[prefix] = true
		prefix = reduce(m, prefix, 1, p.n, p.k)

		d.Output(prefix, p.output)
	*/

	/// Second method: in-place reduce
	d.Output(reduceInPlace(m, p.n, p.k), p.output)

	result := d.Permut([]int{1, 2, 3, 4, 5}, 5, [][]int{})
	for i := range result {
		if i == 0 {
			fmt.Println("Permutation of array {1, 2, 3, 4, 5}: ")
		}

		fmt.Println(result[i])
	}
}

func buildMap(n, k int) map[string]bool {
	store := []string{""}
	csKeys = make([]string, 0, k)

	for i := 0; i < k; i++ {
		csKeys = append(csKeys, strconv.Itoa(i))
	}

	for i := 0; i < n; i++ {
		temp := make([]string, 0, k*len(store))
		for j := range csKeys {
			for k := range store {
				temp = append(temp, store[k]+csKeys[j])
			}
		}

		store = temp
	}

	m := make(map[string]bool, len(store))
	for i := range store {
		m[store[i]] = false
	}

	return m
}

func reduce(m map[string]bool, prefix string, count, n, k int) string {
	// final state -- all nodes visited once and only once
	if count == len(m) {
		return prefix
	}

	size := len(prefix)
	for i := range csKeys {
		key := prefix[size-n+1:] + csKeys[i]
		if m[key] || key == prefix[size-n:] {
			// has already visited this node, or node is self, continue with next key
			continue
		}

		m[key] = true
		result := reduce(m, prefix+csKeys[i], count+1, n, k)

		// we're good
		if len(result) > 0 {
			return result
		}

		// now back-trace
		m[key] = false
	}

	// no way to visit all nodes without duplicating the routes, no match
	return ""
}

func reduceInPlace(m map[string]bool, n, k int) string {
	prefix := ""
	for i := 0; i < n; i++ {
		prefix += csKeys[0]
	}

	var top *stackInfo
	stack := make([]*stackInfo, 0, n)

	count := 1
	keyIndex := 0
	m[prefix] = true

	for count < len(m) {
		// de-stack since we've reached the end of this layer
		if keyIndex >= k {
			s := len(stack)
			if s == 0 {
				// we're at the root, no more to try, quit
				return ""
			}

			// pop
			top, stack = stack[s-1], stack[:s-1]

			// restore states, and we shall also try next key index
			prefix = prefix[:len(prefix)-1]
			count--
			keyIndex = top.index + 1
			m[top.key] = false

			continue
		}

		l := len(prefix)
		key := prefix[l-n+1:] + csKeys[keyIndex]

		// if we've visited this key already, or if it's self, continue with the next key
		if m[key] || key == prefix[l-n:] {
			keyIndex++
			continue
		}

		// push into the stack and recreate a new stack
		stack = append(stack, &stackInfo{
			index: keyIndex,
			key:   key,
		})

		// reset stack states for the next layer
		prefix += csKeys[keyIndex]
		count++
		keyIndex = 0
		m[key] = true
	}

	return prefix
}

type stackInfo struct {
	index int
	key   string
}
