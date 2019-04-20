package utils

var void struct{}

// Set ...
type Set interface {
	Add(interface{})
	Contains(interface{}) bool
	Remove(interface{})
}

// New ...
func New(t string) Set {
	var s Set

	switch t {
	case "string":
		s = &StrSet{
			inner: make(map[string]struct{}),
		}

	default:
		s = &IntSet{
			inner: make(map[int]struct{}),
		}
	}

	return s
}

// StrSet ...
type StrSet struct {
	inner map[string]struct{}
}

// Add ...
func (s *StrSet) Add(val interface{}) {
	str, ok := val.(string)
	if !ok || len(str) == 0 {
		return
	}

	if _, ok := s.inner[str]; !ok {
		s.inner[str] = void
	}
}

// Contains ...
func (s *StrSet) Contains(val interface{}) bool {
	str, ok := val.(string)
	if !ok || len(str) == 0 {
		return false
	}

	_, contains := s.inner[str]
	return contains
}

// Remove ...
func (s *StrSet) Remove(val interface{}) {
	str, ok := val.(string)
	if !ok || len(str) == 0 {
		return
	}

	delete(s.inner, str)
}

// IntSet ...
type IntSet struct {
	inner map[int]struct{}
}

// Add ...
func (s *IntSet) Add(val interface{}) {
	i, ok := val.(int)
	if !ok {
		return
	}

	if _, ok := s.inner[i]; !ok {
		s.inner[i] = void
	}
}

// Contains ...
func (s *IntSet) Contains(val interface{}) bool {
	i, ok := val.(int)
	if !ok {
		return false
	}

	_, contains := s.inner[i]
	return contains
}

// Remove ...
func (s *IntSet) Remove(val interface{}) {
	i, ok := val.(int)
	if !ok {
		return
	}

	delete(s.inner, i)
}
