package challenges

import "sort"

// MyCalendarThree ...
type MyCalendarThree struct {
	start []int
	end   []int
}

// MCConstructor ...
func MCConstructor() MyCalendarThree {
	return MyCalendarThree{
		start: make([]int, 0, 48),
		end:   make([]int, 0, 48),
	}
}

// Book ...
func (t *MyCalendarThree) Book(start int, end int) int {

	ps := sort.SearchInts(t.start, start)
	pe := sort.SearchInts(t.end, end)

	t.start = append(t.start, 0)
	t.end = append(t.end, 0)

	if ps < len(t.start)-1 {
		copy(t.start[ps+1:], t.start[ps:])
	}

	if pe < len(t.end) {
		copy(t.end[pe+1:], t.end[pe:])
	}

	t.start[ps] = start
	t.end[pe] = end

	var i, j, ans, size int

	for i < len(t.start) {
		if t.start[i] < t.end[j] {
			size++
			i++

			if size > ans {
				ans = size
			}
		} else {
			size--
			j++
		}
	}

	return ans
}
