package problems

import (
	"fmt"
	"sort"

	d "../../Utils"
)

// MAI ...
type MAI struct {
	source    []int
	comp      []int
	output    int
	testCount int
}

// CreateMAI ...
func CreateMAI() *MAI {
	return &MAI{}
}

// Build ...
func (p *MAI) Build(test int) {
	p.ResetGlobals()
	p.testCount = 6

	switch test {
	case 1:
		p.source = []int{1, 5, 3, 6, 7}
		p.comp = []int{4, 3, 1}
		p.output = 2

	case 2:
		p.source = []int{1, 5, 3, 6, 7}
		p.comp = []int{1, 6, 3, 3}
		p.output = -1

	case 3:
		p.source = []int{7, 8, 4, 5, 6}
		p.comp = []int{4, 2, 1, 9}
		p.output = 2

	case 4:
		p.source = []int{1, 3, 4, 7, 6}
		p.comp = []int{1, 2, 3, 4, 9}
		p.output = 1

	case 5:
		p.source = []int{5, 3, 4, 7, 6, 12}
		p.comp = []int{2, 3, 4, 9}
		p.output = 2

	default:
		p.source = []int{1, 5, 3, 6, 7}
		p.comp = []int{1, 3, 2, 4}
		p.output = 1

	}
}

const upperBound = 1000000001

var upperCache map[int]int
var lowerCache map[int]int

// ResetGlobals ...
func (p *MAI) ResetGlobals() {
	// upperCache = make(map[int]int)
	// lowerCache = make(map[int]int)
}

// Run ...
func (p *MAI) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)
			sort.Ints(p.comp)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")

				// d.Output(p.findResult(), p.output)
				d.Output(runMAI2(p.source, p.comp), p.output)
			} else {
				// p.findResult()
				runMAI2(p.source, p.comp)
			}
		}
	}
}

type alt struct {
	ops   int
	start int
	last  int
}

func runMAI2(src, comp []int) int {
	if len(src) <= 1 {
		return 0
	}

	upperCache = make(map[int]int)
	root, size, result := buildTree(comp), len(src), -1
	alts := make([]*alt, 0, size*len(comp))

	var max, sub int
	var cur *alt

	alts = append(alts, &alt{
		ops:   0,
		start: size - 1,
		last:  upperBound,
	})

	for len(alts) > 0 {
		cur, alts = alts[0], alts[1:]

		pos := cur.start
		last := cur.last

		for {
			if pos == -1 {
				// reaching a valid solution, check with the bench and update it
				if result == -1 {
					result = cur.ops
				} else if cur.ops < result {
					result = cur.ops
				}

				break
			}

			if (pos == size-1 || src[pos] < last) && (pos == 0 || src[pos] > src[pos-1]) {
				// a valid value
				last = src[pos]
				pos--
				continue
			}

			// the current stream is to update the position
			if pos == size-1 {
				max = upperBound
			} else {
				max = last
			}

			sub = root.findUpper(max)
			if sub == -1 {
				// we can't find a substitute given the current stream
				break
			}

			if pos == size-1 || src[pos] < last {
				// this op can delay to the left elem
				alts = append(alts, &alt{
					ops:   cur.ops,
					start: pos - 1,
					last:  src[pos],
				})
			}

			cur.ops++
			last = sub
			pos--
		}
	}

	return result
}

type op struct {
	pos    int
	srcVal int
}

func (p *MAI) findResult() int {
	result := -1

	for bound := len(p.comp) - 1; bound >= 0; bound-- {
		comp := p.comp[bound:]
		src := append([]int(nil), p.source...)
		upperCache = make(map[int]int)

		temp := runMAI(src, comp)

		if d.DEBUG {
			fmt.Println(src, temp)
		}

		if result == -1 && temp != -1 {
			result = temp
			break
		}
	}

	return result
}

func runMAI(src, comp []int) int {
	if len(src) <= 1 {
		return 0
	}

	root, size := buildTree(comp), len(src)
	ops := make([]*op, 0, size)
	pos := size - 1

	var max int
	var curOp *op

	for {
		if pos < 0 {
			// we've found the solution
			if d.DEBUG {
				fmt.Println("Final: ", src)
			}

			return len(ops)
		}

		if pos >= size {
			// can't find a solution
			return -1
		}

		if (pos == size-1 && src[pos] < upperBound) || (pos < size-1 && src[pos] < src[pos+1]) {
			// a valid value, continue
			pos--
			continue
		}

		if pos == size-1 {
			max = upperBound
		} else {
			max = src[pos+1]
		}

		sub := findSub(root, max, src[pos])

		if sub == -1 {
			idx := len(ops) - 1
			if idx < 0 {
				// nothing to backtrace, we're doomed
				return -1
			}

			var restore *op
			for {
				restore, ops = ops[idx], ops[:idx]
				if restore.pos == size-1 {
					// nowhere to back off from, no answer
					return -1
				}

				// restore the value changed by the operation
				src[restore.pos] = restore.srcVal
				idx--

				// break if we've reached a new trial location
				if idx < 0 || restore.pos+1 != ops[idx].pos {
					pos = restore.pos + 1
					src[pos] = upperBound // a fake value, so we will trigger an update @ this position
					break
				}
			}
		} else {
			curOp = &op{
				pos:    pos,
				srcVal: src[pos],
			}

			// save off the operations and update the array
			ops = append(ops, curOp)
			src[pos] = sub

			// moving on to the next position
			pos--
		}
	}
}

func findSub(root *rngTree, max, src int) int {
	if src < 0 {
		return -1
	}

	var res int

	for {
		res = root.findUpper(max)
		if res != src {
			return res
		}

		max = res
	}
}

type rngTree struct {
	val   int
	left  *rngTree
	right *rngTree
}

func buildTree(src []int) *rngTree {
	var root *rngTree
	for i := range src {
		if root != nil {
			root.insert(src[i])
		} else {
			root = &rngTree{
				val:   src[i],
				left:  nil,
				right: nil,
			}
		}
	}

	return root
}

func (t *rngTree) findUpper(max int) int {
	if d.DEBUG {
		fmt.Println("At: ", t.val, "with", max, t.left, t.right)
	}

	if max < 0 {
		return -1
	}

	if val, ok := upperCache[max]; ok {
		return val
	}

	result := -1
	if t.val < max {
		fromChild := -1
		if t.right != nil {
			fromChild = t.right.findUpper(max)
		}

		if fromChild != -1 && fromChild > t.val {
			result = fromChild
		} else {
			result = t.val
		}
	} else if t.left != nil {
		result = t.left.findUpper(max)
	}

	upperCache[max] = result

	return result
}

func (t *rngTree) findLower(min int) int {
	if d.DEBUG {
		fmt.Println("At: ", t.val, "with", min, t.left, t.right)
	}

	if min < 0 {
		return -1
	}

	if val, ok := lowerCache[min]; ok {
		return val
	}

	result := -1
	if t.val > min {
		fromChild := -1
		if t.left != nil {
			fromChild = t.left.findLower(min)
		}

		if fromChild != -1 && fromChild < t.val {
			result = fromChild
		} else {
			result = t.val
		}
	} else if t.right != nil {
		result = t.right.findLower(min)
	}

	lowerCache[min] = result

	return result
}

func (t *rngTree) insert(val int) {
	if t.val == val {
		return
	}

	if t.val > val {
		if t.left != nil {
			t.left.insert(val)
		} else {
			t.left = &rngTree{
				val:   val,
				left:  nil,
				right: nil,
			}
		}

		return
	}

	if t.val < val {
		if t.right != nil {
			t.right.insert(val)
		} else {
			t.right = &rngTree{
				val:   val,
				left:  nil,
				right: nil,
			}
		}

		return
	}
}
