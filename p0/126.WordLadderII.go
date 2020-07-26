package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// WLIIProblems ...
type WLIIProblems struct {
	set []*WLII
}

// Solve ...
func (p *WLIIProblems) Solve() {
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

// WLII ...
type WLII struct {
	data   []string
	begin  string
	end    string
	output [][]string
}

// CreateWLII ...
func CreateWLII() s.Problem {
	set := make([]*WLII, 0, 4)

	set = append(set, &WLII{
		data:   []string{"hot","dot","dog","lot","log","cog"},
		begin:  "hit",
		end:    "cog",
		output: [][]string{
			{"hit","hot","dot","dog","cog"},
			{"hit","hot","lot","log","cog"},
		},
	})

	return &WLIIProblems{set}
}

func (p *WLII) solve() [][]string {
	return findLadders(p.begin, p.end, p.data)
}

func findLadders(beginWord string, endWord string, wordList []string) [][]string {
  dict := make(map[string][]string)
  found := false
  var size int

  for _, src := range wordList {
    if !found && endWord == src {
      found = true
    }

    size = len(src)
    if size == 0 {
      dict[""] = append(dict[""], src)
      continue
    }

    for i := 0; i < size; i++ {
      next := src[:i] + "*" + src[i+1:]
      dict[next] = append(dict[next], src)
    }
  }

  for i := 0; i < len(beginWord); i++ {
    next := beginWord[:i] + "*" + beginWord[i+1:]
    dict[next] = append(dict[next], beginWord)
  }

  if !found {
    return [][]string{}
  }

  for k, v := range dict {
    if len(v) < 2 {
      delete(dict, k)
    }
  }

  // fmt.Println(dict)

  size = len(wordList)
  res := make([][]string, 0, size)

  visited := make(map[string]bool)
  visited[beginWord] = true

  stack := [][]string{}
  for i := 0; i < len(beginWord); i++ {
    next := beginWord[:i] + "*" + beginWord[i+1:]

    if cand, ok := dict[next]; ok {
      for _, v := range cand {
        if visited[v] {
          continue
        }

        if v == endWord {
          res = append(res, []string{ beginWord, v })
          return res
        }

        stack = append(stack, []string{ beginWord, v })
        visited[v] = true
      }
    }
  }

  // fmt.Println(stack, res)

  if len(stack) == 0 {
    return res
  }

  for {
    size = len(stack)
    found := false
    updated := false
    temp := make(map[string]bool)

    // fmt.Println("round", stack)

    for i := 0; i < size; i++ {
      idx := len(stack[i]) - 1
      curr := stack[i][idx]
      scheck := make(map[string]bool)
      added := false

      for j := 0; j < len(curr); j++ {
        next := curr[:j] + "*" + curr[j+1:]

        if cand, ok := dict[next]; ok {
          for _, v := range cand {
            if visited[v] || scheck[v] {
              continue
            }

            if v == endWord {
              found = true
            }

            if !added {
              stack[i] = append(stack[i], v)
              added = true
              updated = true

              if v == endWord {
                res = append(res, stack[i])
              }

              // fmt.Println("adding back ... ", stack[i])
            } else {
              // fmt.Println("adding more ... ", stack[i])

              entry := append([]string(nil), stack[i][:idx+1]...)
              entry = append(entry, v)
              updated = true

              if v == endWord {
                res = append(res, entry)
              } else {
                stack = append(stack, entry)
              }
            }

            temp[v] = true
            scheck[v] = true
          }
        }
      }
    }

    if found || !updated {
      break
    }

    for k := range temp {
      visited[k] = true
    }
  }


  return res
}