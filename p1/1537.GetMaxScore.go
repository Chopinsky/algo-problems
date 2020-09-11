package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// GMSProblems ...
type GMSProblems struct {
	set []*GMS
}

// Solve ...
func (p *GMSProblems) Solve() {
	fmt.Println()

	start := time.Now()

	for j := 0; j <= 0; j++ {
		for i, p := range p.set {
			result := p.solve()

			if j == 0 {
				s.Print(i, p.output, result)
			}
		}
	}

	fmt.Println("Algorithm finished in:", time.Since(start))
}

// GMS ...
type GMS struct {
	data   []int
	alt    []int
	output int
}

// CreateGMS ...
func CreateGMS() s.Problem {
	set := make([]*GMS, 0, 4)

	set = append(set, &GMS{
		data:   []int{},
		alt:    []int{},
		output: 0,
	})

	return &GMSProblems{set}
}

func (p *GMS) solve() int {
	return maxSum(p.data, p.alt)
}

func maxSum(nums1 []int, nums2 []int) int {
	mod := int64(1e9 + 7)
	m1 := make(map[int]bool)
	s1, s2 := len(nums1), len(nums2)
	joints := make([]int, 0, len(nums1))

	for _, v := range nums1 {
		m1[v] = true
	}

	for _, v := range nums2 {
		if m1[v] {
			joints = append(joints, v)
		}
	}

	var dp1, dp2 int64
	i, j, p := 0, 0, 0
	limit := len(joints)

	for p <= limit {
		for i < s1 && (p == limit || nums1[i] <= joints[p]) {
			dp1 += int64(nums1[i])
			i++
		}

		for j < s2 && (p == limit || nums2[j] <= joints[p]) {
			dp2 += int64(nums2[j])
			j++
		}

		if p < limit {
			m := max64(dp1, dp2)
			dp1, dp2 = m, m
		}

		p++
	}

	// fmt.Println(dp1, dp2)
	// fmt.Println(dp1 % mod, dp2 % mod)
	// fmt.Println(joints)

	return int(max64(dp1, dp2) % mod)
}

func max64(a, b int64) int64 {
	if a >= b {
		return a
	}

	return b
}
