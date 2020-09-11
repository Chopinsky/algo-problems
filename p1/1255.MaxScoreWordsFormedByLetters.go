package p1

import (
	"fmt"
	"sort"
	"time"

	s "go-problems/shared"
)

// MSWFBLProblems ...
type MSWFBLProblems struct {
	set []*MSWFBL
}

// Solve ...
func (p *MSWFBLProblems) Solve() {
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

// MSWFBL ...
type MSWFBL struct {
	data    []string
	letters []byte
	score   []int
	output  int
}

// CreateMSWFBL ...
func CreateMSWFBL() s.Problem {
	set := make([]*MSWFBL, 0, 4)

	set = append(set, &MSWFBL{
		data:    []string{"dog","cat","dad","good"},
		letters: []byte{'a','a','c','d','d','d','g','o','o'},
		score:  []int{1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0},
		output:  23,
	})

	set = append(set, &MSWFBL{
		data:    []string{"xxxz","ax","bx","cx"},
		letters: []byte{'z','a','b','c','x','x','x'},
		score:  []int{4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10},
		output:  27,
	})

	set = append(set, &MSWFBL{
		data:    []string{"leetcode"},
		letters: []byte{'l','e','t','c','o','d'},
		score:  []int{0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0},
		output:  0,
	})

	return &MSWFBLProblems{set}
}

func (p *MSWFBL) solve() int {
	return mswfblMaxScoreWords(p.data, p.letters, p.score)
}

type mswfbl struct {
  m map[int]int
  score int
}

func mswfblMaxScoreWords(words []string, letters []byte, score []int) int {
  supply := make([]int, 26)

  for _, ch := range letters {
    supply[int(ch - 'a')]++
  }

  store := make([]*mswfbl, 0, len(words))

  chCount := make([][]int, len(words)+1)
  for i := range chCount {
    chCount[i] = make([]int, 26)
  }

  for _, w := range words {
    m := make(map[int]int, 26)
    s := 0

    for _, ch := range w {
      val := int(ch - 'a')
      m[val]++
      s += score[val]
    }

    store = append(store, &mswfbl{ m: m, score: s, })
  }

  sort.Slice(store, func (i, j int) bool {
    if store[i].score == store[j].score {
      return len(store[i].m) < len(store[j].m)
    }

    return store[i].score > store[j].score
  })

  scores := make([]int, len(words)+1)
  for i := range store {
    scores[i+1] = scores[i] + store[i].score

    for j := range chCount[i+1] {
      chCount[i+1][j] = chCount[i][j]
    }

    for k, v := range store[i].m {
      chCount[i+1][k] += v
    }

    // fmt.Println(store[i])
  }

  // for i := range chCount {
  //   fmt.Println(chCount[i])
  // }

  // fmt.Println(chCount, supply, scores)

  return searchMswfbl(store, chCount, supply, scores, 0)
}

func searchMswfbl(store []*mswfbl, chCount [][]int, supply, scores []int, idx int) int {
  if len(store) == 0 {
    return 0
  }

  fullSupply := true
  last := len(chCount) - 1
  size := len(scores)

  for i := range supply {
    count := chCount[last][i] - chCount[idx][i]

    // if idx == 6 && i == 4 {
    //   fmt.Println(idx, string('a' + i), count)
    // }

    if supply[i] < count {
      fullSupply = false
      break
    }
  }

  if fullSupply {
    // fmt.Println("full supply", supply, idx, scores[size-1] - scores[idx])
    return scores[size-1] - scores[idx]
  }

  currSupply := true
  currScore := 0
  curr := store[0]

  for k, v := range curr.m {
    if supply[k] < v {
      // fmt.Println("no supply for this word:", )
      currSupply = false
      break
    }
  }

  if currSupply {
    // now take the current word
    for k, v := range curr.m {
      supply[k] -= v
    }

    currScore = curr.score + searchMswfbl(store[1:], chCount, supply, scores, idx+1)

    for k, v := range curr.m {
      supply[k] += v
    }
  }

  // if exclude the current score
  remScore := scores[size-1] - scores[idx+1]

  // fmt.Println(idx, "curr score:", currScore)

  if remScore > currScore {
    nextScore := searchMswfbl(store[1:], chCount, supply, scores, idx+1)

    // fmt.Println("next score:", idx, nextScore, currScore)

    if nextScore > currScore {
      currScore = nextScore
    }
  }

  return currScore
}