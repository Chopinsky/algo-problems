package challenges

func combinationSum3(k int, n int) [][]int {
	if k*9 < n {
		return [][]int{}
	}

	ans, _ := sum2(k, n, 1, []int{})

	return ans
}

func sum2(k, n, i int, stack []int) ([][]int, []int) {
	if i > 9 || k*9 < n || k*i > n {
		return nil, stack
	}

	ans := [][]int{}

	if k == 2 {
		// fmt.Println(n, i)

		if i > (n / 2) {
			return nil, stack
		}

		for j := i; j <= n/2 && j < 10; j++ {
			// fmt.Println("inner loop", i, j, n-j)

			if j == n-j || n-j > 9 {
				continue
			}

			a := make([]int, len(stack))
			copy(a, stack)

			a = append(a, j)
			a = append(a, n-j)

			ans = append(ans, a)

			// fmt.Println("k=2", j, n-j, a, k, n, i)
		}

		return ans, stack
	}

	var a [][]int

	for j := i; j < n/k; j++ {
		stack = append(stack, j)
		a, stack = sum2(k-1, n-j, j+1, stack)

		if a != nil && len(a) > 0 {
			for i := range a {
				ans = append(ans, a[i])
			}

			// fmt.Println("appending", k, n, i, j, a)
		}

		stack = stack[:len(stack)-1]
	}

	return ans, stack
}
