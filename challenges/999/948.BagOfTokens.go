package challenges

import "sort"

func bagOfTokensScore(tokens []int, P int) int {
	if tokens == nil || len(tokens) == 0 || P == 0 {
		return 0
	}

	sort.Ints(tokens)

	size := len(tokens)
	var sum, score int

	for _, v := range tokens {
		if v == 0 {
			score++
		}

		sum += v
	}

	// we can play them all
	if sum <= P {
		return size
	}

	// we don't have the power to play any; note that if score > 0,
	// there's a chance we can flip the most powerful coin left, and gain
	// power to play less powerful tokens, and shooting for a bigger score.
	if score == 0 && P < tokens[score] {
		return 0
	}

	best := score
	l, r := score, size

	for l < r {
		// try to spend powers to gain scores
		for P > 0 && P >= tokens[l] && l < r {
			// get the score, reduce the power
			P -= tokens[l]
			l++
			score++
		}

		if score > best {
			best = score
		}

		// nothing we can do anymore: no more exchange for powers
		if score == 0 {
			break
		}

		// now let's see if we can get more powers with scores
		if l < r && score > 0 {
			P += tokens[r-1]
			r--
			score--
		}

		// fmt.Println(l, r, P, score)
	}

	return best
}
