package challenges

func threeEqualParts(a []int) []int {
	// plan: scan part-1 from 0 to size-3, divid part-2 and part-3
	//       with equal count of 1s

	size := len(a)
	count := 0
	p0, p1, p2 := -1, -1, -1

	for _, val := range a {
		if val == 1 {
			count++
		}
	}

	if count == 0 {
		return []int{0, size - 1}
	}

	if count%3 != 0 {
		return []int{-1, -1}
	}

	// fmt.Println("base lines:", count, count/3)

	base := count / 3
	count = 0

	for i, val := range a {
		if val == 1 {
			count++
		}

		if p0 < 0 && val == 1 {
			p0 = i
			continue
		}

		if val == 1 && count > 0 && (count-1)%base == 0 {
			if p1 < 0 {
				p1 = i
				continue
			}

			p2 = i
		}

		if p2 >= 0 {
			// all boundries are identified, quit
			break
		}
	}

	// fmt.Println("start:", size-p2, p1-p0, p2-p1)

	count = size - p2
	if p1-p0 < count || p2-p1 < count {
		return []int{-1, -1}
	}

	offset := 0
	for offset < size-p2 {
		if a[p2+offset] != a[p1+offset] || a[p2+offset] != a[p0+offset] {
			return []int{-1, -1}
		}

		offset++
	}

	// fmt.Println("offset:", offset)

	return []int{p0 + offset - 1, p1 + offset}
}
