package challenges

/*
==================
Problem:

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

==================
Solution:

The patter repeats itself after 14 days, upper bound is 14 iterations.
*/

//
func prisonAfterNDays(cells []int, N int) []int {
	if N == 0 {
		return cells
	}

	base := uint8(0)

	for i := 0; i < 8; i++ {
		if cells[i] == 1 {
			base |= 1 << i
		}
	}

	base = iterate(base, N)

	cells[0], cells[7] = 0, 0
	for i := 1; i < 8; i++ {
		if base&(1<<i) > 0 {
			cells[i] = 1
		} else {
			cells[i] = 0
		}
	}

	return cells
}

func iterate(base uint8, N int) uint8 {
	end := N
	l, u := uint8(1), uint8(1<<7)

	if end > 14 {
		end = 14
	}

	s := make([]uint8, 14)
	for i := 1; i <= end; i++ {
		base = ^(((base >> 1) | l) ^ ((base << 1) | u))
		s[i%14] = base
	}

	if N <= 14 {
		return base
	}

	return s[N%14]
}
