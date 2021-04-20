package p1

import (
	"fmt"
	// "sort"
	"time"

	s "go-problems/shared"
)

// MXORProblems ...
type MXORProblems struct {
	set []*MXOR
}

// Solve ...
func (p *MXORProblems) Solve() {
	fmt.Println()

	start := time.Now()

	for j := 0; j <= 0; j++ {
		for i, p := range p.set {
			result := p.solve()

			if j == 0 {
				s.Print(i, p.output, result)
			}
		}
	}

	fmt.Println("Algorithm finished in:", time.Since(start))
}

// MXOR ...
type MXOR struct {
	data    []int
	queries [][]int
	output  []int
}

// CreateMXOR ...
func CreateMXOR() s.Problem {
	set := make([]*MXOR, 0, 4)

	set = append(set, &MXOR{
		data: []int{0, 1, 2, 3, 4},
		queries: [][]int{
			{3, 1}, {1, 3}, {5, 6},
		},
		output: []int{3, 3, 7},
	})

	set = append(set, &MXOR{
		data: []int{5, 2, 4, 6, 6, 3},
		queries: [][]int{
			{12, 4}, {8, 1}, {6, 3},
		},
		output: []int{15, -1, 5},
	})

	return &MXORProblems{set}
}

/*
idea is to create a prefix-trie with 31 levels (min int range), such
that we can find the number that's closest to the supplement of the
target from top digits to the low digits.

first, find the supplement of the target number (b in data[i]^b),
then use this number as the guide, then go down the trie, and find the
closest number in the trie.

In addition, the closet number should also be smaller to the limit.
*/
func (p *MXOR) solve() []int {
	root := &bitTrieNode{}
	// sort.Ints(p.data)

	for _, val := range p.data {
		root.insert1(val, 31)
	}

	ans := make([]int, len(p.queries))

	for i, pair := range p.queries {
		src := 1
		for src <= pair[0] {
			src <<= 1
		}

		supp := src - (pair[0] + 1)
		if supp == 0 {
			supp = src
		}

		res := root.search1(supp, pair[1], 0, 31)

		// fmt.Println(pair[0], src, supp, res, res^pair[0])

		if res < 0 {
			ans[i] = -1
		} else {
			ans[i] = res ^ pair[0]
		}
	}

	return ans
}

type bitTrieNode struct {
	hasNum bool
	zero   *bitTrieNode
	one    *bitTrieNode
}

func (root *bitTrieNode) insert(num int) {
	if num == 0 {
		root.hasNum = true
		return
	}

	if num&1 == 1 {
		if root.one == nil {
			root.one = &bitTrieNode{}
		}

		root.one.insert(num >> 1)
	} else {
		if root.zero == nil {
			root.zero = &bitTrieNode{}
		}

		root.zero.insert(num >> 1)
	}
}

func (root *bitTrieNode) search(num, limit, src, curr, lvl int) int {
	// any numbers below are going to be larger
	if curr > limit {
		return -1
	}

	ans := -1
	val := -1

	if num&1 == 1 {
		if root.zero != nil {
			val = root.zero.search(num>>1, limit, src|(1<<lvl), curr, lvl+1)
			if val > ans {
				ans = val
			}
		}

		if root.one != nil {
			val = root.one.search(num>>1, limit, src, curr|(1<<lvl), lvl+1)
			if val > ans {
				ans = val
			}
		}
	} else {
		if root.one != nil {
			val = root.one.search(num>>1, limit, src|(1<<lvl), curr|(1<<lvl), lvl+1)
			if val > ans {
				ans = val
			}
		}

		if root.zero != nil {
			val = root.zero.search(num>>1, limit, src, curr, lvl+1)
			if val > ans {
				ans = val
			}
		}
	}

	if root.hasNum {
		if num > 0 {
			src |= num << lvl
		}

		if src > ans {
			ans = src
		}

		if lvl == 0 && num > ans {
			ans = num
		}
	}

	// if root.hasNum {
	// 	fmt.Println("leaf:", curr, src, ans)
	// }

	return ans
}

func (root *bitTrieNode) insert1(num, lvl int) {
	if lvl < 0 {
		return
	}

	if num&(1<<lvl) > 0 {
		if root.one == nil {
			root.one = &bitTrieNode{}
		}

		root.one.insert1(num, lvl-1)
	} else {
		if root.zero == nil {
			root.zero = &bitTrieNode{}
		}

		root.zero.insert1(num, lvl-1)
	}
}

func (root *bitTrieNode) search1(num, limit, curr, lvl int) int {
	if curr > limit {
		return -1
	}

	if lvl < 0 {
		return curr
	}

	ans := -1

	var first, second *bitTrieNode
	var nextFirst, nextSecond int

	if num&(1<<lvl) > 0 {
		first, second = root.one, root.zero
		nextFirst, nextSecond = curr|(1<<lvl), curr
	} else {
		first, second = root.zero, root.one
		nextFirst, nextSecond = curr, curr|(1<<lvl)
	}

	// fmt.Println("s:", num, ans, curr, lvl)

	if first != nil {
		ans = first.search1(num, limit, nextFirst, lvl-1)
	}

	if ans < 0 && second != nil {
		ans = second.search1(num, limit, nextSecond, lvl-1)
	}

	return ans
}

func (root *bitTrieNode) find(num int) bool {
	if num == 0 {
		return root.hasNum
	}

	if num&1 == 1 && root.one != nil {
		return root.one.find(num >> 1)
	}

	if root.zero != nil {
		return root.zero.find(num >> 1)
	}

	return false
}
