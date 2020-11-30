package challenges

import (
	"container/heap"
)

/**
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

Buildings Skyline Contour:

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
*/

// idea is that assuming we have 2 arrays of the sorted skylines already,
// now use "merge-sort" to merge the skylines together: we pick the
// left-most point from each of the left-half-array and right-half-array,
// then choose the tallest buildings as the profile, and compare the
// next profile pairs, until the merge is complete
func getSkyline(b [][]int) [][]int {
	if len(b) > 1 {
		m := len(b) / 2
		return mergeSkyline(getSkyline(b[:m]), getSkyline(b[m:]))
	}

	if len(b) == 0 {
		return [][]int{}
	}

	return [][]int{{b[0][0], b[0][2]}, {b[0][1], 0}}
}

func mergeSkyline(a, b [][]int) [][]int {
	if len(a) == 0 {
		return b
	}

	if len(b) == 0 {
		return a
	}

	var ai, bi, ah, bh, x int
	var res [][]int

	for ai < len(a) && bi < len(b) {
		if a[ai][0] == b[bi][0] {
			x = a[ai][0]
			ah, bh = a[ai][1], b[bi][1]
			ai++
			bi++
		} else if a[ai][0] < b[bi][0] {
			x = a[ai][0]
			ah = a[ai][1]
			ai++
		} else {
			x = b[bi][0]
			bh = b[bi][1]
			bi++
		}

		h := max(ah, bh)

		if len(res) == 0 || h != res[len(res)-1][1] {
			res = append(res, []int{x, h})
		}
	}

	for i := ai; i < len(a); i++ {
		res = append(res, a[i])
	}

	for i := bi; i < len(b); i++ {
		res = append(res, b[i])
	}

	return res
}

func getSkyline1(buildings [][]int) [][]int {
	size := len(buildings)
	if size == 0 {
		return [][]int{}
	}

	if size == 1 {
		return [][]int{{buildings[0][0], buildings[0][2]}, {buildings[0][1], 0}}
	}

	q := make(queue, 0, size)
	p := make([][]int, 0, size)

	for _, b := range buildings {
		q.Push(b)
	}

	for q.Len() > 0 {
		line := q.Pop().([]int)
		idx := len(p) - 1

		if idx < 0 {
			p = append(p, line)
			continue
		}

		for idx >= 0 {
			// existing buildings have the same hight, extend the profile
			if p[idx][1] >= line[0] && p[idx][2] == line[2] {
				// fmt.Println("equal height:", line, p[idx])
				p[idx][1] = max(p[idx][1], line[1])
				break
			}

			if p[idx][1] <= line[0] {
				p = append(p, line)
				break
			}

			// existing buildings are taller
			if p[idx][2] > line[2] {
				// fmt.Println("taller:", line, p[idx])

				if p[idx][1] >= line[1] {
					break
				}

				if p[idx][1] > line[0] {
					line[0] = p[idx][1]
				}

				p = append(p, line)
				break
			}

			/* last building is shorter */

			// fmt.Println("shorter:", line, p[idx])

			if p[idx][1] > line[1] {
				// stick out more, put the sticked out part into the queue
				q.Push([]int{line[1], p[idx][1], p[idx][2]})
			}

			if p[idx][0] < line[0] {
				p[idx][1] = line[0]
				p = append(p, line)
				break
			}

			// pop the last seg, as it's not going to be blocked
			p = p[:idx]
			idx--
		}

		// fmt.Println(line, p)
	}

	// fmt.Println("stack:", p)

	ans := make([][]int, 0, len(p))

	for i, b := range p {
		if i > 0 {
			if p[i-1][1] != b[0] {
				ans = append(ans, []int{p[i-1][1], 0})
			}

			if b[0] != b[1] {
				ans = append(ans, []int{b[0], b[2]})
			}

		} else {
			ans = append(ans, []int{b[0], b[2]})
		}

		if i+1 == len(p) {
			ans = append(ans, []int{b[1], 0})
		}
	}

	return ans
}

type queue [][]int

func (pq queue) Len() int {
	return len(pq)
}

func (pq queue) Less(i, j int) bool {
	if pq[i][0] == pq[j][0] {
		return pq[i][2] > pq[j][2]
	}

	return pq[i][0] < pq[j][0]
}

// Swap ...
func (pq queue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}

// Push ...
func (pq *queue) Push(val interface{}) {
	n := len(*pq)
	item := val.([]int)

	*pq = append(*pq, item)
	heap.Fix(pq, n)
}

// Pop ...
func (pq *queue) Pop() interface{} {
	old := *pq
	n := len(old)

	item := old[0]
	old[0] = old[n-1]
	old[n-1] = nil

	*pq = old[:n-1]
	heap.Fix(pq, 0)

	return item
}
