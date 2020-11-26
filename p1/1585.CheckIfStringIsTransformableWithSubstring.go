package p1

import (
	"fmt"
	"sort"
	"strings"
	"time"

	s "go-problems/shared"
)

// CISITWSProblems ...
type CISITWSProblems struct {
	set []*CISITWS
}

// Solve ...
func (p *CISITWSProblems) Solve() {
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

// CISITWS ...
type CISITWS struct {
	data   string
	t      string
	output bool
}

// CreateCISITWS ...
func CreateCISITWS() s.Problem {
	set := make([]*CISITWS, 0, 4)

	set = append(set, &CISITWS{
		data:   "84532",
		t:      "34852",
		output: true,
	})

	set = append(set, &CISITWS{
		data:   "34521",
		t:      "23415",
		output: true,
	})

	set = append(set, &CISITWS{
		data:   "12345",
		t:      "12435",
		output: false,
	})

	set = append(set, &CISITWS{
		data:   "1",
		t:      "2",
		output: false,
	})

	return &CISITWSProblems{set}
}

func (p *CISITWS) solve() bool {
	s, t := p.data, p.t

	if len(s) != len(t) {
		return false
	}

	if s == t {
		return true
	}

	size := len(s)
	if size == 1 {
		if s[0] == t[0] {
			return true
		}

		return false
	}

	// there's no way we can amend this situation
	if t[0] > t[1] && s[0] < t[0] {
		return false
	}

	states := make([]int, 10)
	// rangeCount := 0
	ok := true

	for i, c := range t {
		states[c-'0']++
		states[s[i]-'0']--

		if i > 0 && byte(c) < t[i-1] {
			ok = false
		}
	}

	// the target string is sorted, we're done
	if ok {
		return true
	}

	// make sure count of each digits counts match
	for _, v := range states {
		if v != 0 {
			return false
		}
	}

	var start int
	sa, ta := strings.Split(s, ""), strings.Split(t, "")

	for i := range states {
		states[i] = 0
	}

	for i := 0; i < size; i++ {
		if i > 0 && t[i] < t[i-1] {
			sa, ok = reorder(sa, ta, states, start, i-1)
			start = i

			if !ok {
				return false
			}
		}

		states[t[i]-'0']++
	}

	_, ok = reorder(sa, ta, states, start, size-1)

	return ok
}

func reorder(s, t []string, states []int, l, r int) ([]string, bool) {
	var num, total int

	pos := -1
	end := -1

	for i := l; i <= r; i++ {
		num = int(s[i][0] - '0')

		if states[num] <= 0 {
			pos = i
			break
		}

		states[num]--
	}

	if pos < 0 {
		return s, true
	}

	for _, val := range states {
		if val > 0 {
			total += val
		}
	}

	for i := pos; i < len(s); i++ {
		num = int(s[i][0] - '0')

		if states[num] > 0 {
			states[num]--
			total--
		}

		if total == 0 {
			end = i
			break
		}
	}

	// fmt.Println("from s:", states, pos, end)

	if total > 0 || end < 0 {
		return s, false
	}

	sort.Strings(s[pos:(end + 1)])

	for i := l; i <= r; i++ {
		num = int(t[i][0] - '0')
		states[num]++

		num = int(s[i][0] - '0')
		states[num]--
	}

	for _, val := range states {
		if val != 0 {
			return s, false
		}
	}

	return s, true
}
