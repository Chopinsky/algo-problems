package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// VAPProblems ...
type VAPProblems struct {
	set []*VAP
}

// Solve ...
func (p *VAPProblems) Solve() {
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

// VAP ...
type VAP struct {
  data   []string
  result string
	output int
}

// CreateVAP ...
func CreateVAP() s.Problem {
	set := make([]*VAP, 0, 4)

	set = append(set, &VAP{
    data:   []string{"SIX","SEVEN","SEVEN"},
    result: "TWENTY",
		output: 0,
	})

	return &VAPProblems{set}
}

func (p *VAP) solve() bool {
	return isSolvable(p.data, p.result)
}

func isSolvable(words []string, result string) bool {
  if len(result) == 0 || len(words) == 0 {
    return false
  }

  h, w := len(words)+1, len(result)
  grid := make([][]byte, h)

  for i := range grid {
    grid[i] = make([]byte, w)
  }

  maxSum := 0
  for i := range words {
    s := len(words[i])
    if s > w {
      return false
    }

    if s == 0 {
      continue
    }

    col := 0
    curr := 1

    for j := s-1; j >= 0; j-- {
      grid[i][col] = words[i][j]
      col++
      curr *= 10
    }

    curr--
    maxSum += curr
  }

  minTgt := 1
  for i := len(result)-1; i >= 0; i-- {
    grid[h-1][w-1-i] = result[i]
    minTgt *= 10
  }

  minTgt /= 10
  if maxSum < minTgt {
    return false
  }

  fmt.Println(maxSum, minTgt)

  // fmt.Println(grid)

  nums := make([]byte, 10)
  chars := make(map[byte]int, 26)

  res := search(words, grid, nums, chars, 0, 0, 0, h, w)

  // fmt.Println(nums)
  // fmt.Println(chars)

  return res
}

func search(words []string, grid [][]byte, nums []byte, chars map[byte]int, balance, i, j, h, w int) bool {
  // fmt.Println(i, j)

  c := grid[i][j]

  var res bool
  if i == h - 1 {
    if val, ok := chars[c]; ok {
      if val == balance % 10 {
        // we're at the end of the grid, done
        if j < w - 1 {
          return search(words, grid, nums, chars, balance/10, 0, j+1, h, w)
        }

        // last cell, check for final results
        if balance >= 10 {
          return false
        }

        // can't have leading 0s
        if val == 0 {
          return false
        }

        return true
      }

      return false
    }

    val := balance % 10
    if nums[val] != byte(0) {
      return false
    }

    if j < w - 1 {
      nums[val] = c
      chars[c] = val

      res = search(words, grid, nums, chars, balance/10, 0, j+1, h, w)
      if res {
        // fmt.Println("1", string(rune(c)), j, balance)
        return true
      }

      nums[val] = byte(0)
      delete(chars, c)

      return false
    }

    if balance >= 10 {
      return false
    }

    if val == 0 {
      return false
    }

    // fmt.Println("2", c, j, balance)
    return true
  }

  if c == byte(0) {
    return search(words, grid, nums, chars, balance, i+1, j, h, w)
  }

  if val, ok := chars[c]; ok {
    if j == len(words[i])-1 && val == 0 {
      return false
    }

    return search(words, grid, nums, chars, balance+val, i+1, j, h, w)
  }

  for k := 0; k < 10; k++ {
    if nums[k] != byte(0) {
      continue
    }

    if j == len(words[i])-1 && k == 0 {
      continue
    }

    nums[k] = c
    chars[c] = k

    res = search(words, grid, nums, chars, balance+k, i+1, j, h, w)
    if res {
      return true
    }

    nums[k] = byte(0)
    delete(chars, c)
  }

  // fmt.Println("can't find a solution ... ")

  return false
}

func isSolvable1(words []string, result string) bool {
  nums := make([]rune, 10)
  chars := make(map[rune]int, 26)
  size := len(result)
  lvls := make([]map[rune]int, 0, size)
  tgt := make([]rune, size)

  for i := range result {
    tgt[size-i-1] = rune(result[i])
    m := make(map[rune]int)

    for j := range words {
      s := len(words[j]) - 1
      if i <= s {
        m[rune(words[j][s-i])]++
      }
    }

    if len(m) == 0 {
      break
    }

    lvls = append(lvls, m)
  }

  fmt.Println(lvls, tgt)

  return calc1(nums, tgt, chars, lvls, 0)
}

func calc1(nums, tgt []rune, chars map[rune]int, lvls []map[rune]int, carryover int) bool {
  if lvls == nil || len(lvls) == 0 {
    curr := tgt[0]

    var res, reset bool
    var num int

    if val, ok := chars[curr]; ok {
      if val != carryover % 10 {
        return false
      }
    } else {
      num = carryover % 10
      chars[curr] = num
      nums[num] = curr
      reset = true
    }

    if len(tgt) > 1 && carryover >= 10 {
      res = calc1(nums, tgt[1:], chars, lvls[1:], carryover/10)
    } else if carryover < 10 && len(tgt) == 1 {
      res = true
    } else {
      res = false
    }

    if reset {
      nums[num] = rune(0)
      delete(chars, curr)
    }

    return res
  }

  trace := make([]rune, 0, len(lvls[0]))
  for k := range lvls[0] {
    if _, ok := chars[k]; !ok {
      trace = append(trace, k)
    }
  }

  fmt.Println(trace)

  return guess(nums, tgt, chars, lvls, carryover, trace)
}

func guess(nums, tgt []rune, chars map[rune]int, lvls []map[rune]int, carryover int, trace []rune) bool {
  if len(trace) == 0 {
    sum := carryover

    for k, v := range lvls[0] {
      sum += v * chars[k]
    }

    curr := tgt[0]

    var res, reset bool
    var num int

    if val, ok := chars[curr]; ok {
      if val != carryover % 10 {
        return false
      }
    } else {
      num = carryover % 10
      chars[curr] = num
      nums[num] = curr
      reset = true
    }

    if len(tgt) > 1 && carryover >= 10 {
      res = calc1(nums, tgt[1:], chars, lvls[1:], carryover/10)
    } else if carryover < 10 && len(tgt) == 1 {
      res = true
    } else {
      res = false
    }

    if reset {
      nums[num] = rune(0)
      delete(chars, curr)
    }

    return res
  }

  curr := trace[0]
  var res bool

  for i := 0; i <= 9; i++ {
    if nums[i] != rune(0) {
      continue
    }

    chars[curr] = i
    nums[i] = curr

    res = guess(nums, tgt, chars, lvls, carryover, trace[1:])

    if res {
      return true
    }

    delete(chars, curr)
    nums[i] = rune(0)
  }

  return false
}
