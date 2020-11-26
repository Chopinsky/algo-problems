package challenges

func maxDistToClosest(seats []int) int {
	last := -1
	dist := 1
	size := len(seats)

	var d int

	for i, s := range seats {
		if s == 0 {
			if i == size-1 {
				d = size - 1 - last
				if d > dist {
					dist = d
				}
			}

			continue
		}

		if i == 0 || (last >= 0 && last+1 == i) {
			last = i
			continue
		}

		if last < 0 {
			d = i
		} else {
			d = (i - last) / 2
		}

		last = i
		if d > dist {
			dist = d
		}
	}

	return dist
}
