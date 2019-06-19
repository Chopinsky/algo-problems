package problems

import (
	"strconv"

	d "../Utils"
)

// FDS ...
type FDS struct {
	source []int
	output [][]int
}

// CreateFDS ...
func CreateFDS() *FDS {
	return &FDS{}
}

// Build ...
func (p *FDS) Build(test int) {
	switch test {
	default:
		p.source = []int{1, 2, 3, 4, -1, 2, 4, -1, -1, -1, -1, 4}
		p.output = [][]int{
			{1, 5},
			{3, 6, 11},
		}

	}
}

// Run ...
func (p *FDS) Run() {
	// Approach 1: naive iterations
	// indices := p.buildIndices()
	// fmt.Println(p.search(indices))

	// Approach 2: serailization
	_, index := tokenize(p.source, make(map[int]string), 0, len(p.source))

	store := make(map[string][]int)
	for key, val := range index {
		store[val] = append(store[val], key)
	}

	result := [][]int{}
	for _, val := range store {
		if len(val) > 1 {
			result = append(result, val)
		}
	}

	d.Output(result, p.output)
}

func (p *FDS) buildIndices() map[int][]int {
	indices := make(map[int][]int)
	for i, val := range p.source {
		if val != -1 {
			indices[val] = append(indices[val], i)
		}
	}

	return indices
}

func (p *FDS) search(index map[int][]int) [][]int {
	result := make([][]int, 0, len(index))
	for _, arr := range index {
		result = append(result, checkTrees(p.source, arr)...)
	}

	return result
}

func checkTrees(tree []int, roots []int) [][]int {
	result := [][]int{}

	for {
		root, roots := roots[0], roots[1:]
		store := []int{root}
		remainder := []int{}

		for _, other := range roots {
			if compareTrees(tree, root, other) {
				store = append(store, other)
			} else {
				remainder = append(remainder, other)
			}
		}

		if len(store) > 1 {
			result = append(result, store)
		}

		if len(remainder) <= 1 {
			break
		}

		roots = remainder
	}

	return result
}

func compareTrees(tree []int, one, two int) bool {
	if one == two {
		return true
	}

	treeOne := []int{one}
	treeTwo := []int{two}
	size := len(tree)

	// fmt.Println("Source roots: ", one, two)

	for len(treeOne) > 0 {
		leftOne, rightOne := getTreeBranches(tree, size, treeOne[0])
		leftTwo, rightTwo := getTreeBranches(tree, size, treeTwo[0])

		// fmt.Println("One: ", leftOne, rightOne, " <--> Two: ", leftTwo, rightTwo)

		if evalTreeNodes(tree, leftOne, leftTwo) && evalTreeNodes(tree, rightOne, rightTwo) {
			treeOne, treeTwo = treeOne[1:], treeTwo[1:]

			if !isLeaf(tree, size, leftOne) {
				treeOne, treeTwo = append(treeOne, leftOne), append(treeTwo, leftTwo)
			}

			if !isLeaf(tree, size, rightOne) {
				treeOne, treeTwo = append(treeOne, rightOne), append(treeTwo, rightTwo)
			}
		} else {
			return false
		}
	}

	return true
}

func getTreeBranches(tree []int, size, index int) (int, int) {
	if index >= size {
		return -1, -1
	}

	left, right := 2*index+1, 2*index+2

	if left >= size {
		return -1, -1
	}

	if right >= size {
		return left, -1
	}

	return left, right
}

func evalTreeNodes(tree []int, one, two int) bool {
	var valOne, valTwo int

	if one == -1 {
		valOne = -1
	} else {
		valOne = tree[one]
	}

	if two == -1 {
		valTwo = -1
	} else {
		valTwo = tree[two]
	}

	return valOne == valTwo
}

func isLeaf(tree []int, size, node int) bool {
	if node == -1 || node >= size {
		return true
	}

	return tree[node] == -1
}

func tokenize(tree []int, index map[int]string, root, size int) (string, map[int]string) {
	if root >= size || root == -1 {
		// not existing node
		return "", index
	}

	if tree[root] == -1 {
		// node itself is a placeholder (aka not existing)
		return "", index
	}

	left, right := 2*root+1, 2*root+2
	if left >= size {
		left = -1
	}

	if right >= size {
		right = -1
	}

	var token, leftToken, rightToken string

	leftToken, index = tokenize(tree, index, left, size)
	rightToken, index = tokenize(tree, index, right, size)

	token = strconv.Itoa(tree[root]) + "," + leftToken + rightToken
	index[root] = token

	return token, index
}
