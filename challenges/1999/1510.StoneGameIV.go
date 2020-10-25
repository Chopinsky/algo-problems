package challenges

func winnerSquareGame(n int) bool {
	if n == 1 {
		return true
	}

	if n == 2 {
		return false
	}

	dp := make([]bool, n+1)
	dp[1] = true
	dp[2] = false
	s := 2

	for i := 3; i <= n; i++ {
		if i == s*s {
			dp[i] = true
			s++
			continue
		}

		aliceWin := false

		for j := 1; j*j < i; j++ {
			if !dp[i-j*j] {
				aliceWin = true
				break
			}
		}

		dp[i] = aliceWin
	}

	return dp[n]
}
