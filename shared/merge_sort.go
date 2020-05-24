package shared

// import "fmt"

// MergeSort ...
type MergeSort []int

var leftCache, rightCache []int

// Sort ...
func (m *MergeSort) Sort(start, end int) {
	size := (end - start) / 2
	leftCache = make([]int, size+1)
	rightCache = make([]int, size+1)

	m.mergeSort(start, end)
}

func (m *MergeSort) mergeSort(start, end int) {
	if start >= end {
		return
	}

	mid := start + (end-start)/2

	m.mergeSort(start, mid)
	m.mergeSort(mid+1, end)

	m.merge(start, mid, end)

	// fmt.Println(start, mid, end, (*m)[start:end+1])
}

func (m *MergeSort) merge(start, mid, end int) {
	arr := *m

	// already sorted
	if arr[mid] <= arr[mid+1] {
		return
	}

	m.copyToCache(start, mid, true)

	if arr[end] <= arr[start] {
		j := start

		for i := mid + 1; i <= end; i++ {
			arr[j] = arr[i]
			j++
		}

		for i := 0; i <= mid-start; i++ {
			arr[j] = leftCache[i]
			j++
		}

		return
	}

	m.copyToCache(mid+1, end, false)
	i, j, k := 0, 0, start-1

	for i <= mid-start || j <= end-mid-1 {
		k++

		// merge the remainder of the right array
		if i > mid-start {
			arr[k] = rightCache[j]
			j++
			continue
		}

		// merge the remainder of the left array
		if j > end-mid-1 {
			arr[k] = leftCache[i]
			i++
			continue
		}

		if leftCache[i] <= rightCache[j] {
			arr[k] = leftCache[i]
			i++
		} else {
			arr[k] = rightCache[j]
			j++
		}
	}
}

func (m *MergeSort) copyToCache(start, end int, toLeft bool) {
	var target []int

	if toLeft {
		target = leftCache
	} else {
		target = rightCache
	}

	arr := *m

	for i, j := start, 0; i <= end; i++ {
		target[j] = arr[i]
		j++
	}
}
