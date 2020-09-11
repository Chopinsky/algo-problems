package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// NGLNPProblems ...
type NGLNPProblems struct {
	set []*NGLNP
}

// Solve ...
func (p *NGLNPProblems) Solve() {
	fmt.Println()

	start := time.Now()

	for j := 0; j <= 0; j++ {
		for i, p := range p.set {
			result := p.solve()

			if j == 0 {
				s.Print(i, p.output, result)
			}
		}
	}

	fmt.Println("Algorithm finished in:", time.Since(start))
}

// NGLNP ...
type NGLNP struct {
	data   *treeNode
	dist   int
	output int
}

// CreateNGLNP ...
func CreateNGLNP() s.Problem {
	set := make([]*NGLNP, 0, 4)

	set = append(set, &NGLNP{
		data: &treeNode{
			val:   1,
			left:  &treeNode{val: 1},
			right: &treeNode{val: 1},
		},
		dist:   2,
		output: 1,
	})

	return &NGLNPProblems{set}
}

type treeNode struct {
	left  *treeNode
	right *treeNode
	val   int
}

func (p *NGLNP) solve() int {
	count, _ := countPairs(p.data, p.dist)
	return count
}

func countPairs(root *treeNode, dist int) (int, []int) {
	m := make([]int, 11)
	count := 0

	if root.left == nil && root.right == nil {
		m[1] = 1
		return 0, m
	}

	var cl, cr int
	var ml, mr []int

	if root.left != nil {
		cl, ml = countPairs(root.left, dist)
	}

	if root.right != nil {
		cr, mr = countPairs(root.right, dist)
	}

	count += cl
	count += cr

	for i := 1; i < 11; i++ {
		lnum := getSum(ml, i-1, i)

		if lnum == 0 {
			continue
		}

		val := lnum * getSum(mr, 0, dist-i)

		count += val
		m[i+1] += m[i] + lnum + getSum(mr, i-1, i)
	}

	return count, m
}

func getSum(src []int, i, j int) int {
	return src[j] - src[i]
}
