package problems

import (
	"fmt"

	d "../Utils"
)

// SPC ...
type SPC struct {
	rEdges    [][]int
	bEdges    [][]int
	count     int
	output    []int
	testCount int
}

var (
	red  map[int][]int
	blue map[int][]int
)

// CreateSPC ...
func CreateSPC() *SPC {
	return &SPC{}
}

// Build ...
func (p *SPC) Build(test int) {
	p.testCount = 5

	switch test {
	case 1:
		p.rEdges = [][]int{{0, 1}}
		p.bEdges = [][]int{{2, 1}}
		p.count = 3
		p.output = []int{0, 1, -1}

	case 2:
		p.rEdges = [][]int{{1, 0}}
		p.bEdges = [][]int{{2, 1}}
		p.count = 3
		p.output = []int{0, -1, -1}

	case 3:
		p.rEdges = [][]int{{0, 1}}
		p.bEdges = [][]int{{1, 2}}
		p.count = 3
		p.output = []int{0, 1, 2}

	case 4:
		p.rEdges = [][]int{{0, 1}, {0, 2}}
		p.bEdges = [][]int{{1, 0}}
		p.count = 3
		p.output = []int{0, 1, 1}

	default:
		p.rEdges = [][]int{{0, 1}, {1, 2}}
		p.bEdges = [][]int{}
		p.count = 3
		p.output = []int{0, 1, -1}

	}

	p.ResetGlobals(p.count)
}

// ResetGlobals ...
func (p *SPC) ResetGlobals(count int) {
	red = make(map[int][]int, count)
	blue = make(map[int][]int, count)
}

// Run ...
func (p *SPC) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(calcSPC2(p.rEdges, p.bEdges, p.count), p.output)
			} else {
				calcSPC(p.rEdges, p.bEdges, p.count)
			}
		}
	}
}

func buildGlobals(r, b [][]int) {
	for i := range r {
		start, end := r[i][0], r[i][1]
		red[start] = append(red[start], end)
	}

	for i := range b {
		start, end := b[i][0], b[i][1]
		blue[start] = append(blue[start], end)
	}
}

func calcSPC(r, b [][]int, count int) []int {
	buildGlobals(r, b)

	m := make(map[int]int, count)
	level := 0

	var next []int
	var nextColor int

	stack := []*spcNode{
		&spcNode{
			node:  0,
			color: 0,
		},
		&spcNode{
			node:  0,
			color: 1,
		},
	}

	for len(stack) > 0 {
		temp := make([]*spcNode, 0, len(stack))
		level++

		for i := range stack {
			n := stack[i]

			if n.color == 0 {
				// was red, next ridge needs to be in blue
				next = blue[n.node]
				nextColor = 1
			} else {
				// was blue, next ridge needs to be red
				next = red[n.node]
				nextColor = 0
			}

			for _, j := range next {
				if _, ok := m[j]; ok {
					// already visited this node, and since level is solely increamental, we're sure
					// to have a larger number here, so keep the existing number.
					continue
				}

				m[j] = level
				temp = append(temp, &spcNode{
					node:  j,
					color: nextColor,
				})
			}
		}

		stack = temp
	}

	d.Debug(m, 0)

	result := make([]int, count)
	for i := 1; i < count; i++ {
		if val, ok := m[i]; ok {
			result[i] = val
		} else {
			result[i] = -1
		}
	}

	return result
}

func calcSPC2(r, b [][]int, count int) []int {
	buildGlobals(r, b)

	var next []int
	var nextColor, nextCount int

	m := make(map[int]int, count)
	nodes := make([]int, 2*count)
	colors := make([]int, 2*count)

	nodes[0], nodes[1] = 0, 0
	colors[0], colors[1] = 0, 1
	storeCount, level := 2, 0

	for storeCount > 0 {
		level++
		nextCount = 0

		for i := 0; i < storeCount; i++ {
			if colors[i] == 0 {
				// was red, next ridge needs to be in blue
				next = blue[nodes[i]]
				nextColor = 1
			} else {
				// was blue, next ridge needs to be red
				next = red[nodes[i]]
				nextColor = 0
			}

			for _, nextNode := range next {
				if _, ok := m[nextNode]; ok {
					// already visited this node, and since level is solely increamental, we're sure
					// to have a larger number here, so keep the existing number.
					continue
				}

				m[nextNode] = level
				nodes[nextCount] = nextNode
				colors[nextCount] = nextColor

				nextCount++
			}
		}

		storeCount = nextCount
	}

	d.Debug(m, count)

	result := make([]int, count)
	for i := 1; i < count; i++ {
		if val, ok := m[i]; ok {
			result[i] = val
		} else {
			result[i] = -1
		}
	}

	return result
}

type spcNode struct {
	node  int
	color int
}
