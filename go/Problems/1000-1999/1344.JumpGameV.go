package problems

import (
	"fmt"
	"sort"

	d "../../Utils"
)

// JGV ...
type JGV struct {
	problems    []*JGVProblem
	currProblem *JGVProblem
}

// Build ...
func (p *JGV) Build(test int) {
	p.ResetGlobals()

	if test < len(p.problems) {
		p.currProblem = p.problems[test]
		return
	}

	p.currProblem = p.problems[0]
}

// Run ...
func (p *JGV) Run() {
	var prb *JGVProblem

	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < len(p.problems); i++ {
			p.Build(i)
			prb = p.currProblem

			if j == 9 {
				fmt.Println("\n>>> Test case: ", i, ":")
				d.Output(prb.calcJGV(), prb.output)
			} else {
				// prb.calcJGV()
			}
		}
	}
}

// ResetGlobals ...
func (p *JGV) ResetGlobals() {
}

// JGVProblem ...
type JGVProblem struct {
	data   []int
	d      int
	output int
}

// CreateJGV ...
func CreateJGV() *JGV {
	problems := make([]*JGVProblem, 0)

	problems = append(problems, &JGVProblem{
		data:   []int{6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12},
		d:      2,
		output: 4,
	})

	problems = append(problems, &JGVProblem{
		data:   []int{3, 3, 3, 3, 3},
		d:      3,
		output: 1,
	})

	problems = append(problems, &JGVProblem{
		data:   []int{7, 6, 5, 4, 3, 2, 1},
		d:      1,
		output: 7,
	})

	problems = append(problems, &JGVProblem{
		data:   []int{7, 1, 7, 1, 7, 1},
		d:      2,
		output: 2,
	})

	problems = append(problems, &JGVProblem{
		data:   []int{66},
		d:      1,
		output: 1,
	})

	return &JGV{
		problems:    problems,
		currProblem: nil,
	}
}

func (p *JGVProblem) calcJGV() int {
	size := len(p.data)

	jumps := make([][]int, size)
	for i := 0; i < size; i++ {
		h := p.data[i]
		left, right := true, true

		for j := 1; j <= p.d; j++ {
			if left {
				if i-j >= 0 && p.data[i-j] < h {
					jumps[i] = append(jumps[i], i-j)
				} else {
					left = false
				}
			}

			if right {
				if i+j < size && p.data[i+j] < h {
					jumps[i] = append(jumps[i], i+j)
				} else {
					right = false
				}
			}

			if !left && !right {
				break
			}
		}
	}

	arr := make([][]int, size)
	for i := 0; i < size; i++ {
		arr[i] = []int{i, p.data[i]}
	}

	sort.Slice(arr, func(i, j int) bool {
		return arr[i][1] < arr[j][1]
	})

	if d.DEBUG {
		fmt.Println(arr)
	}

	dp := make([]int, size)
	max := 1

	for i := 0; i < size; i++ {
		lMax := 1
		curr := arr[i][0]

		for _, jump := range jumps[curr] {
			if 1+dp[jump] > lMax {
				lMax = 1 + dp[jump]
			}
		}

		dp[curr] = lMax

		if lMax > max {
			max = lMax
		}
	}

	/*
		dirs := make([]int, size)

		for i := 0; i < size; i++ {
			dp[i] = 1
			if i == 0 {
				dirs[i] = 1
			} else if i == size-1 {
				dirs[i] = 2
			} else {
				dirs[i] = 3
			}
		}

		for i := 1; i <= p.d; i++ {
			for j := 0; j < size; j++ {
				idx := arr[j][0]
				left, right := idx-i, idx+i

				if dirs[j]&2 != 0 {
					if left >= 0 {
						if p.data[left] < p.data[j] {
							count = 1 + dp[left]
							if count > dp[j] {
								dp[j] = count
							}
						} else {
							dirs[j] -= 2
						}
					} else {
						dirs[j] -= 2
					}
				}

				if dirs[j]&1 != 0 {
					if right < size {
						if p.data[right] < p.data[j] {
							count = 1 + dp[right]
							if count > dp[j] {
								dp[j] = count
							}
						} else {
							dirs[j]--
						}
					} else {
						dirs[j]--
					}
				}

				if i == p.d {

				}
			}
		}
	*/

	if d.DEBUG {
		fmt.Println(dp)
	}

	return max
}
