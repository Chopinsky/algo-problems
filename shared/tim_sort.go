package shared

// TimSort ...
type TimSort []int

// Sort ...
func (t *TimSort) Sort(start, end int) {

}

func merge(arr, lCache, rCache []int, start, mid, end int) {
	// already sorted
	if arr[mid] <= arr[mid+1] {
		return
	}

	copyToCache(arr, lCache, start, mid)

	if arr[end] <= arr[start] {
		j := start

		for i := mid + 1; i <= end; i++ {
			arr[j] = arr[i]
			j++
		}

		for i := 0; i <= mid-start; i++ {
			arr[j] = lCache[i]
			j++
		}

		return
	}

	copyToCache(arr, rCache, mid+1, end)
	i, j, k := 0, 0, start-1

	for i <= mid-start || j <= end-mid-1 {
		k++

		// merge the remainder of the right array
		if i > mid-start {
			arr[k] = rCache[j]
			j++
			continue
		}

		// merge the remainder of the left array
		if j > end-mid-1 {
			arr[k] = lCache[i]
			i++
			continue
		}

		if lCache[i] <= rCache[j] {
			arr[k] = lCache[i]
			i++
		} else {
			arr[k] = rCache[j]
			j++
		}
	}
}

func copyToCache(src, cache []int, start, end int) {
	i, j := start, 0

	for i <= end {
		cache[j] = src[i]
		i++
		j++
	}
}
