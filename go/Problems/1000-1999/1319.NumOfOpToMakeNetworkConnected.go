package problems

import (
	"fmt"
	"sort"

	d "../../Utils"
)

// MOMNC ...
type MOMNC struct {
	problems    []*MOMNCProblem
	currProblem *MOMNCProblem
}

// Build ...
func (p *MOMNC) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *MOMNC) Run() {
	var prb *MOMNCProblem

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\n>>> Test case: ", i, ":")
				d.Output(prb.calcMOMNC(), prb.output)
			} else {
				// prb.calcMOMNC()
			}
		}
	}
}

// ResetGlobals ...
func (p *MOMNC) ResetGlobals() {
}

// MOMNCProblem ...
type MOMNCProblem struct {
	source [][]int
	count  int
	output int
}

// CreateMOMNC ...
func CreateMOMNC() *MOMNC {
	problems := make([]*MOMNCProblem, 0, 4)

	problems = append(problems, &MOMNCProblem{
		source: [][]int{
			{0, 1}, {0, 2}, {1, 2},
		},
		count:  4,
		output: 1,
	})

	problems = append(problems, &MOMNCProblem{
		source: [][]int{
			{0, 1}, {0, 2}, {0, 3}, {1, 2}, {1, 3},
		},
		count:  6,
		output: 2,
	})

	problems = append(problems, &MOMNCProblem{
		source: [][]int{
			{0, 1}, {0, 2}, {0, 3}, {1, 2},
		},
		count:  6,
		output: -1,
	})

	problems = append(problems, &MOMNCProblem{
		source: [][]int{
			{0, 1}, {0, 2}, {3, 4}, {2, 3},
		},
		count:  5,
		output: 0,
	})

	return &MOMNC{
		problems:    problems,
		currProblem: nil,
	}
}

func (p *MOMNCProblem) calcMOMNC() int {
	sort.SliceStable(p.source, func(i, j int) bool { return p.source[i][0] < p.source[j][0] })

	size := len(p.source)
	src, unions := p.source, createUnion(p.count)

	srcMap := make(map[int][]int)
	network := make([]int, p.count)

	nwCount, extra := 0, 0

	for i := 0; i < size; i++ {
		a, b := src[i][0], src[i][1]
		if a > b {
			a, b = b, a
		}

		root := union(unions, a, b)

		srcMap[a] = append(srcMap[a], b)

		if _, ok := srcMap[b]; !ok {
			srcMap[b] = []int{}
		}

		if network[root] == 0 {
			// a new network is found
			network[root] = 1
			nwCount++
		}
	}

	for i := 0; i < p.count; i++ {
		if _, ok := srcMap[i]; ok {
			if network[i] == 1 {
				extra += p.calcRedudent(i, srcMap)
			}

			continue
		}

		// isolated, sole-computer network
		nwCount++
	}

	if !d.DEBUG {
		fmt.Println(unions)
		fmt.Println(nwCount, extra)
	}

	if nwCount == 1 {
		return 0
	}

	if extra >= nwCount-1 {
		return nwCount - 1
	}

	return -1
}

func (p *MOMNCProblem) calcRedudent(head int, srcMap map[int][]int) int {
	nodes := make(map[int]struct{})
	count := 0

	queue := append([]int(nil), srcMap[head]...)
	nodes[head] = empty

	for len(queue) > 0 {
		head, queue = queue[0], queue[1:]

		if _, ok := nodes[head]; ok {
			count++
			continue
		}

		next := srcMap[head]
		if len(next) > 0 {
			queue = append(queue, next...)
		}

		nodes[head] = empty
	}

	return count
}

func createUnion(count int) []int {
	src := make([]int, count)

	for i := 0; i < count; i++ {
		src[i] = i
	}

	return src
}

func union(src []int, i, j int) int {
	iRoot, jRoot := find(src, i), find(src, j)

	if iRoot < jRoot {
		src[jRoot] = iRoot
		return iRoot
	}

	src[iRoot] = jRoot
	return jRoot
}

func find(src []int, i int) int {
	for src[i] != i {
		i = src[i]
	}

	return i
}
