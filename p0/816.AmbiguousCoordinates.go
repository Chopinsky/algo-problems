package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// ACProblems ...
type ACProblems struct {
	set []*AC
}

// Solve ...
func (p *ACProblems) Solve() {
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

// AC ...
type AC struct {
	data   []int
	output int
}

// CreateAC ...
func CreateAC() s.Problem {
	set := make([]*AC, 0, 4)

	set = append(set, &AC{
		data:   []int{},
		output: 0,
	})

	return &ACProblems{set}
}

func (p *AC) solve() int {
	return 0
}

func ambiguousCoordinates(S string) []string {
  s := S[1:len(S)-1]
  res := []string{}

  if len(s) <= 1 {
    res = append(res, S)
    return res
  }

  cache := make(map[string][]string, 2 * len(s))
  for i := 1; i < len(s); i++ {
    l, r := build(s[:i], cache), build(s[i:], cache)

    if len(l) > 0 && len(r) > 0 {
      for _, vl := range l {
        for _, vr := range r {
          res = append(res, "(" + vl + ", " + vr + ")")
        }
      }
    }
  }


  return res
}

func build(s string, cache map[string][]string) []string {
  if vals, ok := cache[s]; ok {
    return vals
  }

  size := len(s)
  arr := make([]string, 0, 2 * size)

  if size == 1 {
    arr = append(arr, s)
    cache[s] = arr
    return arr
  }

  if s[0] == '0' {
    if s[size-1] != '0' {
      arr = append(arr, s[:1] + "." + s[1:])
    }

    cache[s] = arr
    return arr
  }

  // the integer number is always valid if not starting with '0'
  arr = append(arr, s)

  // decimal doesn't allow trailing 0s
  if s[size-1] != '0' {
    for i := size-1; i > 0; i-- {
      arr = append(arr, s[:i] + "." + s[i:])
    }
  }

  cache[s] = arr
  return arr
}
