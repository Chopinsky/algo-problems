package shared

// Fenwick ...
type Fenwick struct {
	size int
	bits []int
}

// CreateFenwick ...
func CreateFenwick(size int) *Fenwick {
	return &Fenwick{
		size: size,
		bits: make([]int, size+1),
	}
}

// Update ...
func (f *Fenwick) Update(idx, val int) {
	idx++

	for idx <= f.size {
		f.bits[idx] += val
		idx += (idx & -idx)
	}
}

// Query ...
func (f *Fenwick) Query(idx int) int {
	sum := 0
	idx++

	for idx > 0 {
		sum += f.bits[idx]
		idx -= (idx & -idx)
	}

	return sum
}

// UpdateFenwick ...
func UpdateFenwick(src []int, idx, val int) {
	idx++
	size := len(src)

	for idx < size {
		src[idx] += val
		idx += (idx & -idx)
	}
}

// QueryFenwick ...
func QueryFenwick(src []int, idx int) int {
	sum := 0
	idx++

	for idx > 0 {
		sum += src[idx]
		idx -= (idx & -idx)
	}

	return sum
}
