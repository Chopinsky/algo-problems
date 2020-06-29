package challenges

import "sort"

/**
===================
Problem:

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.

===================
Solution:

Essentially to solve the Euler Path problem: go down the path and remove the endpoints one by one, essentially forming an itinerary.
*/

func findItinerary(tickets [][]string) []string {
	stops := make(map[string][]string)
	count := 0

	for _, t := range tickets {
		stops[t[0]] = append(stops[t[0]], t[1])
		count++
	}

	for k := range stops {
		sort.Strings(stops[k])
	}

	res := make([]string, 0, count+1)
	res = dfs(stops, "JFK", res)
	size := len(res)

	for i := 0; i < size/2; i++ {
		res[i], res[size-1-i] = res[size-1-i], res[i]
	}

	return res
}

func dfs(stops map[string][]string, curr string, res []string) []string {
	var next string

	for len(stops[curr]) > 0 {
		next, stops[curr] = stops[curr][0], stops[curr][1:]
		res = dfs(stops, next, res)
	}

	res = append(res, curr)

	return res
}
