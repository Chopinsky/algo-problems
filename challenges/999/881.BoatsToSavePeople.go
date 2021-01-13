package challenges

import "sort"

/**
The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)

Note:

1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000
*/

func numRescueBoats(people []int, limit int) int {
	sort.Ints(people)

	l, r := 0, len(people)-1
	var count int

	for l <= r {
		if people[l]+people[r] <= limit {
			l++
		}

		r--
		count++
	}

	return count
}

func numRescueBoats1(people []int, limit int) int {
	counts := make(map[int]int)
	for _, p := range people {
		counts[p]++
	}

	w := make([][2]int, 0, len(counts))

	for k, v := range counts {
		w = append(w, [2]int{k, v})
	}

	sort.Slice(w, func(i, j int) bool {
		return w[i][0] < w[j][0]
	})

	var ans, idx int

	for len(w) > 0 {
		idx = len(w) - 1
		weight, count := w[idx][0], w[idx][1]

		if count <= 0 {
			w = w[:idx]
			continue
		}

		if count > 1 && 2*weight <= limit {
			ans++
			w[idx][1] -= 2

			if w[idx][1] == 0 {
				w = w[:idx]
			}

			continue
		}

		w[idx][1]--
		if w[idx][1] == 0 {
			w = w[:idx]
		}

		j := sort.Search(len(w), func(i int) bool { return w[i][0] > limit-weight }) - 1

		for j >= 0 {
			if w[j][1] > 0 {
				break
			}

			j--
		}

		if j >= 0 {
			w[j][1]--
		}

		ans++
	}

	return ans
}

func fit(w []int, counts map[int]int, limit, seats int) {
	if len(counts) == 0 {
		return
	}

	idx := sort.SearchInts(w, limit)

	if idx < len(w) && counts[w[idx]] > 0 && w[idx] == limit {
		counts[w[idx]]--
		if counts[w[idx]] == 0 {
			delete(counts, w[idx])
		}

		return
	}

	idx--

	for idx >= 0 {
		if counts[w[idx]] > 0 {
			n := min3(limit/w[idx], counts[w[idx]], seats)

			counts[w[idx]] -= n
			limit -= n * w[idx]
			seats -= n

			if counts[w[idx]] == 0 {
				delete(counts, w[idx])
			}

			break
		}

		idx--
	}

	if idx >= 0 && seats >= 1 {
		fit(w, counts, limit, seats)
	}
}

func min3(a, b, c int) int {
	if a <= b && a <= c {
		return a
	}

	if b <= a && b <= c {
		return b
	}

	return c
}
