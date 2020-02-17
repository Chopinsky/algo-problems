package problems

import (
	"fmt"

	d "../../Utils"
)

// SGII ...
type SGII struct {
	source    []int
	output    int
	testCount int
}

// CreateSGII ...
func CreateSGII() *SGII {
	return &SGII{}
}

// Build ...
func (p *SGII) Build(test int) {
	p.ResetGlobals()
	p.testCount = 1

	switch test {
	default:
		p.source = []int{2, 7, 9, 4, 4}
		p.output = 10

	}

	buildSGII(p.source)
}

var (
	sgiiSum   []int
	sgiiStore map[int][]int
)

// ResetGlobals ...
func (p *SGII) ResetGlobals() {
}

// Run ...
func (p *SGII) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")

				s1, _ := calcSGII(p.source, 0, len(p.source), 1, 0, 0, true)
				d.Output(s1, p.output)
			} else {
				calcSGII(p.source, 0, len(p.source), 1, 0, 0, true)
			}
		}
	}
}

func buildSGII(piles []int) {
	sgiiSum = make([]int, len(piles)+1)
	for i := range piles {
		sgiiSum[i+1] = sgiiSum[i] + piles[i]
	}

	sgiiStore = make(map[int][]int, 2*len(piles))
}

func getSliceSum(i, j int) int {
	return sgiiSum[j+1] - sgiiSum[i]
}

func getSgiiKey(start, m int, s1Pick bool) int {
	if s1Pick {
		return start<<9 | m<<1 | 1
	}

	return start<<9 | m<<1
}

func calcSGII(piles []int, start, size, m, s1, s2 int, s1Pick bool) (int, int) {
	if start >= size {
		return s1, s2
	}

	key := getSgiiKey(start, m, s1Pick)
	if stones, ok := sgiiStore[key]; ok {
		d.Debug(fmt.Sprintln("lucky hit: ", start, m, s1Pick), 0)
		return s1 + stones[0], s2 + stones[1]
	}

	s1Max, s2Max := 0, 0
	delta1, delta2 := 0, 0
	var s1Next, s2Next, temp1, temp2 int

	for i := 0; i < d.Min(2*m, len(piles)-start); i++ {
		pickSum := getSliceSum(start, start+i)

		if s1Pick {
			s1Next = s1 + pickSum
			s2Next = s2
		} else {
			s1Next = s1
			s2Next = s2 + pickSum
		}

		temp1, temp2 = calcSGII(piles, start+i+1, size, d.Max(m, i+1), s1Next, s2Next, !s1Pick)

		d.Debug(fmt.Sprintln(start, i, s1, s2, s1Next, s2Next, temp1, temp2), 0)

		if (s1Pick && temp1 > s1Max) || (!s1Pick && temp2 > s2Max) {
			s1Max, s2Max = temp1, temp2
			delta1, delta2 = temp1-s1, temp2-s2
		}
	}

	sgiiStore[key] = []int{delta1, delta2}
	return s1Max, s2Max
}
