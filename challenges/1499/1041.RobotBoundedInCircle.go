package challenges

func isRobotBounded(instructions string) bool {
	if len(instructions) == 1 {
		if instructions[0] == 'G' {
			return false
		}

		return true
	}

	dirs := []int{0, 1, 0, -1, 0}
	var x, y, d int

	for _, mv := range instructions {
		if mv == 'G' {
			x += dirs[d]
			y += dirs[d+1]
			continue
		}

		if mv == 'L' {
			d--
			if d < 0 {
				d += 4
			}
		} else {
			d++
			d = (d % 4)
		}
	}

	if x == 0 && y == 0 {
		return true
	}

	if d != 0 {
		return true
	}

	return false
}
