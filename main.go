package main

import (
	"bufio"
	"flag"
	"fmt"
	p0 "go-problems/p0"
	p1 "go-problems/p1"
	s "go-problems/shared"
	"os"
	"strconv"
	"strings"
)

func main() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT
	n, k := input()

	fmt.Println(getRemainder(n, k))
}

var arr = []int{
	1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10,
	4, 12, 6, 8, 8, 16, 6, 18, 8, 12, 10, 22,
	8, 20, 12, 18, 12, 28, 8, 30, 16, 20, 16, 24,
	12, 36, 18, 24, 16, 40, 12, 42, 20, 24, 22, 46,
	16, 42,
}

func getEulerVal(num int) int {
	if num <= 50 {
		return arr[num-1]
	}

	return 0
}

func getRemainder(n, k int) int {
	if n%k == 0 {
		return 0
	}

	e := getEulerVal(k)
	r := n % e
	val := 1

	var b int

	if n > k {
		b = n % k
	} else {
		b = n
	}

	for i := 0; i < r; i++ {
		val = (val * b)
	}

	aval := 1
	for i := 0; i < n; i++ {
		aval = (aval * n)
	}

	fmt.Println(n, k, e, r, b, val, aval%k)

	return val % k
}

func input() (int, int) {
	reader := bufio.NewReader(os.Stdin)
	text, _ := reader.ReadString('\n')

	input := strings.Split(text, " ")

	n, err := strconv.Atoi(input[0])
	if err != nil {
		fmt.Println(err)
	}

	k, err := strconv.Atoi(strings.TrimSpace(input[1]))
	if err != nil {
		fmt.Println(err)
	}

	return n, k
}

func main1() {
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
