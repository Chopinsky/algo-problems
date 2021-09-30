package shared

// StringPowerMod ...
func StringPowerMod(sa, sb string, mod int) int {
	var a, b int64
	mm := int64(mod)

	for _, char := range sa {
		a = (a*10 + int64(char-'0')) % mm
	}

	for _, char := range sb {
		b = (b*10 + int64(char-'0')) % (mm - 1)
	}

	return int(PowerMod(a, b, mm))
}

// PowerMod ... calculate (x^n % mod)
func PowerMod(x, n, mod int64) int64 {
	ans := int64(1)

	for n > 0 {
		if n&1 > 0 {
			ans = (ans * x) % mod
		}

		n >>= 1
		x = (x * x) % mod
	}

	return ans
}
