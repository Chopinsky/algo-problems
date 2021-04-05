package challenges

/**
We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.

Example 1:

Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.
Example 2:

Input: A = [1,2,0]
Output: false
Explanation: There are 2 global inversions, and 1 local inversion.
Note:

A will be a permutation of [0, 1, ..., A.length - 1].
A will have length in range [1, 5000].
The time limit for this problem has been reduced.
*/

func isIdealPermutation(a []int) bool {
	max := -1

	for i := 0; i < len(a)-2; i++ {
		if a[i] > max {
			max = a[i]
		}

		if max > a[i+2] {
			return false
		}
	}

	return true
}

func isIdealPermutation1(a []int) bool {
	ln := len(a)
	if ln <= 2 {
		return true
	}

	fenwick := make([]int, ln+1)
	local := 0
	global := 0

	for i, val := range a {
		if i > 0 && val < a[i-1] {
			local++
		}

		updateFenwick(fenwick, val, 1)
		g := queryFenwick(fenwick, val)
		global += i + 1 - g
		// fmt.Println(val, i+1-g)
	}

	return local == global
}

// updateFenwick ...
func updateFenwick(arr []int, idx, val int) {
	idx++
	ln := len(arr)

	for idx < ln {
		arr[idx] += val
		idx += (idx & -idx)
	}
}

// queryFenwick ...
func queryFenwick(arr []int, idx int) int {
	sum := 0
	idx++

	for idx > 0 {
		sum += arr[idx]
		idx -= (idx & -idx)
	}

	return sum
}
