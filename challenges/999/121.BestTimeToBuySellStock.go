package challenges

func maxProfit(prices []int) int {
	profit := 0
	low := -1
	high := -1

	for _, val := range prices {
		if low < 0 || val < low {
			if high >= 0 && low >= 0 {
				p := high - low
				if p > profit {
					profit = p
				}
			}

			low = val
			high = -1

			continue
		}

		if high < 0 || val > high {
			high = val
		}
	}

	if high >= 0 && low >= 0 {
		p := high - low

		if p > profit {
			profit = p
		}
	}

	return profit
}
