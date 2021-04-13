package p1

import (
	"fmt"
	"sort"
	"time"

	s "go-problems/shared"
)

// ClSSProblems ...
type ClSSProblems struct {
	set []*ClSS
}

// Solve ...
func (p *ClSSProblems) Solve() {
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

// ClSS ...
type ClSS struct {
	data   []int
	goal   int
	output int
}

// CreateClSS ...
func CreateClSS() s.Problem {
	set := make([]*ClSS, 0, 4)

	set = append(set, &ClSS{
		data:   []int{5, -7, 3, 5},
		goal:   6,
		output: 0,
	})

	set = append(set, &ClSS{
		data:   []int{7, -9, 15, -2},
		goal:   -5,
		output: 1,
	})

	set = append(set, &ClSS{
		data:   []int{1, 2, 3},
		goal:   -7,
		output: 7,
	})

	return &ClSSProblems{set}
}

// similar algo as solve1, just another way of looking at it
func (p *ClSS) solve() int {
	size := len(p.data)
	goal := p.goal

	if size == 1 {
		return min(goal, absDiff(goal, p.data[0]))
	}

	l, r := p.data[:(size/2)], p.data[(size/2):]

	lsums := make(map[int]bool, (1 << len(l)))
	rsums := make(map[int]bool, (1 << len(r)))

	enum(lsums, l)
	enum(rsums, r)

	// fmt.Println(l, lsums, r, rsums)

	tgt := make([]int, 0, len(rsums))
	ans := absDiff(goal, 0)

	// only a subsequence from left
	for k := range lsums {
		diff := absDiff(goal, k)
		if diff < ans {
			ans = diff
		}
	}

	// only a subsequence from right
	for k := range rsums {
		tgt = append(tgt, k)

		diff := absDiff(goal, k)
		if diff < ans {
			ans = diff
		}
	}

	sort.Ints(tgt)

	// a combined subsequence from left and right
	for k := range lsums {
		num := goal - k
		idx := sort.SearchInts(tgt, num)

		if idx < len(tgt) {
			diff := absDiff(goal, k+tgt[idx])
			if diff < ans {
				ans = diff
			}
		}

		if idx > 0 {
			diff := absDiff(goal, k+tgt[idx-1])
			if diff < ans {
				ans = diff
			}
		}
	}

	return ans
}

func enum(sums map[int]bool, nums []int) {
	tmp := make([]int, 0, len(nums))

	for _, val := range nums {
		for k := range sums {
			tmp = append(tmp, k+val)
		}

		for _, v := range tmp {
			sums[v] = true
		}

		tmp = tmp[:0]
		sums[val] = true
	}
}

func (p *ClSS) solve1() int {
	nums := p.data
	goal := p.goal

	if goal == 0 {
		return 0
	}

	var taken int64
	sort.Ints(nums)

	ans := []int{absDiff(0, goal)}
	visited := make(map[int64]bool)
	size := len(nums)

	for i := range nums {
		taken = 0
		taken |= int64(1 << i)

		minDiff(nums, ans, visited, taken, nums[i], goal, size)

		if ans[0] == 0 {
			break
		}
	}

	return ans[0]
}

func minDiff(nums, ans []int, visited map[int64]bool, taken int64, sum, goal, size int) {
	if ans[0] == 0 || visited[taken] {
		return
	}

	var diff int
	visited[taken] = true

	bench := absDiff(sum, goal)
	r := sort.SearchInts(nums, goal-sum)
	l := r - 1

	for l >= 0 || r < size {
		if l >= 0 {
			diff = absDiff(sum+nums[l], goal)

			if diff <= bench {
				if taken&int64(1<<l) == 0 {
					if diff < ans[0] {
						ans[0] = diff
					}

					minDiff(nums, ans, visited, taken|int64(1<<l), sum+nums[l], goal, size)
					l = -1
				} else {
					l--
				}
			} else {
				// won't get a better solution
				l = -1
			}
		}

		if r < size {
			diff = absDiff(sum+nums[r], goal)

			if diff <= bench {
				if taken&int64(1<<r) == 0 {
					if diff < ans[0] {
						ans[0] = diff
					}

					minDiff(nums, ans, visited, taken|int64(1<<r), sum+nums[r], goal, size)
					r = size
				} else {
					r++
				}
			} else {
				// won't get a better solution
				r = size
			}
		}
	}
}

func absDiff(a, b int) int {
	val := a - b
	if val < 0 {
		return -val
	}

	return val
}
