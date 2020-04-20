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
