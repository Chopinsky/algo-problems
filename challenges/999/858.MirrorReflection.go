package challenges

/**
There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)

Example 1:

Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.
*/

func mirrorReflection(p int, q int) int {
	if q == 0 {
		return 0
	}

	if p == q {
		return 1
	}

	g := gcd(p, q)
	m, n := p/g, q/g

	if n%2 == 1 {
		if m%2 == 1 {
			return 1
		}

		return 2
	}

	return 0
}

func gcd(p, q int) int {
	for q != 0 {
		p = p % q
		p, q = q, p
	}

	return p
}
