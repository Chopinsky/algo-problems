package p1

import (
	"fmt"
	"sort"
	"time"

	s "go-problems/shared"
)

// FBSProblems ...
type FBSProblems struct {
	set []*FBS
}

// Solve ...
func (p *FBSProblems) Solve() {
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

// FBS ...
type FBS struct {
	data   []int
	load   []int
	k      int
	output []int
}

// CreateFBS ...
func CreateFBS() s.Problem {
	set := make([]*FBS, 0, 4)

	set = append(set, &FBS{
		data:   []int{1, 2, 3, 4, 5},
		load:   []int{5, 2, 3, 3, 3},
		k:      3,
		output: []int{1},
	})

	set = append(set, &FBS{
		data:   []int{1, 2, 3, 4},
		load:   []int{1, 2, 1, 2},
		k:      3,
		output: []int{0},
	})

	set = append(set, &FBS{
		data:   []int{1, 2, 3},
		load:   []int{10, 12, 11},
		k:      3,
		output: []int{0, 1, 2},
	})

	set = append(set, &FBS{
		data:   []int{1, 2, 3, 4, 8, 9, 10},
		load:   []int{5, 2, 10, 3, 1, 2, 2},
		k:      3,
		output: []int{1},
	})

	set = append(set, &FBS{
		data:   []int{1},
		load:   []int{1},
		k:      1,
		output: []int{0},
	})
	return &FBSProblems{set}
}

func (p *FBS) solve() []int {
	if p.k == 1 {
		return []int{0}
	}

	h := make(s.IntHeap, 0, p.k)
	var root *s.TreeNode

	counts := make(map[int]int, p.k)
	maxCount := 0

	for i, t := range p.data {
		// find out servers that have finished their tasks,
		// and add them to the free-servers-tree
		for h.Len() > 0 && h[0][0] <= t {
			free := h.Pop().([]int)
			// fmt.Println("freed up server:", free[1])

			if root != nil {
				root.Insert(free[1])
			} else {
				root = s.MakeNode(free[1])
			}
		}

		// get the default server id
		s := i % p.k

		// if we have every server has been assigned at the
		// moment, looking for the ones that are free now
		if i >= p.k {
			// we don't have any free servers at the moment, skip
			if root == nil {
				continue
			}

			// get the id of the next free server with id larger
			// or equal to desired server id of `s`
			next := root.Ceil(s)

			if next != nil {
				// get the actual free server
				s = next.Val
			} else {
				// if wrapping around and starting from 0, get the
				// smallest server id
				s = root.Min()
			}

			// now remove this server from the free server tree
			root = root.Delete(s)
		}

		// update the counters
		counts[s]++
		if counts[s] > maxCount {
			maxCount = counts[s]
		}

		// move the server to the busy-servers-heap
		h.Push([]int{t + p.load[i], s})
	}

	// done, retrieve the busy servers
	ans := []int{}
	for k, v := range counts {
		if v == maxCount {
			ans = append(ans, k)
		}
	}

	sort.Ints(ans)

	return ans
}
