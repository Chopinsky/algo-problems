package shared

var cutoff = 8

// QuickSort ...
func QuickSort(src []int) {
	qsort(src, 0, len(src)-1)
}

func qsort(src []int, l, r int) {
	if r-l >= cutoff {
		pivot := src[l]
		start := l + 1
		mid := l + 1

		// divide the array into 2 portions
		for i := start; i <= r; i++ {
			if src[i] <= pivot {
				swap(src, mid, i)
				mid++
			}
		}

		// moving the pivot to the center (and filtered from
		// the recursive calls)
		swap(src, l, mid-1)

		// divide and conqure
		qsort(src, l, mid-2)
		qsort(src, mid, r)
	} else if r > l {
		// under the linmit, bubble sort is faster
		BubbleSort(src[l : r+1])
	}
}

func swap(src []int, i, j int) {
	temp := src[i]
	src[i] = src[j]
	src[j] = temp
}
