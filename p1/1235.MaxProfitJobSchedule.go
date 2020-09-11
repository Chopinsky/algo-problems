package p1

import (
	"fmt"
	"sort"
	"time"

	s "go-problems/shared"
)

// MPJSProblems ...
type MPJSProblems struct {
	set []*MPJS
}

// Solve ...
func (p *MPJSProblems) Solve() {
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

// MPJS ...
type MPJS struct {
	data   []int
	output int
}

// CreateMPJS ...
func CreateMPJS() s.Problem {
	set := make([]*MPJS, 0, 4)

	set = append(set, &MPJS{
		data:   []int{},
		output: 0,
	})

	return &MPJSProblems{set}
}

func (p *MPJS) solve() int {
	return 0
}


func jobScheduling(startTime []int, endTime []int, profit []int) int {
  size := len(startTime)
  s := make([]*jobNode, 0, size)

  for i := range startTime {
    n := &jobNode {
      start: startTime[i],
      end: endTime[i],
      profit: profit[i],
    }

    s = append(s, n)
  }

  sort.Slice(s, func (i, j int) bool {
    return s[i].end < s[j].end
  })

  l := len(s)
  top := 0
  dp := make(map[int]int, l)

  for i := range s {
    best := find(s, dp, s[i].start, i)
    val := best + s[i].profit

    if last, ok := dp[s[i].end]; ok {
      if last < val {
        dp[s[i].end] = val
      } else {
        val = last
      }
    } else {
      dp[s[i].end] = val
    }

    // fmt.Println("calc:", s[i].end, best, top, val)

    if top < val {
      top = val
    } else {
      dp[s[i].end] = top
    }
  }

  // for i := range s {
  //   fmt.Println(s[i].start, s[i].end, ":", dp[s[i].end])
  // }

  return dp[s[l-1].end]
}

type jobNode struct {
  start  int
  end    int
  profit int
}

func find(src []*jobNode, dp map[int]int, end, last int) int {
  if last == 0 {
    return 0
  }

  if last == 1 {
    if src[0].end <= end {
      return src[0].profit
    }

    return 0
  }

  l, r := 0, last

  for l < r {
    m := (l + r) / 2

    if src[m].end == end {
      return dp[src[m].end]
    }

    if src[m].end <= end {
      l = m + 1
    } else {
      r = m - 1
    }
  }

  if src[l].end <= end {
    return dp[src[l].end]
  }

  if l > 0 && src[l-1].end <= end {
    return dp[src[l-1].end]
  }

  return 0
}
