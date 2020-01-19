package problems

import (
	"fmt"
	"strconv"

	d "../../Utils"
)

// SAIFS ...
type SAIFS struct {
	problems    []*SAIFSProblem
	currProblem *SAIFSProblem
}

// Build ...
func (p *SAIFS) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *SAIFS) Run() {
	var prb *SAIFSProblem

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\n>>> Test case: ", i, ":")
				d.Output(prb.calcSAIFS(), prb.output)
			} else {
				prb.calcSAIFS()
			}
		}
	}
}

// ResetGlobals ...
func (p *SAIFS) ResetGlobals() {
}

// SAIFSProblem ...
type SAIFSProblem struct {
	source string
	output []int
}

// CreateSAIFS ...
func CreateSAIFS() *SAIFS {
	problems := make([]*SAIFSProblem, 0)

	problems = append(problems, &SAIFSProblem{
		source: "123456579",
		output: []int{123, 456, 579},
	})

	problems = append(problems, &SAIFSProblem{
		source: "11235813",
		output: []int{1, 1, 2, 3, 5, 8, 13},
	})

	problems = append(problems, &SAIFSProblem{
		source: "112358130",
		output: []int{},
	})

	problems = append(problems, &SAIFSProblem{
		source: "0123",
		output: []int{},
	})

	problems = append(problems, &SAIFSProblem{
		source: "1101111",
		output: []int{11, 0, 11, 11},
	})

	return &SAIFS{
		problems:    problems,
		currProblem: nil,
	}
}

func (p *SAIFSProblem) calcSAIFS() []int {
	size := len(p.source)
	cache := make([][]int, size)

	for i := 0; i < size; i++ {
		cache[i] = make([]int, size)
		for j := i; j < size; j++ {
			p.toNum(i, j, cache)
		}
	}

	if d.DEBUG {
		fmt.Println(cache)
	}

	for i := 0; i < size-2; i++ {
		if cache[0][i] == -1 {
			return []int{}
		}

		for j := i + 1; j < size-1; j++ {
			if cache[i+1][j] == -1 {
				break
			}

			res := p.genFibSeq(i, j, size, cache)
			if res != nil {
				return res
			}

			rest := size - 1 - j
			if j > rest || i > rest {
				break
			}
		}
	}

	return []int{}
}

func (p *SAIFSProblem) genFibSeq(i, j, size int, cache [][]int) []int {
	first, second, b := cache[0][i], cache[i+1][j], j
	res := []int{first, second}

	for first >= 0 && second >= 0 {
		next := first + second
		c := b + getDigits(next)

		if d.DEBUG {
			fmt.Println(i, j, first, second, next, b, c, cache[b+1][c])
		}

		if c >= size {
			// we don't have that many ditis left
			return nil
		}

		if cache[b+1][c] != next {
			// not a match
			return nil
		}

		res = append(res, next)

		if c == size-1 {
			return res
		}

		first, second, b = second, next, c
	}

	return nil
}

func (p *SAIFSProblem) toNum(i, j int, cache [][]int) int {
	val, err := strconv.Atoi(p.source[i : j+1])
	if err != nil {
		// fail to parse, illegal
		val = -1
	}

	if p.source[i] == byte('0') && val != 0 {
		// illegal number
		val = -1
	}

	cache[i][j] = val
	return val
}

func getDigits(num int) int {
	if num == 0 {
		return 1
	}

	count := 0
	for num > 0 {
		num /= 10
		count++
	}

	return count
}
