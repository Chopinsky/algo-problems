package challenges

import "container/heap"

func minRefuelStops(target int, startFuel int, stations [][]int) int {
	if stations == nil || len(stations) == 0 {
		if target <= startFuel {
			return 0
		}

		return -1
	}

	// can't even reach the 1st station
	if startFuel < stations[0][0] {
		return -1
	}

	size := len(stations)
	fuels := make(fuelHeap, 0, size)
	fuel := startFuel
	var count int

	for _, s := range stations {
		for fuel < s[0] {
			if fuels.Len() == 0 {
				return -1
			}

			// fmt.Println("add oil:", add, fuels)

			fuel += fuels.Pop().(int)
			count++
		}

		// now we've reached this station, add the fuel from this station
		// to the backup queue
		fuels.Push(s[1])
	}

	for fuel < target {
		if fuels.Len() == 0 {
			return -1
		}

		fuel += fuels.Pop().(int)
		count++
	}

	return count
}

type fuelHeap []int

func (h fuelHeap) Len() int {
	return len(h)
}

func (h fuelHeap) Less(i, j int) bool {
	return h[i] > h[j]
}

func (h fuelHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *fuelHeap) Push(v interface{}) {
	val := v.(int)
	*h = append(*h, val)
	heap.Fix(h, h.Len()-1)
}

func (h *fuelHeap) Pop() interface{} {
	old := *h
	n := old.Len()

	item := old[0]
	old[0] = old[n-1]

	*h = old[:n-1]
	heap.Fix(h, 0)

	return item
}
