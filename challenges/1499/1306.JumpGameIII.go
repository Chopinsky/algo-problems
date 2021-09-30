package challenges

func canReach(arr []int, start int) bool {
	if arr[start] == 0 {
		return true
	}

	size := len(arr)
	visited := make([]bool, size)

	stack := make([]int, 0, size)
	stack = append(stack, start)
	var curr int

	for len(stack) > 0 {
		curr, stack = stack[0], stack[1:]
		if visited[curr] {
			continue
		}

		visited[curr] = true
		nl, nr := curr+arr[curr], curr-arr[curr]

		if nl < size && !visited[nl] {
			if arr[nl] == 0 {
				return true
			}

			stack = append(stack, nl)
		}

		if nr >= 0 && !visited[nr] {
			if arr[nr] == 0 {
				return true
			}

			stack = append(stack, nr)
		}
	}

	return false
}
