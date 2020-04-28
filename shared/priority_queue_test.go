package shared

import (
	"sort"
	"testing"
)

type TestNode struct {
	val int
	pos int
}

var maxQueue = true

// a maximum queue
func (s TestNode) Less(t Compare) bool {
	if maxQueue {
		return s.val > t.(TestNode).val		
	}

	return s.val < t.(TestNode).val
}

func TestMaxPQ(t *testing.T) {
	runTest(t)
}

func TestMinPQ(t *testing.T) {
	maxQueue = false
	runTest(t)
}

func runTest(t *testing.T) {
	src := []int{42, 1, 98, 7, 29, 4, 13, 11, 83}
	tgt := append([]int(nil), src...)
	
	// use correct sort for comparison
	sort.Slice(tgt, func (i, j int) bool {
		if maxQueue {
			return tgt[i] > tgt[j]			
		}

		return tgt[i] < tgt[j]
	})

	pq := PriorityQueueInit(len(src))

	for i := 0; i < len(src); i++ {
		pq.Push(TestNode{
			val: src[i],
			pos: i,
		})
	}

	idx := 0
	
	for pq.Len() > 0 {
		top := pq.Pop().(TestNode).val

		if top != tgt[idx] {
			t.Errorf("top value: %d; want %d", top, tgt[idx])
		}

		idx++
	}
}

