package challenges

// RunQC ...
import (
	"container/list"
	"sort"
)

// RunQR1 ...
func RunQR1(people [][]int) [][]int {
	size := len(people)

	if size == 0 {
		return people
	}

	sort.Slice(people, func(i, j int) bool {
		if people[i][0] == people[j][0] {
			return people[i][1] < people[j][1]
		}

		return people[i][0] < people[j][0]
	})

	result := make([][]int, size)
	jumper := make([][]int, size)

	for i := range jumper {
		jumper[i] = []int{i - 1, i + 1}
	}

	start, count := 0, 0
	init, curr := people[0][0], -1
	// pos, last := 0, 0

	for i := range people {
		p := people[i]

		// fmt.Println(p, result)

		if p[0] == init {
			result[p[1]] = p

			l, r := jumper[p[1]][0], jumper[p[1]][1]

			if l < 0 {
				// p[1] is the first 0
				start = r
			} else {
				jumper[l][1] = r
			}

			if r < size {
				jumper[r][0] = l
			}

			continue
		}

		if p[0] != curr {
			// reset the start pointer
			curr = p[0]
			count = 0
			// pos = 0
			// last = 0
		}

		jumps := 0
		pos := start

		for pos < size {
			if count+jumps == p[1] {
				// this is the spot
				result[pos] = p
				count++

				l, r := jumper[pos][0], jumper[pos][1]

				if l < 0 {
					// pos is the first 0
					start = r
				} else {
					jumper[l][1] = r
				}

				if r < size {
					jumper[r][0] = l
				}

				break
			}

			jumps++
			pos = jumper[pos][1]
		}

	}

	return result
}

// RunQR ...
func RunQR(people [][]int) [][]int {
	sort.Slice(people, func(i, j int) bool {
		if people[i][0] == people[j][0] {
			return people[i][1] < people[j][1]
		}

		if people[i][0] > people[j][0] {
			return true
		}

		return false
	})

	// fmt.Println(people)

	// solution using linked list
	output := list.New()

	for i, p := range people {
		j := p[1]
		e := output.PushBack(i)

		if j < i {
			mark := output.Back()

			for k := i; k > j; k-- {
				mark = mark.Prev()
			}

			output.MoveBefore(e, mark)
		}
	}

	indx := 0
	ans := make([][]int, len(people))

	for e := output.Front(); e != nil; e = e.Next() {
		pos := e.Value.(int)
		ans[indx] = people[pos]
		indx++
	}

	return ans
}
