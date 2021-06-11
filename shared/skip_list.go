package shared

// Tower ...
type Tower struct {
	levels []*Tower
	val    int
}

// SkipList ...
type SkipList struct {
	head *Tower
}

// MakeSkipList ...
func MakeSkipList(vals []int) *SkipList {
	t := &Tower{
		val:    vals[0],
		levels: make([]*Tower, 0, 4),
	}

	return &SkipList{
		head: t,
	}
}

// Search ...
func (s *SkipList) Search(val int) bool {
	curr := s.head
	if val < curr.val {
		return false
	}

	for curr != nil {
		if val == curr.val {
			return true
		}

		found := false
		for h := len(curr.levels) - 1; h >= 0; h-- {
			if curr.levels[h] == nil || curr.levels[h].val > val {
				continue
			}

			curr = curr.levels[h]
			found = true

			break
		}

		if !found {
			break
		}
	}

	return false
}

// Delete ...
func (s *SkipList) Delete(val int) {
	curr := s.head
	if val < curr.val {
		return
	}

	if val == curr.val {
		if curr.levels[0] != nil {
			s.head = curr.levels[0]
		} else {
			s.head = nil
		}

		return
	}

	for curr != nil {
		found := false
		for h := len(curr.levels) - 1; h >= 0; h-- {
			if curr.levels[h] == nil || curr.levels[h].val > val {
				continue
			}

			if curr.levels[h].val == val {
				node := curr.levels[h]
				if len(node.levels) <= h || node.levels[h] == nil {
					curr.levels[h] = nil
				} else {
					curr.levels[h] = node.levels[h]
				}

				continue
			}

			// first
			curr = curr.levels[h]
			found = true
		}

		if !found {
			break
		}
	}
}

func (s *SkipList) Insert(val int) {

}
