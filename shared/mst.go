package shared

import (
	"sort"
)

// BuildMST ...
func BuildMST(graph [][]int, nodes int) (int, [][]int) {
	res := make([][]int, 0, nodes)
	clone := make([][]int, 0, len(graph))
	min := 0

	for i, e := range graph {
		clone = append(clone, []int{i, e[0], e[1], e[2]})
	}

	sort.Slice(clone, func(i, j int) bool {
		return clone[i][3] < clone[j][3]
	})

	union := InitUnionFind(nodes)
	var edge []int

	for i := range clone {
		edge = clone[i]
		if edge[3] < 0 {
			continue
		}

		if Union(union, edge[1], edge[2]) {
			res = append(res, edge[:3])
			min += edge[3]
		}
	}

	var base int
	for i := range union {
		if i == 0 {
			base = Find(union, 0)
			continue
		}

		if base != Find(union, i) {
			return -1, nil
		}
	}

	return min, res
}

// InitUnionFind ...
func InitUnionFind(count int) []int {
	src := make([]int, count)

	for i := range src {
		src[i] = i
	}

	return src
}

// Union ...
func Union(src []int, i, j int) bool {
	ri, rj := Find(src, i), Find(src, j)
	if ri == rj {
		return false
	}

	if ri < rj {
		src[rj] = ri
	} else {
		src[ri] = rj
	}

	return true
}

// Find ...
func Find(src []int, n int) int {
	for src[n] != n {
		n = src[n]
	}

	return n
}
