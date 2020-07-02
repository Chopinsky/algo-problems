package p1

import (
	"fmt"
	"math"
	"time"

	s "go-problems/shared"
)

// MVEProblems ...
type MVEProblems struct {
	set []*MVE
}

// Solve ...
func (p *MVEProblems) Solve() {
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

// MVE ...
type MVE struct {
	data   [][]int
	k      int
	output int
}

// CreateMVE ...
func CreateMVE() s.Problem {
	set := make([]*MVE, 0, 4)

	set = append(set, &MVE{
		data: [][]int{
			{1, 3}, {2, 0}, {5, 10}, {6, -10},
		},
		k:      1,
		output: 4,
	})

	set = append(set, &MVE{
		data: [][]int{
			{0, 0}, {3, 0}, {9, 2},
		},
		k:      3,
		output: 3,
	})

	set = append(set, &MVE{
		data: [][]int{
			{1, 2}, {2, 4}, {3, 6}, {4, 8}, {5, 8}, {6, 9},
		},
		k:      1,
		output: 18,
	})

	return &MVEProblems{set}
}

func (p *MVE) solve() int {
	d, k := p.data, p.k
	size := len(d)
	best := int(math.MinInt32)

	q := make([][]int, 0, size)
	q = append(q, []int{d[0][0], d[0][1] - d[0][0]})

	for i := 1; i < size; i++ {
		val := d[i][1] - d[i][0]
		pos := len(q)

		for j := 0; j < len(q); j++ {
			if d[i][0]-q[j][0] <= k {
				pos = j
				break
			}
		}

		if pos < len(q) {
			res := d[i][0] + d[i][1] + q[pos][1]
			if res > best {
				best = res
			}
		}

		if pos > 0 {
			q = q[pos:]
		}

		if len(q) == 0 || val < q[len(q)-1][1] {
			q = append(q, []int{d[i][0], val})
		} else {
			pos = -1
			for j := len(q) - 2; j >= 0; j-- {
				if val < q[j][1] {
					pos = j + 1
					break
				}
			}

			q[pos+1][0] = d[i][0]
			q[pos+1][1] = val
			q = q[:pos+2]
		}
	}

	return best
}

func (p *MVE) solve1() int {
	d, k, size := p.data, p.k, len(p.data)
	q := make([][]int, 0, size)

	last, curr, next := 0, 1, 1
	best := int(math.MinInt32)

	var dist, offset, upper int

	// add the first batch of the points met the critiria
	for {
		for d[next][0]-d[last][0] <= k {
			dist = calcDist(d[last], d[next])

			if dist > best {
				best = dist
			}

			q = fix(q, next, dist)
			next++
		}

		if len(q) > 0 {
			break
		}

		last++
		curr = last + 1
		next = curr
	}

	// moving to the next ones
	for curr < size {
		offset = 0

		// make sure that the next point can only make the value larger
		for curr < size && curr <= next {
			offset = calcOffset(d[last], d[curr])
			if offset >= 0 {
				break
			}

			curr++
		}

		// we're at the end of the points set, done
		if curr >= size {
			// fmt.Println(last, curr, next)
			return best
		}

		upper = -1
		next = -1

		// now clearning up the queue, pop all points left to the current one,
		// and updating the remainder ones with the offset; also set the starter
		// point for the next iteration
		for i := len(q) - 1; i >= 0; i-- {
			if q[i][0] <= curr {
				upper = i
				break
			} else {
				q[i][1] += offset

				if next < 0 {
					next = q[i][0] + 1
				}

				if q[i][1] > best {
					best = q[i][1]
				}
			}
		}

		// pop out points in the queue to the left
		if upper >= 0 {
			q = q[upper:]
		}

		if next < 0 {
			next = curr + 1
		}

		// now feed the queue with the next batch of points within the k distance
		// along the x-axis
		for next < size && d[next][0]-d[curr][0] <= k {
			dist = calcDist(d[curr], d[next])

			if dist > best {
				best = dist
			}

			q = fix(q, next, dist)
			next++
		}

		last = curr
		curr++
	}

	// fmt.Println(last, curr, next)
	return best
}

func calcDist(a, b []int) int {
	return b[0] - a[0] + b[1] + a[1]
}

func calcOffset(a, b []int) int {
	return b[1] - a[1] - (b[0] - a[0])
}

func fix(q [][]int, pos, val int) [][]int {
	size := len(q)
	if size == 0 || q[size-1][1] > val {
		q = append(q, []int{pos, val})
		return q
	}

	i := size - 2
	for i >= 0 {
		if q[i][1] <= val {
			i--
			continue
		}
	}

	q[i+1] = []int{pos, val}
	q = q[:i+1]

	return q
}
