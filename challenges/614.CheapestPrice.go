package challenges

import "fmt"

// RunCP ..
func RunCP(n int, flights [][]int, src int, dst int, K int) int {
	inf := 9223372036854775807
	d := make([]int, n)
	temp := make([]int, n)

	for i := range d {
		if i != src {
			d[i] = inf
			temp[i] = inf
		}
	}

	// fmt.Println("post init", d)

	for i := 0; i <= K; i++ {
		for j := range flights {
			start, end, cost := flights[j][0], flights[j][1], flights[j][2]

			if d[start] != inf && d[start]+cost < d[end] {
				temp[end] = min(temp[end], d[start]+cost)
			} else {
				temp[end] = min(temp[end], d[end])
			}

			// fmt.Println("update", i, j, d[start] + cost, d[end])
		}

		d, temp = temp, d

		fmt.Println("post run", i, d)
	}

	if d[dst] == inf {
		return -1
	}

	return d[dst]
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}

// RunCP1 ..
func RunCP1(n int, flights [][]int, src int, dst int, K int) int {
	store := make(map[int][][]int)
	prices := make(map[int]int)
	stack := make([][]int, 0, n)

	for _, f := range flights {
		store[f[0]] = append(store[f[0]], f[1:])
	}

	if stop, ok := store[src]; ok {
		for _, next := range stop {
			stack = append(stack, []int{next[0], next[1], 0})

			// if p, ok := prices[next[0]]; ok {
			//   if next[1] < p {
			//     prices[next[0]] = next[1]
			//   }
			// } else {
			//   prices[next[0]] = next[1]
			// }
		}
	}

	var curr []int

	for len(stack) > 0 {
		curr, stack = stack[0], stack[1:]
		city, cost, stops := curr[0], curr[1], curr[2]

		// fmt.Println(city, cost, stops, K)

		if city == dst {
			if p, ok := prices[dst]; ok {
				if cost < p {
					prices[dst] = cost
				}
			} else {
				prices[dst] = cost
			}

			continue
		}

		if stops >= K {
			// not reaching the destination within K stops, halt
			continue
		}

		// fmt.Println("post updating", city, prices)

		if p, ok := prices[city]; ok {
			if cost >= p {
				// a better solution is queued
				continue
			}
		}

		// update the best cost
		prices[city] = cost

		if nextStops, ok := store[city]; ok {
			for _, nextCity := range nextStops {
				stack = append(stack, []int{nextCity[0], cost + nextCity[1], stops + 1})
			}
		}
	}

	// fmt.Println(prices)

	if cost, ok := prices[dst]; ok {
		return cost
	}

	return -1
}
