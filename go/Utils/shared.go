package utils

import (
	"fmt"
)

// Dirs ...
var Dirs = []int{-1, 0, 1, 0, -1}

// Output ...
func Output(calculated, expected interface{}) {
	fmt.Println("Calculated result: ", calculated)
	fmt.Println("Expected result:   ", expected)
}

// QSort ...
func QSort(src []int, l, u int) []int {
	// no need to sort
	if u <= l {
		return src
	}

	// simple compare
	if u-l == 1 {
		if src[l] > src[u] {
			src[l], src[u] = src[u], src[l]
		}

		return src
	}

	t, i, j := src[l], l, u+1

	// goal: [l, j-1] to have elem smaller or equal to `j`; [j+1, u] to have elem larger or
	// equal to `j`. trigger `l` is swapped with `j` (guranteed by condition src[j] <= src[l]).
	for {
		// move index until: 1) out of bound, or 2) found first elem to be equal or
		// larger than the trigger
		for {
			i++
			if i > u || src[i] >= t {
				break
			}
		}

		// move index until: 1) out of bound, or 2) found first elem to be equal or
		// smaller than the trigger. Note that `src[j] <= t` also check bound, since
		// if j == l, then src[j] == src[l] == t
		for {
			j--
			if src[j] <= t {
				break
			}
		}

		// if out of bound, quit
		if i > j {
			break
		}

		// only swap if i, j are in bound, aka l < i <= j < u
		if i != j {
			src[i], src[j] = src[j], src[i]
		}
	}

	// swap trigger and j, where src[j] <= src[l]
	if l != j {
		src[l], src[j] = src[j], src[l]
	}

	// sort left if necessary
	if j-1 > l {
		src = QSort(src, l, j-1)
	}

	// sort right if necessary
	if u > j+1 {
		src = QSort(src, j+1, u)
	}

	return src
}

// Permut ...
func Permut(src []int, k int, output [][]int) [][]int {
	if k == 1 {
		output = append(output, append([]int(nil), src...))
	} else {
		// output the source array, which is also a valid result
		output = Permut(src, k-1, output)

		// actual elem swaps to create a new and different array
		var index int
		for i := 0; i < k-1; i++ {
			if k%2 == 0 {
				index = i
			} else {
				index = 0
			}

			// swap
			src[index], src[k-1] = src[k-1], src[index]

			// permut the newly created array. Note that the Permut(...) will
			// also output the made array at this step
			output = Permut(src, k-1, output)
		}
	}

	return output
}
