package problems

import (
	"sort"

	d "../../Utils"
)

// CSN ...
type CSN struct {
	source []int
	output []int
}

type csnNode struct {
	num   int
	pos   int
	count int
	next  *csnNode
}

// CreateCSN ...
func CreateCSN() *CSN {
	return &CSN{}
}

// Build ...
func (p *CSN) Build(test int) {
	switch test {
	case 1:
		p.source = []int{7, 1, 3, 2, 9, 2, 1}
		p.output = []int{5, 0, 3, 1, 2, 1, 0}

	default:
		p.source = []int{5, 2, 1, 6, 0, 1}
		p.output = []int{4, 3, 1, 2, 0, 0}

	}
}

// Run ...
func (p *CSN) Run() {
	d.Output(p.count2(), p.output)
}

func (p *CSN) count() []int {
	var head *csnNode
	size := len(p.source)

	for i := size - 1; i >= 0; i-- {
		head = insrtCsnNode(head, &csnNode{
			num:   p.source[i],
			pos:   i,
			count: 0,
			next:  nil,
		})
	}

	result := make([]int, size)
	curr := head

	for curr != nil {
		result[curr.pos] = curr.count
		curr = curr.next
	}

	d.Debug(result, 0)

	return result
}

func insrtCsnNode(head, newNode *csnNode) *csnNode {
	if head == nil {
		return newNode
	}

	if newNode.num < head.num {
		newNode.next = head
		return newNode
	}

	curr := head
	count := 0
	var last *csnNode

	for curr != nil {
		if curr.num > newNode.num {
			break
		} else if curr.num < newNode.num {
			count++
		}

		last = curr
		curr = curr.next
	}

	// update the chain
	last.next = newNode
	newNode.next = curr
	newNode.count = count

	// still the head
	return head
}

func (p *CSN) count1() []int {
	size := len(p.source)
	result := make([]int, size)

	store := make(map[int]int)
	for i := size - 1; i >= 0; i-- {
		store[p.source[i]]++
		result[i] = countSmaller(store, p.source[i])
	}

	return result
}

func countSmaller(s map[int]int, num int) int {
	count := 0
	for k, v := range s {
		if k < num {
			count += v
		}
	}

	return count
}

func (p *CSN) count2() []int {
	temp := append([]int(nil), p.source...)
	sort.SliceStable(temp, func(i, j int) bool {
		return temp[i] < temp[j]
	})

	ranks := make(map[int]int)
	skipped := 0
	for i, val := range temp {
		if _, ok := ranks[val]; ok {
			skipped++
		} else {
			ranks[val] = i - skipped
		}
	}

	size := len(p.source)
	// rankAry := make([]int, size)
	rankTree := d.BuildTree(make([]int, size))
	result := make([]int, size)

	for i := size - 1; i >= 0; i-- {
		if rankPos, ok := ranks[p.source[i]]; ok {
			// rankAry[rankPos]++
			// result[i] = countFreq(rankAry, rankPos)

			rankTree.UpdateWithDiff(rankPos, 1)
			result[i] = rankTree.Query(rankPos)
		}
	}

	return result
}

func countFreq(r []int, pos int) int {
	count := 0
	for i := 0; i < pos; i++ {
		count += r[i]
	}

	return count
}
