package challenges

func intToRoman(num int) string {
	var top int
	base := 1000
	res := ""

	for num > 0 {
		top, num = num/base, num%base
		res += spell(top, base)
		base /= 10
	}

	return res
}

func spell(n, base int) string {
	if n == 0 {
		return ""
	}

	s := ""
	if base == 1000 {
		for i := 0; i < n; i++ {
			s += "M"
		}

		return s
	}

	if base == 100 {
		return makeSpell("C", "D", "M", n)
	}

	if base == 10 {
		return makeSpell("X", "L", "C", n)
	}

	return makeSpell("I", "V", "X", n)
}

func makeSpell(acc, low, high string, n int) string {
	if n == 4 {
		return acc + low
	} else if n == 9 {
		return acc + high
	}

	s := ""
	if n >= 5 {
		s += low
		n -= 5
	}

	for i := n; i > 0; i-- {
		s += acc
	}

	return s
}
