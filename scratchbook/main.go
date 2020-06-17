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
	solve()
}

func solve() {
	arr := []int{1, 2, 3, 4, 5, 6, 7}

	Heapify(arr)
	fmt.Println(UpdateHeap(arr, 2), arr)
	fmt.Println(UpdateHeap(arr, 5), arr)
	fmt.Println(UpdateHeap(arr, 4), arr)

	arr1 := []int{5, 9, 2, 8, 3, 4, 6, 1, 7}
	HeapSort(arr1)
	fmt.Println(arr1)

	// idx := FindLeastCommonAncestor(arr, 4, 5, false)
	// fmt.Println("Common ancestor:", idx, arr[idx])

	// idx = FindLeastCommonAncestor(arr, 4, 6, false)
	// fmt.Println("Common ancestor:", idx, arr[idx])

	// idx = FindLeastCommonAncestor(arr, 3, 4, false)
	// fmt.Println("Common ancestor:", idx, arr[idx])

	// idx = FindLeastCommonAncestor(arr, 2, 4, false)
	// fmt.Println("Common ancestor:", idx, arr[idx])
	fmt.Println(eval([]string{
		"(", "+", "5", "(", "*", "7", "8", ")", "9", "10", "33",
	}))
}

func eval(src []string) string {
	size := len(src)
	stack := make([]string, 0, size)

	for i := size - 1; i >= 0; i-- {
		if src[i] != "(" {
			stack = append(stack, src[i])
			continue
		}

		stack = calc(stack)
	}

	if len(stack) != 1 {
		return "-1"
	}

	return stack[0]
}

func calc(stack []string) []string {
	size := len(stack)
	if size < 2 {
		return stack
	}

	calcType := stack[size-1]
	curr, _ := strconv.Atoi(stack[size-2])
	last := 0

	for j := size - 3; j >= 0; j-- {
		if stack[j] == ")" {
			last = j
			break
		}

		val, _ := strconv.Atoi(stack[j])

		switch calcType {
		case "+":
			curr += val

		case "-":
			curr -= val

		case "*":
			curr *= val

		case "/":
			curr /= val
		}
	}

	stack = stack[:last]
	res := strconv.Itoa(curr)
	stack = append(stack, res)

	return stack
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
