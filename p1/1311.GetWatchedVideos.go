package p1

import (
	"fmt"
	"sort"
	"time"

	s "go-problems/shared"
)

// GWVProblems ...
type GWVProblems struct {
	set []*GWV
}

// Solve ...
func (p *GWVProblems) Solve() {
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

// GWV ...
type GWV struct {
	data   [][]int
	videos [][]string
	id     int
	level  int
	output []string
}

// CreateGWV ...
func CreateGWV() s.Problem {
	set := make([]*GWV, 0, 4)

	set = append(set, &GWV{
		data:   [][]int{{1, 2}, {0, 3}, {0, 3}, {1, 2}},
		videos: [][]string{{"A", "B"}, {"C"}, {"B", "C"}, {"D"}},
		id:     0,
		level:  1,
		output: []string{"B", "C"},
	})

	return &GWVProblems{set}
}

func (p *GWV) solve() []string {
	return watchedVideosByFriends(p.videos, p.data, p.id, p.level)
}

func watchedVideosByFriends(watchedVideos [][]string, friends [][]int, id int, level int) []string {
	seen := make([]bool, len(friends))
	seen[id] = true

	f := make([]int, len(friends[id]))
	copy(f, friends[id])
	for _, i := range f {
		seen[i] = true
	}

	tmp := make([]int, 0, len(friends))

	for level > 1 {
		// fmt.Println(f)

		for _, ppl := range f {
			for _, fr := range friends[ppl] {
				if !seen[fr] {
					seen[fr] = true
					tmp = append(tmp, fr)
				}
			}
		}

		f, tmp = tmp, f
		tmp = tmp[len(tmp):]
		level--
	}

	// fmt.Println(f)

	vids := make(map[string]*vnode)
	arr := make([]*vnode, 0, len(friends))

	for _, ppl := range f {
		for _, v := range watchedVideos[ppl] {
			if n, ok := vids[v]; ok {
				n.count++
			} else {
				n := &vnode{
					name:  v,
					count: 1,
				}

				vids[v] = n
				arr = append(arr, n)
			}
		}
	}

	sort.Slice(arr, func(i, j int) bool {
		if arr[i].count == arr[j].count {
			return arr[i].name < arr[j].name
		}

		return arr[i].count < arr[j].count
	})

	res := make([]string, 0, len(arr))
	for i := range arr {
		res = append(res, arr[i].name)
	}

	return res
}

type vnode struct {
	name  string
	count int
}
