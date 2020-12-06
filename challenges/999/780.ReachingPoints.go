package challenges

/**
A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).

Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.

Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True

Note:

sx, sy, tx, ty will all be integers in the range [1, 10^9]
*/

// idea is that from (tx, ty), there's only 1 way to reach
// (sx, sy), since (tx, ty) --> (tx-ty, ty) if tx > ty, or
// (tx, ty-tx) if ty > tx; use modula to speed up the process,
// and the end game is either (sx, sy + k*sx) or (sx + k*sy, sy),
// otherwise, we can't reach the end
func reachingPoints(sx int, sy int, tx int, ty int) bool {
	if tx < sx || ty < sy {
		return false
	}

	if sx == tx && sy == ty {
		return true
	}

	// decending from (tx, ty) to the origin, use modula to
	// get it faster because (tx, tx+k*ty) can be reduced to
	// (tx, ty) in 1 step, instead of k steps.
	for tx > sx && ty > sy {
		if tx < ty {
			ty %= tx
		} else {
			tx %= ty
		}
	}

	// check if we're in one of the end games: (sx, sy + k*sx)
	// or (sx + k*sy, sy), if not, false.
	return (tx == sx && ty >= sy && (ty-sy)%sx == 0) || (ty == sy && tx >= sx && (tx-sx)%sy == 0)
}
