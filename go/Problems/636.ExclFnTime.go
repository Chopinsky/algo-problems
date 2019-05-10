package problems

import (
	"fmt"
	"strconv"
	"strings"
)

// ETF ...
type ETF struct {
	source int
	logs   []string
	output []int
}

// CreateETF ...
func CreateETF() *ETF {
	return &ETF{}
}

// Build ...
func (p *ETF) Build(test int) {
	switch test {
	case 1:
		p.source = 1
		p.logs = []string{
			"0:start:0",
			"0:start:2",
			"0:start:3",
			"0:end:3",
			"0:end:4",
			"0:end:6",
		}
		p.output = []int{7}

	case 2:
		p.source = 3
		p.logs = []string{
			"0:start:0",
			"1:start:2",
			"0:start:3",
			"0:end:3",
			"2:start:5",
			"2:end:5",
			"1:end:7",
			"0:end:9",
		}
		p.output = []int{5, 4, 1}

	default:
		p.source = 2
		p.logs = []string{
			"0:start:0",
			"1:start:2",
			"1:end:5",
			"0:end:6",
		}
		p.output = []int{3, 4}

	}
}

// Run ...
func (p *ETF) Run() {
	fmt.Println("Calculated result: ", p.calc())
	fmt.Println("Expected result: ", p.output)
}

func (p *ETF) calc() []int {
	result := make([]int, p.source)
	fnStack := make([][]int, 0, p.source)
	start := 0
	var top []int

	for _, log := range p.logs {
		info := parse(log)
		size := len(fnStack)

		if info[1] == 0 {
			// a start
			if size > 0 {
				// update the top function's running time
				fnStack[size-1][1] += info[2] - start
			}

			// push the new Fn to the stack top
			fnStack = append(fnStack, []int{info[0], 0})
			start = info[2]
		} else {
			// an end, pop and update the top fn in the stack
			top, fnStack = fnStack[size-1], fnStack[:size-1]
			top[1] += info[2] - start + 1
			start = info[2] + 1

			// update the final result
			result[top[0]] += top[1]
		}
	}

	return result
}

func parse(input string) []int {
	result := make([]int, 3)
	for i, val := range strings.Split(input, ":") {
		if i >= 3 {
			break
		}

		if i == 1 {
			if val == "start" {
				result[i] = 0
			} else {
				result[i] = 1
			}
		} else {
			result[i], _ = strconv.Atoi(val)
		}
	}

	return result
}
