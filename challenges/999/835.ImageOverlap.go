package challenges

import "math/bits"

func largestOverlap(a [][]int, b [][]int) int {
	size := len(a)
	if size == 1 {
		if a[0][0] == 1 && b[0][0] == 1 {
			return 1
		}

		return 0
	}

	amap := condense(a)
	bmap := condense(b)

	aclone := make([]uint32, len(amap))
	for i := range amap {
		aclone[i] = amap[i]
	}

	// fmt.Println("src:", amap, aclone, bmap)

	// var a1, a2 int
	a1 := overlap(amap, bmap, true)
	a2 := overlap(aclone, bmap, false)

	// fmt.Println(a1, a2)

	if a1 > a2 {
		return a1
	}

	return a2
}

func condense(a [][]int) []uint32 {
	arr := make([]uint32, len(a))
	var base uint32

	for i := range a {
		base = 0

		for j := range a[i] {
			base <<= 1
			base |= uint32(a[i][j])
		}

		arr[i] = base
	}

	return arr
}

func overlap(a, b []uint32, shiftRight bool) int {
	size := len(a)
	best := 0
	var sum, count int

	for k := 0; k < size; k++ {
		for i := 0; i < size; i++ {
			sum = 0

			for j := i; j < size; j++ {
				sum += bits.OnesCount32(a[j-i] & b[j])
			}

			if sum > best {
				best = sum
			}

			if i == 0 {
				continue
			}

			sum = 0

			for j := 0; j < i; j++ {
				sum += bits.OnesCount32(a[size-i+j] & b[j])
			}

			if sum > best {
				best = sum
			}
		}

		count = 0
		for i := range a {
			if shiftRight {
				a[i] >>= 1
			} else {
				a[i] <<= 1
			}

			if a[i] > 0 {
				count++
			}
		}

		// a is now a blank image, no more overlaps, break
		if count == 0 {
			break
		}
	}

	return best
}
