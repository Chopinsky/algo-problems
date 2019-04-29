package problems

import "fmt"

var nodes = make(map[int]bool)

// ESS ...
type ESS struct {
	graph  [][]int
	output []int
}

// CreateESS ...
func CreateESS() *ESS {
	return &ESS{}
}

// Build ...
func (p *ESS) Build(test int) {
	switch test {
	default:
		p.graph = [][]int{
			{1, 2},
			{2, 3},
			{5},
			{0},
			{5},
			{},
			{},
		}
		p.output = []int{2, 4, 5, 6}

	}
}

// Run ...
func (p *ESS) Run() {
	for i := range p.graph {
		p.walk(i)
	}

	result := []int{}
	for i := range p.graph {
		isSafe, ok := nodes[i]
		if ok && !isSafe {
			continue
		}

		result = append(result, i)
	}

	fmt.Println("Calculated results: ", result)
	fmt.Println("Expected results:   ", p.output)
}

func (p *ESS) walk(start int) {
	// already determined, early return
	if _, ok := nodes[start]; ok {
		return
	}

	initMap := make(map[int]struct{})
	initMap[start] = empty

	stack := []path{path{start, initMap}}
	var head path
	var size, safeCount int
	var nextVals []int

	for {
		if len(stack) == 0 {
			break
		}

		head, stack = stack[0], stack[1:]
		nextVals = p.graph[head.curr]
		size = len(nextVals)

		if size == 0 {
			nodes[head.curr] = true
			continue
		}

		safeCount = 0
		for _, next := range nextVals {
			if isSafe, ok := nodes[next]; ok {
				// connecting to a ring, everything so far is not-safe
				if !isSafe {
					head.dye()
					break
				}

				// otherwise, we're connected to a safe node, no need to continue
				// this path
				safeCount++
			} else {
				// find the ring, mark all nodes in the ring as not-safe
				if _, ok := head.route[next]; ok {
					head.dye()
					break
				}

				nextMap := make(map[int]struct{})
				for k := range head.route {
					nextMap[k] = empty
				}

				nextMap[next] = empty
				stack = append(stack, path{next, nextMap})
			}
		}

		// if all connected nodes are safe, self is safe, too
		if safeCount == size {
			nodes[head.curr] = true
		}
	}
}

type path struct {
	curr  int
	route map[int]struct{}
}

func (p *path) dye() {
	for k := range p.route {
		nodes[k] = false
	}
}
