package problems

import (
	"fmt"
	"sort"

	d "../../Utils"
)

// SSS ...
type SSS struct {
	source    string
	pairs     [][]int
	output    string
	testCount int
}

// CreateSSS ...
func CreateSSS() *SSS {
	return &SSS{}
}

// Build ...
func (p *SSS) Build(test int) {
	p.ResetGlobals()
	p.testCount = 3

	switch test {
	case 1:
		p.source = "dcab"
		p.pairs = [][]int{
			{0, 3},
			{1, 2},
			{0, 2},
		}
		p.output = "abcd"

	case 2:
		p.source = "cba"
		p.pairs = [][]int{
			{0, 1},
			{1, 2},
		}
		p.output = "abc"

	default:
		p.source = "dcab"
		p.pairs = [][]int{
			{0, 3},
			{1, 2},
		}
		p.output = "bacd"

	}
}

// var graph map[int][]int
var arr []int

// ResetGlobals ...
func (p *SSS) ResetGlobals() {
	// graph = make(map[int][]int, 26)
}

// Run ...
func (p *SSS) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(calcSSS(p.source, p.pairs), p.output)
			} else {
				//calcSSS(p.source)
			}
		}
	}
}

func calcSSS(src string, pairs [][]int) string {
	if len(pairs) == 0 {
		return src
	}

	// buildGraph(pairs)

	size := len(src)
	final := make([]byte, size)

	groups := buildGroups(pairs, size)
	for _, v := range groups {
		sort.Ints(v)

		bytes := make([]byte, len(v))
		for i, val := range v {
			bytes[i] = src[val]
		}

		sort.Slice(bytes, func(i, j int) bool {
			return bytes[i] < bytes[j]
		})

		for i, val := range v {
			final[val] = bytes[i]
		}
	}

	return string(final)
}

func buildGroups(pairs [][]int, size int) map[int][]int {
	sort.Slice(pairs, func(i, j int) bool {
		if pairs[i][0] == pairs[j][0] {
			return pairs[i][1] < pairs[j][1]
		}

		return pairs[i][0] < pairs[j][0]
	})

	arr = make([]int, size)
	for i := 0; i < size; i++ {
		arr[i] = i
	}

	for _, pair := range pairs {
		a, b := findRoot(pair[0]), findRoot(pair[1])

		if a >= b {
			arr[a] = b
		} else {
			arr[b] = a
		}
	}

	if d.DEBUG {
		fmt.Println(arr)
	}

	groups := make(map[int][]int)

	for i := range arr {
		root := findRoot(i)
		groups[root] = append(groups[root], i)
	}

	return groups
}

func findRoot(i int) int {
	res := i

	for res != arr[res] {
		res = arr[res]
	}

	return res
}

/*
func buildGraph(pairs [][]int) {
	for _, pair := range pairs {
		graph[pair[0]] = append(graph[pair[0]], pair[1])
		graph[pair[1]] = append(graph[pair[1]], pair[0])
	}
}
*/

/*
func dfsSSS(src string, start, size int) string {
	stack := make([]int, 0, size)
	visited := make([]bool, len(graph))
	stack = append(stack, start)

	var curr int
	for len(stack) > 0 {
		curr, stack = stack[0], stack[1:]

		if !visited[curr] {

		}

		visited[curr] = true

		if next, ok := graph[curr]; ok {
			for _, nextPos := range next {
				if !visited[nextPos] {
					stack = append(stack, nextPos)
				}
			}
		}
	}

	return string(src[curr])
}
*/
