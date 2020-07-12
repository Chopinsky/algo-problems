/**
=====================
Problem:

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

=====================
Solution:

Kind of the brutal force, but using tricks and watching for edge cases.
*/

func threeSum(nums []int) [][]int {
  size := len(nums)
  if size < 3 {
    return [][]int{}
  }

  sort.Ints(nums)
  res := make([][]int, 0, size*(size-1))

  for i, v := range nums {
    if i > 0 && v == nums[i-1] {
      continue
    }

    l, r := i+1, size-1
    for l < r {
      sum := v + nums[l] + nums[r]

      if sum > 0 {
        r--
      } else if sum < 0 {
        l++
      } else {
        res = append(res, []int{v, nums[l], nums[r]})
        l++

        for l < r && nums[l-1] == nums[l] {
          l++
        }
      }
    }
  }

  return res
}

func threeSum1(nums []int) [][]int {
  size := len(nums)
  if size < 3 {
    return [][]int{}
  }

  sort.Ints(nums)

  store := make(map[int]int, size)
  l, u := nums[0], nums[size-1]

  for i := range nums {
    store[nums[i]]++
  }

  //fmt.Println(store)

  if l > 0 {
    return [][]int{}
  }

  if u < 0 {
    return [][]int{}
  }

  res := make([][]int, 0, size*(size-1))
  last := l-1

  for idx, i := range nums {
    if i > 0 {
      break
    }

    if i == last {
      continue
    }

    last = i
    if store[i] == 0 {
      continue
    }

    store[i]--
    res = twoSum(store, res, nums[idx+1:], i)
    store[i]++
  }

  return res
}

func twoSum(m map[int]int, res [][]int, nums []int, src int) [][]int {
  tgt := -1 * src
  last := src-1

  for _, i := range nums {
    if i > tgt - i {
      break
    }

    if i == last {
      continue
    }

    last = i
    if i == (tgt - i) {
      if m[i] >= 2 {
        res = append(res, []int{src, i, i})
      }

      continue
    }

    if m[i] > 0 && m[tgt-i] > 0 {
      res = append(res, []int{src, i, tgt-i})
    }
  }

  return res
}
