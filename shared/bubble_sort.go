package shared

// BubbleSort ...
func BubbleSort(src []int) {
	n := len(src)
	var max, val int

	for i := n; i > 1; i-- {
		max = src[0]

		for j := 1; j < i; j++ {
			val = src[j]

			if val > max {
				src[j-1] = max
				max = val
			} else {
				src[j-1] = val
			}
		}

		src[i-1] = max
	}
}
