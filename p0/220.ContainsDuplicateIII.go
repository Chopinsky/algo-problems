package p0

import (
	"fmt"
	"sort"
	"time"

	s "go-problems/shared"
)

// CDIIIProblems ...
type CDIIIProblems struct {
	set []*CDIII
}

// Solve ...
func (p *CDIIIProblems) Solve() {
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

// CDIII ...
type CDIII struct {
	data   []int
	output int
}

// CreateCDIII ...
func CreateCDIII() s.Problem {
	set := make([]*CDIII, 0, 4)

	set = append(set, &CDIII{
		data:   []int{},
		output: 0,
	})

	return &CDIIIProblems{set}
}

func (p *CDIII) solve() int {
	return 0
}

func containsNearbyAlmostDuplicate(nums []int, k int, t int) bool {
	if t < 0 {
		return false
	}

	buckets := make(map[int]int)

	for i, v := range nums {
		key := v

		if t > 0 {
			key /= t
		}

		// check if there's a valid buckets in the vicinity
		for m := -1; m <= 1; m++ {
			if j, ok := buckets[key+m]; ok && nums[j]+t >= v && nums[j]-t <= v {
				return true
			}
		}

		// save the key, since it's in range now
		buckets[key] = i

		// revoke the keys that're out of the range
		if i-k >= 0 {
			key = nums[i-k]

			if t > 0 {
				key /= t
			}

			delete(buckets, key)
		}
	}

	return false
}

func containsNearbyAlmostDuplicate1(nums []int, k int, t int) bool {
	if nums == nil || len(nums) < 2 {
		return false
	}

	size := len(nums)
	fen := make([]int, size+1)

	arr := make([][]int, size)
	for i, val := range nums {
		arr[i] = []int{i, val}
	}

	sort.Slice(arr, func(i, j int) bool {
		if arr[i][1] == arr[j][1] {
			return arr[i][0] < arr[j][0]
		}

		return arr[i][1] < arr[j][1]
	})

	fmt.Println(arr)

	l, r := 0, 1
	var ll, lr, d1, d2 int

	updateCDIII(fen, arr[l][0], 1)

	for l < size {
		for r < size && abs(arr[l][1], arr[r][1]) <= t {
			updateCDIII(fen, arr[r][0], 1)
			r++
		}

		ll, lr = arr[l][0]-k, arr[l][0]+k
		if ll < 0 {
			ll = 0
		}

		if lr >= size {
			lr = size - 1
		}

		d1 = queryCDIII(fen, lr) - queryCDIII(fen, arr[l][0]-1)
		d2 = queryCDIII(fen, arr[l][0]) - queryCDIII(fen, ll-1)

		fmt.Println(l, r-1, "-", ll, arr[l][0], d2, ";", arr[l][0], lr, d1, ";")

		if d1 > 1 || d2 > 1 {
			return true
		}

		updateCDIII(fen, arr[l][0], -1)
		l++
	}

	return false
}

func abs(a, b int) int {
	ans := a - b

	if ans < 0 {
		return -ans
	}

	return ans
}

func updateCDIII(arr []int, idx, val int) {
	idx++

	for idx < len(arr) {
		arr[idx] += val
		idx += (idx & -idx)
	}
}

func queryCDIII(arr []int, idx int) int {
	if idx < 0 {
		return 0
	}

	sum := 0
	idx++

	for idx > 0 {
		sum += arr[idx]
		idx -= (idx & -idx)
	}

	return sum
}
