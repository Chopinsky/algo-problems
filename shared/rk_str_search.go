package shared

var base = 26
var mod = 101

func longestDupSubstring(s string) string {
	size := len(s)
	low, high := 0, size-1
	substr := ""

	for low <= high {
		mid := (low + high) / 2
		res := RKSearch(s, size, mid)

		// fmt.Println(low, mid, high, res)

		if res == "" {
			high = mid - 1
			continue
		}

		substr = res
		low = mid + 1
	}

	return substr
}

// RKSearch ...
func RKSearch(s string, size, l int) string {
	top := getTopBase(l)
	hashes := make(map[int][]int)
	// seen := make(map[int]bool)

	h := -1
	for i := 0; i < size-l+1; i++ {
		h = hash(s, i, i+l-1, h, top)
		if h < 0 {
			h += mod
		}

		// fmt.Println(i, h)

		if positions, ok := hashes[h]; ok {
			for _, pos := range positions {
				if s[pos:pos+l] == s[i:i+l] {
					return s[i : i+l]
				}
			}

			hashes[h] = append(hashes[h], i)
			continue
		}

		/*
			if seen[h] && strings.Contains(s[:i+l-1], s[i:i+l]) {
				return s[i:i+l]
			}
		*/

		hashes[h] = []int{i}
		// seen[h] = true
	}

	return ""
}

// rolling hash
func hash(s string, i, j, last, topBase int) int {
	if last == -1 || i == 0 {
		h := 0

		for k := i; k <= j; k++ {
			h = ((h*base)%mod + int(s[k])) % mod
		}

		return h
	}

	return (((last+mod-int(s[i-1])*topBase)*base)%mod + int(s[j])) % mod
}

func getTopBase(l int) int {
	val := 1

	for i := 0; i < l-1; i++ {
		val = (val * base) % mod
	}

	return val
}
