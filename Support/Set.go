package support

// Set ...
type Set struct {
	store map[interface{}]struct{}
}

// NewSet ...NewSet
func NewSet() *Set {
	return &Set{make(map[interface{}]struct{})}
}

// Add ...
func (s *Set) Add(key interface{}) {
	if _, ok := s.store[key]; !ok {
		s.store[key] = struct{}{}
	}
}

// Remove ...
func (s *Set) Remove(key interface{}) {
	if _, ok := s.store[key]; ok {
		delete(s.store, key)
	}
}

// Has ...
func (s *Set) Has(key interface{}) bool {
	_, ok := s.store[key]
	return ok
}

// Clear ...
func (s *Set) Clear() {
	s.store = make(map[interface{}]struct{})
}

// ToArray ...ToArray
func (s *Set) ToArray() []interface{} {
	var ans []interface{}

	for key := range s.store {
		ans = append(ans, key)
	}

	return ans
}
