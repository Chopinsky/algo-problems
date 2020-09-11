package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// KSPFProblems ...
type KSPFProblems struct {
	set []*KSPF
}

// Solve ...
func (p *KSPFProblems) Solve() {
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

// KSPF ...
type KSPF struct {
	data   []int
	k      int
	output []int
}

// CreateKSPF ...
func CreateKSPF() s.Problem {
	set := make([]*KSPF, 0, 4)

	set = append(set, &KSPF{
		data:   []int{1, 2, 3, 5},
		k:      3,
		output: []int{2, 5},
	})

	return &KSPFProblems{set}
}

func (p *KSPF) solve() []int {
	return kthSmallestPrimeFraction(p.data, p.k)
}

func kthSmallestPrimeFraction(a []int, k int) []int {
  // binary + slide window? see 719

  size := len(a)
  if k == 1 {
    return []int{a[0], a[size-1]}
  }

  // lol has to grind this number down to the 1e-9 to pass ....
  eps := 1.0 / float64(300000001)
  l, r := float64(0), float64(1)
  res := []int{a[0], a[1]}

  var count int
  var best float64

  for l < r {
    m := (l+r) / 2

    count = 0
    best = 0

    // res[0] = -1
    // res[1] = -1

    for i := 1; i < size; i++ {
      c := find(a, i, m, eps)

      if c >= 0 {
        count += c + 1

        val := float64(a[c]) / float64(a[i])
        if val > best {
          res[0], res[1] = a[c], a[i]
          best = val
        }
      }
    }

    // fmt.Println(m, count, res)

    if count == k {
      break
    }

    // val := float64(res[0]) / float64(res[1])

    if count < k {
      l = m + eps
    } else {
      r = m - eps
    }
  }

  return res
}

func find(a []int, i int, k, eps float64) int {
  base := float64(a[i])
  l, r := 0, i-1

  if float64(a[l]) / base > k {
    return -1
  }

  if float64(a[r]) / base <= k {
    return r
  }

  for l < r {
    m := (l + r) / 2
    val := float64(a[m]) / base

    if val <= k && (m + 1 == i || float64(a[m+1]) / base > k) {
      return m
    }

    if val < k {
      l = m+1
    } else {
      r = m-1
    }
  }

  if l == i {
    return -1
  }

  return l
}