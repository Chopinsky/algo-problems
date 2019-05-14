package problems

import (
	"fmt"
	"strconv"

	d "../Utils"
)

// EAO ...
type EAO struct {
	source string
	target int
	output []string
}

// CreateEAO ...
func CreateEAO() *EAO {
	return &EAO{}
}

// Build ...
func (p *EAO) Build(test int) {
	switch test {
	case 1:
		p.source = "232"
		p.target = 8
		p.output = []string{"2*3+2", "2+3*2"}

	case 2:
		p.source = "105"
		p.target = 5
		p.output = []string{"1*0+5", "10-5"}

	case 3:
		p.source = "00"
		p.target = 0
		p.output = []string{"0+0", "0-0", "0*0"}

	case 4:
		p.source = "3456237490"
		p.target = 9191
		p.output = []string{}

	case 5:
		p.source = "3456237490"
		p.target = 338133
		p.output = []string{"345623-7490"}

	default:
		p.source = "123"
		p.target = 6
		p.output = []string{"1+2+3", "1*2*3"}

	}
}

// Run ...
func (p *EAO) Run() {
	aryChan := make(chan [][]int)
	opsChan := make(chan map[int][]string)

	go makeOps(len(p.source), opsChan)
	go makePartitions(p.source, aryChan)

	ary := <-aryChan
	ops := <-opsChan

	result := []string{}
	for _, nums := range ary {
		size := len(nums)
		if size == 0 {
			continue
		}

		if size == 1 && nums[0] == p.target {
			result = append(result, strconv.Itoa(nums[0]))
			continue
		}

		if op, ok := ops[size]; ok {
			for _, o := range op {
				res := eval(nums, o)
				d.Debug(fmt.Sprintln("Evaluating: ", nums, " with ", o, "; Result: ", res), 0)

				if res == p.target {
					result = append(result, format(nums, o))
				}
			}
		}
	}

	fmt.Println("Calculated result: ", result)
	fmt.Println("Expected result: ", p.output)
}

func makePartitions(src string, c chan<- [][]int) {
	c <- partition(toIntAry(src))
}

func toIntAry(src string) []int {
	result := make([]int, len(src))

	for i, r := range src {
		result[i] = int(r - '0')
	}

	return result
}

func partition(src []int) [][]int {
	result := [][]int{}
	base := []int{}
	index := 0

	// seek and save all leading 0s
	for index < len(src) {
		if src[index] != 0 {
			if index == 0 {
				index = -1
			}

			break
		}

		base = append(base, 0)
		index++
	}

	if index >= 0 {
		src = src[index:]
	}

	size := len(src)
	if size == 0 {
		return append(result, base)
	}

	curr := 0
	for i, val := range src {
		curr = curr*10 + val
		if i == size-1 {
			result = append(result, append(base, curr))
		} else {
			temp := append(base, curr)
			for _, next := range partition(src[i+1:]) {
				result = append(result, append(temp, next...))
			}
		}
	}

	return result
}

func makeOps(l int, c chan<- map[int][]string) {
	result := make(map[int][]string)
	if l < 2 {
		c <- result
		return
	}

	base := []string{"+", "-", "*"}
	result[2] = base

	for i := 3; i <= l; i++ {
		next := make([]string, 3*len(base))
		for j, val := range base {
			next[3*j] = val + "+"
			next[3*j+1] = val + "-"
			next[3*j+2] = val + "*"
		}

		result[i] = next
		base = next
	}

	c <- result
}

func eval(src []int, ops string) int {
	if len(ops) < 1 || len(ops) != len(src)-1 {
		return src[0]
	}

	ary := make([]int, len(src))
	ary[0] = src[0]

	for i, op := range ops {
		if op == '*' {
			ary[i], ary[i+1] = 0, src[i]*src[i+1]
		} else {
			ary[i+1] = src[i+1]
		}
	}

	var lastOp rune
	base := ary[0]

	for i, op := range ops {
		if op != '*' {
			lastOp = op
		}

		if lastOp == '-' {
			base -= ary[i+1]
		} else {
			base += ary[i+1]
		}
	}

	return base
}

func format(src []int, ops string) string {
	if len(src) != len(ops)+1 {
		return ""
	}

	base := strconv.Itoa(src[0])
	for i, op := range ops {
		base += string(op) + strconv.Itoa(src[i+1])
	}

	return base
}
