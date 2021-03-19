package challenges

func canVisitAllRooms(rooms [][]int) bool {
	l := len(rooms)

	stack := make([]int, 0, l)
	stack = append(stack, 0)

	notVisited := make(map[int]bool, l)
	for i := 1; i < l; i++ {
		notVisited[i] = true
	}

	var curr int
	for len(stack) > 0 {
		curr, stack = stack[0], stack[1:]

		for _, r := range rooms[curr] {
			if _, ok := notVisited[r]; ok {
				delete(notVisited, r)
				stack = append(stack, r)
			}
		}

		if len(notVisited) == 0 {
			return true
		}
	}

	return false
}
