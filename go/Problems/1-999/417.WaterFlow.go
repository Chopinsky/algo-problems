package problems

import (
	"fmt"

	d "../../Utils"
)

// WF ...
type WF struct {
	source [][]int
	flow   [][]int
}

// CreateWF ...
func CreateWF() *WF {
	return &WF{}
}

// Build ...
func (p *WF) Build(test int) {
	switch test {
	default:
		p.source = [][]int{
			{1, 2, 2, 3, 5},
			{3, 2, 3, 4, 4},
			{2, 4, 5, 3, 1},
			{6, 7, 1, 4, 5},
			{5, 1, 1, 2, 4},
		}

		p.flow = [][]int{
			{0, 4}, {1, 3}, {1, 4}, {2, 2}, {3, 0}, {3, 1}, {4, 0},
		}

	}
}

// Run ...
func (p *WF) Run() {
	m := len(p.source)
	n := len(p.source[0])
	results := [][]int{}

	// init flow
	flow := make([][][]bool, m)
	for i := range flow {
		flow[i] = make([][]bool, n)
		for j := range flow[i] {
			flow[i][j] = []bool{false, false}
			if i == 0 || j == 0 {
				flow[i][j][0] = true
			}

			if i == m-1 || j == n-1 {
				flow[i][j][1] = true
			}
		}
	}

	// run the flow for bidirections
	p.calc(m, n, 0, flow)
	p.calc(m, n, 1, flow)

	// check the flow
	for i := range flow {
		for j := range flow[i] {
			if flow[i][j][0] && flow[i][j][1] {
				results = append(results, []int{i, j})
			}
		}
	}

	fmt.Println("Calculated results: ", results)
	fmt.Println("Expected results: ", p.flow)
}

func (p *WF) calc(m, n, k int, flow [][][]bool) {
	queue := initQueue(k, m, n)
	if len(queue) == 0 {
		return
	}

	var i, j, x, y, val int

	for {
		// pop head
		i = queue[0][0]
		j = queue[0][1]
		val = p.source[i][j]
		queue = queue[1:]

		// check, flip, and update the surrounding nodes
		for idx := 0; idx < 4; idx++ {
			x = i + dir[idx]
			y = j + dir[idx+1]

			if x >= 0 && x < m && y >= 0 && y < n && !flow[x][y][k] && p.source[x][y] >= val {
				flow[x][y][k] = true
				queue = append(queue, []int{x, y})
			}
		}

		if len(queue) == 0 {
			break
		}
	}

}

func initQueue(isAtlantic, m, n int) [][]int {
	q := make([][]int, m+n-1)
	size := d.Max(m, n)
	index := 1

	if isAtlantic == 0 {
		q[0] = []int{0, 0}

		for i := 1; i < size; i++ {
			if i < m {
				q[index] = []int{i, 0}
				index++
			}

			if i < n {
				q[index] = []int{0, i}
				index++
			}
		}
	} else {
		q[0] = []int{m - 1, n - 1}

		for i := 0; i < size-1; i++ {
			if i < m {
				q[index] = []int{i, n - 1}
				index++
			}

			if i < n {
				q[index] = []int{m - 1, i}
				index++
			}
		}
	}

	return q
}
