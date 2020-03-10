package main

import (
	"flag"
	"fmt"
	p0 "go-problems/p0"
	p1 "go-problems/p1"
	s "go-problems/shared"
)

func main() {
	numPtr := flag.Int("n", 0, "the problem number")
	boolPtr := flag.Bool("d", false, "if we're in the debug mode")

	flag.Parse()

	number := *numPtr
	s.SetDebug(*boolPtr)

	var problem s.Problem

	if number <= 0 {
		fmt.Println("invalid problem number; expecting the number to be larger or equal to 1, but getting: ", number)
		return
	}

	if number < 1000 {
		problem = p0.CreateProblem(number)
	} else if number >= 1000 && number <= 1999 {
		problem = p1.CreateProblem(number)
	} else {
		fmt.Println("invalid problem number; expecting it to be between 1000 and 1999, but getting: ", number)
		return
	}

	if problem != nil {
		problem.Solve()
	}

	fmt.Println("done ... ")
}
