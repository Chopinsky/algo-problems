package challenges

func minDominoRotations(A []int, B []int) int {
	va := make([]int, 6)
	vb := make([]int, 6)

	for i := range A {
		a, b := A[i], B[i]
		update(va, a, b)
		update(vb, b, a)
	}

	ans := -1

	for i := range va {
		if va[i] >= 0 {
			if ans < 0 || va[i] < ans {
				ans = va[i]
			}
		}

		if vb[i] >= 0 {
			if ans < 0 || vb[i] < ans {
				ans = vb[i]
			}
		}
	}

	// fmt.Println(va)
	// fmt.Println(vb)

	return ans
}

func update(nums []int, a, b int) {
	for i := range nums {
		// not having this value in previous cols, can't fulfill
		if nums[i] < 0 {
			continue
		}

		// no need to turn
		if i+1 == a {
			continue
		}

		// need to turn
		if i+1 == b {
			nums[i]++
			continue
		}

		// can't make it
		nums[i] = -1
	}
}
