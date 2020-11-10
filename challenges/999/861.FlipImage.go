package challenges

func flipAndInvertImage(a [][]int) [][]int {
	if a == nil || len(a) == 0 || len(a[0]) == 0 {
		return a
	}

	w := len(a[0])

	for i := range a {
		if w%2 == 1 {
			a[i][w/2] ^= 1
		}

		for j := 0; j < w/2; j++ {
			a[i][j], a[i][w-1-j] = a[i][w-1-j], a[i][j]
			a[i][j] ^= 1
			a[i][w-1-j] ^= 1
		}
	}

	return a
}
