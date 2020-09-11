package p0

import (
	"container/heap"
	"fmt"
	"sort"
)

// Algo -- Lego stack:
//   0) assumption: in the lego stack below, all of the courses scheduled
//   are valid, and they will stay valid even if moved to an earlier date.
//        |__ C1 __|_____ C2 _____|_ C3 _| (valid)
//            => (replace C2 with a shorter course C4)
//        |__ C1 __|___ C4 ___|_ C3 _| (still valid)
//
//   1) sort courses such that we will consider courses ends first first
//   2) if the last available date + the course length <= the deadline date,
//      add the course to the tail of the Lego stack
//   3) if the course is shorter than the longest course in the stack,
//      we can replace that course with this shorter one, and the stack
//      is still valid, the course count won't change, but the last available
//      date can be dialed back by
//                  `thisCourseDuration - longestCourseDuration`
//      and this will help us to take more future courses
func scheduleCourse(courses [][]int) int {
	sort.Slice(courses, func(i, j int) bool {
		return courses[i][1] < courses[j][1]
	})

	h := make(MaxHeap, 0, len(courses))
	lastDay := 0
	count := 0

	for _, c := range courses {
		if lastDay+c[0] <= c[1] {
			// we can take this course with current conditions
			lastDay += c[0]
			count++

			// record the course and add it to the max-heap
			heap.Push(&h, c[0])
		} else if h.Len() > 0 && h[0] > c[0] {
			// we can make the last days moving backwards, do so
			longest := heap.Pop(&h).(int)
			lastDay += c[0] - longest

			// replacement is valid, because the replaced course has an earlier
			// deadline than this course, we're good for the deadlines.
			heap.Push(&h, c[0])
		}
	}

	return count
}

// MaxHeap ...
type MaxHeap []int

func (h MaxHeap) Less(i, j int) bool {
	return h[i] > h[j]
}

func (h MaxHeap) Len() int {
	return len(h)
}

func (h MaxHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

// Push ...
func (h *MaxHeap) Push(v interface{}) {
	*h = append(*h, v.(int))
}

// Pop ...
func (h *MaxHeap) Pop() interface{} {
	x := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]

	return x
}

func scheduleCourse1(courses [][]int) int {
	sort.Slice(courses, func(i, j int) bool {
		if courses[i][1] == courses[j][1] {
			return courses[i][0] > courses[j][0]
		}

		return courses[i][1] < courses[j][1]
	})

	size := len(courses)
	best, start := 1, 0
	dp := make([]int, size+1)

	for i := 0; i < size; i++ {
		if courses[i][1]-courses[i][0] < 0 {
			continue
		}

		dp[1] = courses[i][0]
		start = i + 1
		break
	}

	for i := start; i < size; i++ {
		if courses[i][1]-courses[i][0] <= 0 {
			continue
		}

		top := searchCSIII(dp, courses[i][1]-courses[i][0], size)

		s := top + 1
		if s > size {
			s = size
		}

		for j := s; j > 0; j-- {
			if dp[j] == 0 || dp[j-1]+courses[i][0] < dp[j] {
				dp[j] = dp[j-1] + courses[i][0]

				if j > best {
					best = j
				}
			}
		}
	}

	fmt.Println(courses, dp)

	return best
}

func searchCSIII(dp []int, th, size int) int {
	l, r := 1, size

	for l < r {
		m := (l + r) / 2

		if dp[m] == 0 || dp[m] > th {
			r = m - 1
		} else {
			l = m + 1
		}
	}

	if dp[l] == 0 || dp[l] > th {
		if l > 0 {
			return l - 1
		}

		return 0
	}

	return l
}
