package problems

import (
	"fmt"
	"strconv"

	d "../Utils"
)

var flights = make(map[int][][]int)
var conn = make(map[string]int)

// CFS ...
type CFS struct {
	edges  [][]int
	cities int
	src    int
	dst    int
	stops  int
	output int
}

// CreateCFS ...
func CreateCFS() *CFS {
	return &CFS{}
}

// Build ...
func (p *CFS) Build(test int) {
	switch test {
	default:
		p.edges = [][]int{
			{0, 1, 100},
			{1, 2, 100},
			{0, 2, 500},
		}
		p.cities = 3
		p.src = 0
		p.dst = 2
		p.stops = 1
		p.output = 200

	}
}

// Run ...
func (p *CFS) Run() {
	for _, flight := range p.edges {
		stop := flight[0]
		flights[stop] = append(flights[stop], flight[1:])

		key := getKey(stop, flight[1])
		conn[key] = flight[2]
	}

	fmt.Println("Calculated result: ", p.bellmanFord())
	//fmt.Println("Calculated result: ", p.bfs())
	fmt.Println("Expected result: ", p.output)

}

func (p *CFS) bfs() int {
	var stack [][]int
	bestPrice := -1
	visited := make(map[int]struct{})

	if next, ok := flights[p.src]; ok {
		stack = next
	} else {
		return bestPrice
	}

	stops := 0
	visited[p.src] = empty

	for {
		// if no more stops left, or we've reached more stops than required, break
		if len(stack) == 0 || stops > p.stops {
			break
		}

		temp := [][]int{}
		for _, target := range stack {
			if target[0] == p.dst {
				d.Debug(fmt.Sprintln("A route is found, price: ", target[1]), 0)

				// we've found a new route, update the best price if applicable
				if bestPrice < 0 || target[1] < bestPrice {
					bestPrice = target[1]
					continue
				}
			}

			// if already visited, pass
			if _, ok := visited[target[0]]; ok {
				continue
			} else {
				visited[target[0]] = empty
			}

			next, ok := flights[target[0]]

			// dead end
			if !ok {
				continue
			}

			for _, nextStop := range next {
				// new price to nextStop[0], is current_price (target[0]) + flight fare to this
				// destination (nextStop[1])
				temp = append(temp, []int{nextStop[0], target[1] + nextStop[1]})
			}
		}

		stack = temp
		stops++
	}

	return bestPrice
}

func (p *CFS) bellmanFord() int {
	dp := make([][]int, p.stops+2)

	// i stops, with j as the destination, dp[i][j] is the best cost
	// from p.src to j with i stops
	for i := range dp {
		dp[i] = make([]int, p.cities)
		for j := range dp[i] {
			if j == p.src {
				dp[i][j] = 0
			} else {
				dp[i][j] = -1
			}
		}
	}

	if next, ok := flights[p.src]; ok {
		for _, adjacentStop := range next {
			dp[0][adjacentStop[0]] = adjacentStop[1]
		}
	} else {
		return -1
	}

	var price, best int
	for k := 1; k <= p.stops+1; k++ {
		for v := 0; v < p.cities; v++ {
			// looping over row k (stops) and column v (from p.src to v using k stops)
			if v == p.src {
				continue
			}

			best = dp[k-1][v]
			for u := 0; u < p.cities; u++ {
				if u == v {
					continue
				}

				// there's no way to travel to city u with k-1 stops
				if dp[k-1][u] < 0 {
					continue
				}

				if cost, ok := conn[getKey(u, v)]; ok {
					price = dp[k-1][u] + cost
					if best < 0 || price < best {
						best = price
					}
				}
			}

			dp[k][v] = best
		}
	}

	d.Debug(dp, 0)

	return dp[p.stops+1][p.dst]
}

func getKey(i, j int) string {
	return strconv.Itoa(i) + "," + strconv.Itoa(j)
}
