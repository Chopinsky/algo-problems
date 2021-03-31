package challenges

//lint:file-ignore U1000 Ignore all unused code, it's generated

/**
You want to form a target string of lowercase letters.

At the beginning, your sequence is target.length '?' marks.  You also have a stamp of lowercase letters.

On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.  You can make up to 10 * target.length turns.

For example, if the initial sequence is "?????", and your stamp is "abc",  then you may make "abc??", "?abc?", "??abc" in the first turn.  (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)

If the sequence is possible to stamp, then return an array of the index of the left-most letter being stamped at each turn.  If the sequence is not possible to stamp, return an empty array.

For example, if the sequence is "ababc", and the stamp is "abc", then we could return the answer [0, 2], corresponding to the moves "?????" -> "abc??" -> "ababc".

Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within 10 * target.length moves.  Any answers specifying more than this number of moves will not be accepted.

Example 1:

Input: stamp = "abc", target = "ababc"
Output: [0,2]
([1,0,2] would also be accepted as an answer, as well as some other answers.)

Example 2:

Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]

Note:

1 <= stamp.length <= target.length <= 1000
stamp and target only contain lowercase letters.
*/

func movesToStamp(stamp string, target string) []int { // unused
	m, n := len(stamp), len(target)
	done := make([]bool, n)
	q := make([]int, 0, n)
	ans := make([]int, 0, n)

	todo := make([]map[int]bool, n-m+1)
	seen := make([]map[int]bool, n-m+1)

	for i := 0; i <= n-m; i++ {
		t, s := make(map[int]bool), make(map[int]bool)

		for j := 0; j < m; j++ {
			if stamp[j] == target[i+j] {
				// the char can be stamped from starting position `i`
				s[i+j] = true
			} else {
				// the char can't be stamped from starting position `i`
				t[i+j] = true
			}
		}

		if len(t) == 0 {
			ans = append(ans, i)
			for j := i; j < i+m; j++ {
				if !done[j] {
					q = append(q, j)
					done[j] = true
				}
			}
		}

		todo[i] = t
		seen[i] = s
	}

	// fmt.Println(q, done, todo, seen)

	var pos int
	count := len(q)

	for len(q) > 0 && count < n {
		pos, q = q[0], q[1:]

		// fmt.Println("iter:", pos, q)

		// check the windows with starting position `i` prior to the current char
		// that's already been stamped
		for i := max(0, pos-m+1); i <= min(n-m, pos); i++ {
			// already handled and stamped, continue
			if !todo[i][pos] {
				continue
			}

			// if the window is affected -- meaning the char at `pos` is covered
			// by a later stamp; now mark it as done, as see if the current window
			// can be stamped
			delete(todo[i], pos)

			// if not all chars in this window is cleared by either self or from
			// later stamps, taking no actions
			if len(todo[i]) > 0 {
				continue
			}

			// now we stamp the window starting at `i`
			ans = append(ans, i)

			// all chars in this stamp is freed and stamped, add them to the next
			// candidate to check windows with, if they haven't been added yet.
			for j := range seen[i] {
				if !done[j] {
					q = append(q, j)
					done[j] = true
					count++
				}
			}
		}
	}

	// can't be done
	for _, res := range done {
		if !res {
			return []int{}
		}
	}

	// fmt.Println("done:", ans)

	// reverse the orders
	la := len(ans)
	for i := 0; i < la/2; i++ {
		ans[i], ans[la-i-1] = ans[la-i-1], ans[i]
	}

	return ans
}

func movesToStamp1(stamp string, target string) []int {
	m, n := len(stamp), len(target)
	tgt := []byte(target)
	seen := make([]bool, n)
	rem := n
	ans := make([]int, 0, n)

	for rem > 0 {
		found := false

		for i := 0; i+m <= n; i++ {
			if seen[i] {
				continue
			}

			count := searchSeq(stamp, tgt, i, m, n)
			// fmt.Println(i, rem, count)

			if count <= 0 {
				continue
			}

			rem -= count
			seen[i] = true
			found = true
			ans = append(ans, i)
		}

		// fmt.Println(rem, seen, found)

		if !found {
			return []int{}
		}
	}

	ll := len(ans)
	for i := 0; i < ll/2; i++ {
		ans[i], ans[ll-i-1] = ans[ll-i-1], ans[i]
	}

	return ans
}

func searchSeq(src string, tgt []byte, i, m, n int) int {
	for j := 0; j < m; j++ {
		if i+j >= n {
			return -1
		}

		if tgt[i+j] != '?' && tgt[i+j] != byte(src[j]) {
			return -1
		}
	}

	var count int
	for j := 0; j < m; j++ {
		if tgt[i+j] != '?' {
			tgt[i+j] = '?'
			count++
		}
	}

	return count
}
