package problems

import (
	"fmt"

	d "../../Utils"
)

// CSII ...
type CSII struct {
	source    [][]int
	number    int
	output    []int
	testCount int
}

// CreateCSII ...
func CreateCSII() *CSII {
	return &CSII{}
}

// Build ...
func (p *CSII) Build(test int) {
	p.ResetGlobals()
	p.testCount = 2

	switch test {
	case 1:
		p.source = [][]int{
			{1, 3},
			{2, 3},
			{0, 1},
			{0, 2},
		}
		p.number = 4
		p.output = []int{3, 2, 1, 0}

	default:
		p.source = [][]int{
			{1, 0},
		}
		p.number = 2
		p.output = []int{0, 1}

	}
}

var graph map[int][]int

// ResetGlobals ...
func (p *CSII) ResetGlobals() {
}

// Run ...
func (p *CSII) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(calcCSII(p.number, p.source), p.output)
			} else {
				calcCSII(p.number, p.source)
			}
		}
	}
}

func buildGraph(number int, prerequisities [][]int) {
	graph = make(map[int][]int, number)

	for _, dependencies := range prerequisities {
		if len(dependencies) != 2 {
			fmt.Println("Data formation error: ", dependencies)
			continue
		}

		start, end := dependencies[0], dependencies[1]
		graph[start] = append(graph[start], end)
	}

	if d.DEBUG {
		fmt.Println(graph)
	}
}

func calcCSII(number int, prerequisites [][]int) []int {
	buildGraph(number, prerequisites)

	result := make([]int, 0, number)
	stack := make([]int, 0, number)
	visited := make([]bool, number)

	for i := 0; i < number; i++ {
		if visited[i] {
			continue
		}

		stack = append(stack, i)
		result = dfsInPlace(visited, stack, result)

		// clear the stack
		stack = stack[:0]
	}

	return result
}

func dfsInPlace(visited []bool, stack, result []int) []int {
	var curr int

	size = 1
	for size > 0 {
		curr, stack = stack[size-1], stack[:size-1]
		size--

		if dependencies, ok := graph[curr]; ok {
			stack = append(stack, curr)
			size++
			done := true

			for i := range dependencies {
				node := dependencies[i]
				if !visited[node] {
					done = false
					stack = append(stack, node)
					size++
				}
			}

			if done {
				// remove the current from the stack
				stack = stack[:size-1]
				size--

				// store the current and update the visited array
				result = append(result, curr)
				visited[curr] = true
			}
		} else {
			// the course has no dependencies, just append it
			result = append(result, curr)
			visited[curr] = true
		}
	}

	if d.DEBUG {
		fmt.Println(result)
	}

	return result
}
