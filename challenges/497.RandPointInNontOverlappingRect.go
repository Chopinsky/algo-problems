package challenges

import (
	"fmt"
	"math/rand"
)

// Solution ...
type Solution struct {
	rects  [][]int
	points []int
	last   int
	r1     *rand.Rand
}

// RPNConstructor ...
func RPNConstructor(rects [][]int) Solution {
	r1 := rand.New(rand.NewSource(42))
	size := len(rects)
	points := make([]int, size+1)

	for i := range rects {
		rect := rects[i]
		points[i+1] = points[i] + (rect[2]-rect[0]+1)*(rect[3]-rect[1]+1)
	}

	fmt.Println(points)

	return Solution{
		rects:  rects,
		points: points,
		last:   points[size],
		r1:     r1,
	}
}

// Pick ...
func (t *Solution) Pick() []int {
	size := len(t.rects)

	if size == 0 {
		return []int{}
	}

	var rect []int
	var x, y int

	if size == 1 {
		rect = t.rects[0]
	} else {
		p := t.r1.Intn(t.last)

		if p == 0 || p < t.points[1] {
			rect = t.rects[0]
		} else if p >= t.points[size-1] {
			rect = t.rects[size-1]
		} else {
			l, r := 0, size

			for l < r {
				m := (l + r) / 2

				if p >= t.points[m] && p < t.points[m+1] {
					l = m
					break
				}

				if p < t.points[m] {
					r = m - 1
				} else if p >= t.points[m+1] {
					l = m + 1
				}
			}

			rect = t.rects[l]
		}
	}

	if rect[0] == rect[2] {
		x = rect[0]
	} else {
		x = rect[0] + t.r1.Intn(rect[2]-rect[0]+1)
	}

	if rect[1] == rect[3] {
		y = rect[1]
	} else {
		y = rect[1] + t.r1.Intn(rect[3]-rect[1]+1)
	}

	return []int{x, y}
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(rects);
 * param_1 := obj.Pick();
 */
