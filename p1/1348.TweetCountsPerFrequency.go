package p1

// TweetCounts ...
type TweetCounts struct {
  tweets map[string]*node
}

type node struct {
  time []int
  count map[int]int
}

func (t *TweetCounts) makeNode(name string, time int) *node {
  n := &node {
    time: []int{time},
    count: make(map[int]int),
  }

  n.count[time] = 1
  t.tweets[name] = n

  return n
}

func (n *node) update(t int) {
  // t /= 60

  n.count[t]++
  if n.count[t] > 1 {
    // already added
    return
  }

  n.time = append(n.time, 0)
  i := len(n.time)-1

  for i > 0 && t < n.time[i-1] {
    n.time[i] = n.time[i-1]
    i--
  }

  n.time[i] = t
}

func (n *node) query(start, end int) int {
  if start > n.time[len(n.time)-1] || end < n.time[0] {
    return 0
  }

  a, b := n.binarySearch(start, true), n.binarySearch(end, false)

  // fmt.Println("q:", start, end, a, b, n.time, n.count)

  total := 0
  for i := a; i <= b && i < len(n.time); i++ {
    total += n.count[n.time[i]]
  }

  return total
}

func (n *node) binarySearch(t int, isStart bool) int {
  size := len(n.time)
  l, r := 0, size

  for l < r {
    m := (l+r)/2
    val := n.time[m]

    if val == t {
      l = m
      r = m
      break
    }

    if val < t {
      l = m+1
    } else {
      r = m-1
    }
  }

  // fmt.Println("bs:", t, l, r)

  if isStart {
    for l > 0 && l < size && n.time[l-1] >= t {
      l--
    }

    for l < size && l >= 0 && n.time[l] < t {
      l++
    }

    return l
  }

  for r < size-1 && r >= 0 && n.time[r+1] <= t {
    r++
  }

  for r >= 0 && r < size && n.time[r] > t {
    r--
  }

  return r
}

// Constructor ...
func Constructor() TweetCounts {
  return TweetCounts {
    tweets: make(map[string]*node),
  }
}

// RecordTweet ...
func (t *TweetCounts) RecordTweet(tweetName string, time int)  {
  if n, ok := t.tweets[tweetName]; ok {
    n.update(time)
  } else {
    t.makeNode(tweetName, time)
  }

  // fmt.Println("added", time, t.tweets[tweetName].time)
}

// GetTweetCountsPerFrequency ...
func (t *TweetCounts) GetTweetCountsPerFrequency(freq string, tweetName string, startTime int, endTime int) []int {
  res := []int{}
  n := t.tweets[tweetName]

  if n == nil {
    return res
  }

  delta := 1
  switch freq {
    case "minute":
      delta = 60

    case "hour":
      delta = 3600

    case "day":
      delta = 24 * 3600
  }

  for s := startTime; s <= endTime; s += delta {
    end := s + delta - 1
    if end > endTime {
      end = endTime
    }

    // fmt.Println("time interval:", s, end)

    res = append(res, n.query(s, end))
  }

  return res
}
