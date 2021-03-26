package challenges

// RecentCounter ...
type RecentCounter struct {
	stack []int
}

// NoRConstructor ...
func NoRConstructor() RecentCounter {
	return RecentCounter{
		stack: make([]int, 0, 256),
	}
}

// Ping ...
func (rc *RecentCounter) Ping(t int) int {
	start := t - 3000
	rc.stack = append(rc.stack, t)

	if start <= 0 || rc.stack[0] >= start {
		return len(rc.stack)
	}

	l, r := 0, len(rc.stack)

	for l < r {
		m := (l + r) / 2
		if rc.stack[m] == start {
			l = m
			break
		}

		if rc.stack[m] < start {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	if rc.stack[l] < start {
		l++
	}

	// fmt.Println(t, rc.stack, l, r)

	rc.stack = rc.stack[l:]

	return len(rc.stack)
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */
