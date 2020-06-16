package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {
	solveNested()
}

func solveNested() {
	// test := [][][]int{1, 2, []int{4, 5, []int{7}, 8}, 9}
}

func main1() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT
	n, k := input()
	arr := make([]int, k)
	start := time.Now()

	for i := 1; i <= n; i++ {
		remainder := getRemainder(i%k, i, k)
		arr[remainder] = (arr[remainder] + 1) % mod
	}

	elapsed := time.Since(start)
	fmt.Println("algo took", elapsed)

	fmt.Println(arr)
}

var arr = []int{
	1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10,
	4, 12, 6, 8, 8, 16, 6, 18, 8, 12, 10, 22,
	8, 20, 12, 18, 12, 28, 8, 30, 16, 20, 16, 24,
	12, 36, 18, 24, 16, 40, 12, 42, 20, 24, 22, 46,
	16, 42, 20,
}

var debug = false

var mod = 1000000000

func getEulerVal(num int) int {
	if num <= 50 {
		return arr[num-1]
	}

	return 0
}

// find the result of n^m % k
func getRemainder(n, m, k int) int {
	if n == 0 || n%k == 0 {
		return 0
	}

	if m == 0 || n%k == 1 {
		return 1
	}

	aval := 1
	val := 1
	b := n % k

	if debug && n == m {
		base := n % k
		for i := 0; i < m; i++ {
			aval = (aval * base) % mod
		}
	}

	gcd := gcd(n, k)
	if gcd != 1 {
		k /= gcd

		val = ((n / gcd) % k) * getRemainder(n, m-1, k)
		val %= k

		if debug && n == m {
			// fmt.Println(n, k, "gcd:", gcd)
			fmt.Println("gcd", m, val, aval%(k*gcd))
		}

		return val
	}

	e := getEulerVal(k)
	r := m % e

	for i := 0; i < r; i++ {
		val = (val * b) % mod
	}

	if debug && n == m {
		// fmt.Println(n, k, "gcd:", gcd)
		fmt.Println(n, val%k, aval%k, aval)
	}

	return val % k
}

func input() (int, int) {
	var input []string

	vals := os.Args[1:]
	if len(vals) > 0 {
		input = vals[:2]
	} else {
		reader := bufio.NewReader(os.Stdin)
		text, _ := reader.ReadString('\n')
		input = strings.Split(text, " ")
	}

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

// GCD ...
func gcd(a, b int) int {
	if a == b {
		return a
	}

	if a < b {
		a, b = b, a
	}

	for b != 0 {
		a = a % b
		a, b = b, a
	}

	return a
}
