package challenges

func minCostToMoveChips(position []int) int {
	var oc, ec int

	for _, v := range position {
		if v%2 == 0 {
			ec++
		} else {
			oc++
		}
	}

	return min(ec, oc)
}
