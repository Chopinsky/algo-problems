package challenges

func findRepeatedDnaSequences(s string) []string {
	if len(s) <= 10 {
		return nil
	}

	ans := make(map[string]bool)
	hash, val := 0, 0

	for i := 0; i < 10; i++ {
		val = getVal(s[i])
		hash <<= 2
		hash += val
	}

	cache := make(map[int][]string)
	cache[hash] = []string{s[:10]}

	for i := 1; i <= len(s)-10; i++ {
		curr := s[i : i+10]

		if ans[curr] {
			continue
		}

		last := getVal(s[i-1])
		hash -= (last << 18)
		hash <<= 2
		hash += getVal(s[i+9])

		if arr, ok := cache[hash]; ok {
			found := false

			for _, str := range arr {
				if curr == str {
					ans[curr] = true
					found = true
					break
				}
			}

			if !found {
				cache[hash] = append(cache[hash], curr)
			}
		} else {
			cache[hash] = []string{curr}
		}
	}

	res := make([]string, 0, len(ans))
	for k := range ans {
		res = append(res, k)
	}

	return res
}

func getVal(r byte) int {
	switch r {
	case 'A':
		return 0

	case 'C':
		return 1

	case 'G':
		return 2

	case 'T':
		return 3
	}

	return 0
}
