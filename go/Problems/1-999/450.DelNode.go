package problems

import (
	"fmt"
)

var size int

// DN ...
type DN struct {
	source []int
	key    int
	output [][]int
}

// CreateDN ...
func CreateDN() *DN {
	return &DN{}
}

// Build ...
func (p *DN) Build(test int) {
	switch test {
	case 1:
		p.source = []int{8, 3, 9, 2, 6, -1, 10, -1, -1, 4, 7, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5}
		p.key = 3
		p.output = [][]int{
			{8, 4, 9, 2, 6, -1, 10, -1, -1, 5, 7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
			{8, 2, 9, -1, 6, -1, 10, -1, -1, 4, 7, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5},
		}

	default:
		p.source = []int{5, 3, 6, 2, 4, -1, 7}
		p.key = 3
		p.output = [][]int{
			{5, 4, 6, 2, -1, -1, 7},
			{5, 2, 6, -1, 4, -1, 7},
		}

	}
}

// Run ...
func (p *DN) Run() {
	size = len(p.source)
	var idx, left, right int

	for {
		if p.key == p.source[idx] {
			p.source[idx] = p.getLeaf(idx)
			break
		}

		left = p.leftChild(idx)
		right = p.rightChild(idx)

		if left < 0 && right < 0 {
			// at the leaf, no match
			break
		}

		if p.key < p.source[idx] {
			if left < 0 {
				// no match
				break
			} else {
				idx = left
			}
		} else {
			if right < 0 {
				// no match
				break
			} else {
				idx = right
			}
		}
	}

	fmt.Println("Calculated result: \n- ", p.source)
	fmt.Println("\nPossible expected results: ")

	for _, vals := range p.output {
		fmt.Println("- ", vals)
	}
}

func (p *DN) getLeaf(index int) int {
	left := p.leftChild(index)
	right := p.rightChild(index)

	if right < 0 && left < 0 {
		return -1
	}

	var res int
	if right < 0 {
		res = p.source[left]
		p.shift(left, index)
		return res
	}

	if left < 0 {
		res = p.source[right]
		p.shift(right, index)
		return res
	}

	// left and right children both exist
	index = right
	for {
		left = p.leftChild(index)

		if left < 0 {
			// reaching the smallest element in the right sub-tree
			res = p.source[index]

			right = p.rightChild(index)
			if right < 0 {
				// we're at leaf, again
				p.source[index] = -1
			} else {
				// otherwise, shift the right tree up
				p.shift(right, index)
			}

			break
		}

		// go left if it exists
		index = left
	}

	return res
}

func (p *DN) shift(old, new int) {
	p.source[new] = p.source[old]
	p.source[old] = -1

	oldLeft := p.leftChild(old)
	newLeft := p.leftChild(new)

	if oldLeft >= 0 {
		p.shift(oldLeft, newLeft)
	} else if newLeft >= 0 {
		p.source[newLeft] = -1
	}

	oldRight := p.rightChild(old)
	newRight := p.rightChild(new)

	if oldRight >= 0 {
		p.shift(oldRight, newRight)
	} else if newRight >= 0 {
		p.source[newRight] = -1
	}
}

func (p *DN) leftChild(curr int) int {
	res := (curr+1)*2 - 1
	if res >= size {
		return -1
	}

	if p.source[res] < 0 {
		return -1
	}

	return res
}

func (p *DN) rightChild(curr int) int {
	res := (curr + 1) * 2
	if res >= size {
		return -1
	}

	if p.source[res] < 0 {
		return -1
	}

	return res
}

func getParent(curr int) int {
	return (curr+1)/2 - 1
}
