package main

import "fmt"

// BinarySearch ...
func BinarySearch(src []int, l, r, val int) int {
	if val < src[l] {
		return l
	}

	if val >= src[r] {
		return r + 1
	}

	var m int
	for l <= r {
		m = (l + r) / 2
		if val < src[m] {
			r = m - 1
		} else if val >= src[m] {
			l = m + 1
		}
	}

	return l
}

// InsertSort ...
func InsertSort(src []int, l, r int) {
	if r-l < 1 {
		return
	}

	var j, temp int

	for i := l + 1; i <= r; i++ {
		j = i - 1
		temp = src[i]

		for j >= l && temp < src[j] {
			src[j+1] = src[j]
			j--
		}

		src[j+1] = temp
	}
}

// FindLeastCommonAncestor ...
func FindLeastCommonAncestor(tree []int, a, b int, debug bool) int {
	l, r, res := findLCA(tree, 0, len(tree), a, b)

	if debug {
		fmt.Println(l, r, res)
	}

	return res
}

func findLCA(tree []int, root, size, a, b int) (int, int, int) {
	l, r := 2*root+1, 2*root+2
	la, lb := -1, -1

	if tree[root] == a {
		la = root
	}

	if tree[root] == b {
		lb = root
	}

	if l < size {
		la0, lb0, res := findLCA(tree, l, size, a, b)

		if res >= 0 {
			return -1, -1, res
		}

		if la < 0 {
			la = la0
		}

		if lb < 0 {
			lb = lb0
		}
	}

	if la >= 0 && lb >= 0 {
		return -1, -1, root
	}

	if r < size {
		la0, lb0, res := findLCA(tree, r, size, a, b)

		if res >= 0 {
			return -1, -1, res
		}

		if la < 0 {
			la = la0
		}

		if lb < 0 {
			lb = lb0
		}
	}

	if la >= 0 && lb >= 0 {
		return -1, -1, root
	}

	return la, lb, -1
}

// Heapify ...
func Heapify(src []int) {
	size := len(src)
	if size <= 1 {
		return
	}

	for i := (size - 1) / 2; i >= 0; i-- {
		siftDown(src, i, size)
	}
}

// UpdateHeap ...
func UpdateHeap(src []int, val int) int {
	if val >= src[0] {
		return val
	}

	old := src[0]
	src[0] = val
	siftDown(src, 0, len(src))

	return old
}

// HeapSort ...
func HeapSort(src []int) {
	Heapify(src)
	size := len(src)

	for i := size - 1; i > 0; i-- {
		src[0], src[i] = src[i], src[0]
		siftDown(src, 0, i-1)
	}
}

func siftDown(src []int, root, size int) {
	l, r := 2*root+1, 2*root+2
	next := root

	if l < size && src[next] < src[l] {
		next = l
	}

	if r < size && src[next] < src[r] {
		next = r
	}

	if next != root {
		src[next], src[root] = src[root], src[next]
		siftDown(src, next, size)
	}
}
