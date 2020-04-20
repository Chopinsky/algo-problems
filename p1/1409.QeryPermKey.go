package p1

import (
	"fmt"
	"math/rand"
	"time"

	s "go-problems/shared"
)

// QPKProblems ...
type QPKProblems struct {
	set []*QPK
}

// Solve ...
func (p *QPKProblems) Solve() {
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

	fmt.Println("Algorithm took", time.Since(start))
}

// QPK ...
type QPK struct {
	data   []int
	m      int
	output []int
}

// CreateQPK ...
func CreateQPK() s.Problem {
	set := make([]*QPK, 0, 4)

	set = append(set, &QPK{
		data:   []int{3, 1, 2, 1},
		m:      5,
		output: []int{2, 1, 2, 1},
	})

	set = append(set, &QPK{
		data:   []int{4, 1, 2, 2},
		m:      4,
		output: []int{3, 1, 2, 0},
	})

	set = append(set, &QPK{
		data:   []int{7, 5, 5, 8, 3},
		m:      8,
		output: []int{6, 5, 0, 7, 5},
	})

	rand.Seed(time.Now().UnixNano())
	size := 1000
	d := make([]int, size)

	for i := 0; i < size; i++ {
		d[i] = rand.Intn(size) + 1
	}

	set = append(set, &QPK{
		data:   d,
		m:      size,
		output: []int{},
	})

	return &QPKProblems{set}
}

// scheme: padded queue, only move the queried value to the front, don't shift
//  1) at the beginning:               [0,0,0,0,0,1,2,3,4,5]
//  2) then move one to the front:     [0,0,0,0,2,1,0,3,4,5]
//  3) then move another, till finish: [0,0,0,2,0,1,0,3,4,5]
//
// goal: calculate how many elements are in front of the queried element
//       to get the position of it
func (p *QPK) solve() []int {
	size := len(p.data)
	result := make([]int, 0, size)

	f := s.CreateFenwick(2*p.m + 1)
	loc := make(map[int]int)

	for i := 1; i <= p.m; i++ {
		f.Update(p.m+i, 1)
		loc[i] = p.m + i
	}

	if s.DebugMode() {
		fmt.Println(loc, p.m)
	}

	for i := 0; i < size; i++ {
		// the query value -- index in the loc
		q := p.data[i]

		// the front position to which the fenwick queue to place this query, i.e.
		// prepend to the front of the queue
		pos := p.m - i

		// the current location of the queried number in the padded queue
		curr := loc[q]

		if curr > 2*p.m {
			fmt.Println("error:", i, q, curr)
		}

		// get the sum of elements till `curr`, minus 1 to be the index
		actual := f.Query(curr) - 1
		result = append(result, actual)

		// update the book-keeprs: now the element is moved to the front of
		// the queue, need to update the location hashmap, as well as the
		// fenwick prefix-sums -- moving the element from `curr` to `pos`
		loc[q] = pos
		f.Update(curr, -1) // remove the value from the current location in Fenwick
		f.Update(pos, 1)   // add the value to the front of the queue
	}

	return result
}

func (p *QPK) solve1() []int {
	size := len(p.data)
	result := make([]int, 0, size)
	locations := make([]int, p.m)
	lastQuery := make([]int, p.m)
	largest := 0

	for i := 0; i < p.m; i++ {
		locations[i] = i
		lastQuery[i] = -1
	}

	var actual int

	for i := 0; i < size; i++ {
		q := p.data[i]
		loc := locations[q-1]

		if loc > largest {
			actual = loc
			largest = loc
		} else {
			actual = findActual(loc, lastQuery[q-1], result)
		}

		result = append(result, actual)
		locations[q-1] = 0
		lastQuery[q-1] = i

		if s.DebugMode() {
			fmt.Println(q, locations, lastQuery, actual)
		}
	}

	return result
}

func findActual(loc, last int, output []int) int {
	var start int

	if last < 0 {
		start = 0
	} else {
		start = last + 1
	}

	for i := start; i < len(output); i++ {
		pos := output[i]
		if pos >= loc {
			loc++
		}
	}

	return loc
}
