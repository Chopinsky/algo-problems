package p1

import (
	"fmt"
	"math"
	"sort"
	"strconv"
	"time"

	s "go-problems/shared"
)

// MNVPProblems ...
type MNVPProblems struct {
	set []*MNVP
}

// Solve ...
func (p *MNVPProblems) Solve() {
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

// MNVP ...
type MNVP struct {
	data     [][]int
	location []int
	angle    int
	output   int
}

// CreateMNVP ...
func CreateMNVP() s.Problem {
	set := make([]*MNVP, 0, 4)

	set = append(set, &MNVP{
		data: [][]int{
			{2, 1}, {2, 2}, {3, 3},
		},
		location: []int{1, 1},
		angle:    90,
		output:   3,
	})

	set = append(set, &MNVP{
		data: [][]int{
			{2, 1}, {2, 2}, {3, 4}, {1, 1},
		},
		location: []int{1, 1},
		angle:    90,
		output:   4,
	})

	set = append(set, &MNVP{
		data: [][]int{
			{1, 0}, {2, 1},
		},
		location: []int{1, 1},
		angle:    13,
		output:   1,
	})

	return &MNVPProblems{set}
}

func (p *MNVP) solve() int {
	points, loc, angle := p.data, p.location, float64(p.angle)
	size := len(points)

	if angle == 360.0 {
		return size
	}

	dots := make(map[float64]int)
	count := 0

	var s string
	var a float64

	for _, point := range points {
		x, y := point[0]-loc[0], point[1]-loc[1]
		if x == 0 && y == 0 {
			count++
			continue
		}

		if x == 0 {
			if y > 0 {
				a = 90.0
			} else {
				a = 270.0
			}
		} else if y == 0 {
			if x > 0 {
				a = 0
			} else {
				a = 180.0
			}
		} else {
			s = fmt.Sprintf("%.4f", math.Atan2(float64(y), float64(x))*180.0/3.141593)
			a, _ = strconv.ParseFloat(s, 64)

			if y < 0 || (y == 0 && x < 0) {
				a += 360
			}
		}

		dots[a]++
	}

	// fmt.Println(dots)

	arr := make([][]float64, 0, len(dots))
	for ag, cnt := range dots {
		arr = append(arr, []float64{ag, float64(cnt)})
	}

	sort.Slice(arr, func(i, j int) bool {
		return arr[i][0] < arr[j][0]
	})

	fmt.Println(arr)

	last := len(arr) - 1
	if arr[last][0]-arr[0][0] <= angle {
		return len(points)
	}

	r := 0
	best := count

	for l := 0; l <= last; l++ {
		for {
			diff := arr[r][0] - arr[l][0]
			if diff < 0 {
				diff += 360
			}

			if diff > angle {
				break
			}

			count += int(arr[r][1])
			if count > best {
				best = count
			}

			r++

			if r > last {
				r = 0
			}

			// we can include every points in this range
			if r == l {
				return len(points)
			}
		}

		count -= int(arr[l][1])
	}

	return best
}
