package challenges

func canCompleteCircuit(gas []int, cost []int) int {
	var start, gasLeft, total, spent int

	// loop over the intervals: if the gasLeft can't sustain the travel from
	// start to gas station i, then reset, make i the start point; also, record
	// the total amount of the gas cost, if the total cost is larger than
	// the total gas, then the car can't finish the trip.
	//
	// assuming we start from gas station i, then there are 2 parts: [i, last]
	// cost cost1, which has to be positive in our case; then [0, i-1], which
	// has the cost2, and cost1 + cost2 = total
	for i := range gas {
		spent = gas[i] - cost[i]

		if gasLeft >= 0 {
			gasLeft += spent
		} else {
			gasLeft = spent
			start = i
		}

		total += spent
	}

	if total >= 0 {
		return start
	}

	return -1
}
