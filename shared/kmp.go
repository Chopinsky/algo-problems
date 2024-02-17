package shared

// Match implements the KMP string search algorithm
// input: s - srouce string; p - pattern string to match against the source string
func Match(s, p string, count int) []int {
	size := len(p)
	ans := []int{}

	// build the prefix-jump table
	prefix := Prefix(p)
	j := 0

	// i is the pointer to the srouce string
	for i := 0; i < len(s); i++ {
		for s[i] != p[j] && j > 0 {
			// if we've reached a mismatch, find the next prefix-match that we can start with,
			// until the point where j == 0, where we shall keep moving till the next initial char
			// match
			j = prefix[j]
		}

		if s[i] == p[j] {
			// this is a char match, now both string shall move the cursor to the next char for matching
			j++
		}

		if j == size {
			// found the match, now push the start index of this match
			ans = append(ans, i-size+1)

			if len(ans) == count {
				return ans
			}

			// jump to the next match -- it could be a suffix-to-prefix match, hence non-0
			j = prefix[j]
		}
	}

	return ans
}

// Prefix ...
func Prefix(p string) []int {
	// lenght of the longest prefix of p[0:i] that is also the suffix
	size := len(p)
	prefix := make([]int, size+1)

	// j is the prefix pointer
	j := 0

	// i is the suffix pointer
	for i := 1; i < size; i++ {
		// looping back to the last matched position, or the front of the pattern
		for p[i] != p[j] && j > 0 {
			j = prefix[j]
		}

		// if there's a match, moving i, j to the next point
		if p[i] == p[j] {
			j++
		}

		// record the suffix-to-prefix position
		prefix[i+1] = j
	}

	return prefix
}
