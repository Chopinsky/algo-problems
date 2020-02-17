package utils

// PrefixSumTree ...
type PrefixSumTree struct {
	internal []int
}

// BuildTree ...
func BuildTree(arr []int) *PrefixSumTree {
	tree := &PrefixSumTree{
		internal: make([]int, len(arr)+1),
	}

	for i, val := range arr {
		// the arr -> tree has 1 elem (elem 0) padding
		tree.UpdateWithDiff(i+1, val)
	}

	return tree
}

// Switch ...
func (t *PrefixSumTree) Switch(i, val int) {
	delta := val - t.internal[i]
	t.UpdateWithDiff(i, delta)
}

// UpdateWithDiff ...
func (t *PrefixSumTree) UpdateWithDiff(i, delta int) {
	for i < len(t.internal) {
		t.internal[i] += delta
		i += lowbit(i)
	}
}

// Query ...
func (t *PrefixSumTree) Query(i int) int {
	sum := 0
	i++

	for i > 0 {
		sum += t.internal[i]
		i -= lowbit(i)
	}

	return sum
}

// QueryRange ...
func (t *PrefixSumTree) QueryRange(i, j int) int {
	// query from arrya's (i-1) to j, that gives the range betwee [i,j], inclusively
	start, end := Min(i, j)-1, Max(i, j)
	return t.Query(end) - t.Query(start)
}

func lowbit(x int) int {
	return x & (-x)
}
