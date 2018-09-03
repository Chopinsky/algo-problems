package lru

import (
	"errors"
	"fmt"
)

type node struct {
	key   int
	value int
	freq  int
	prev  *node
	next  *node
}

type list struct {
	head *node
	tail *node
}

// Cache ...
type Cache struct {
	store    *list
	storeMap map[int]*node
	capacity int
}

// InitCache ...
func InitCache(capacity int) (*Cache, error) {
	if capacity < 1 {
		return nil, errors.New("Cache capacity must be equal or larger than 1")
	}

	head := new(node)
	tail := new(node)

	head.prev = nil
	head.next = tail

	tail.prev = head
	tail.next = nil

	cache := &Cache{
		&list{head, tail},
		make(map[int]*node),
		1,
	}

	if err := cache.SetCapacity(capacity); err != nil {
		return nil, err
	}

	return cache, nil
}

// SetCapacity ...
func (cache *Cache) SetCapacity(c int) error {
	if c == cache.capacity {
		return nil
	}

	if c < 1 {
		return fmt.Errorf("Cache capacity must be larger than 1, but receiving %d", c)
	}

	if c < cache.capacity {
		cache.shrinkBy(cache.capacity - c)
	}

	cache.capacity = c
	return nil
}

// Put ...
func (cache *Cache) Put(key, value int) {
	if n := cache.storeMap[key]; n != nil {
		if n.value != value {
			n.value = value
		}

		cache.touch(n)
		return
	}

	newNode := &node{
		key,
		value,
		1,
		nil,
		nil,
	}

	cache.storeMap[key] = newNode
	cache.store.push(newNode)

	size := len(cache.storeMap)
	if size > cache.capacity {
		cache.shrinkBy(size - cache.capacity)
	}
}

// Get ...
func (cache *Cache) Get(key int) int {
	if n := cache.storeMap[key]; n != nil {
		cache.touch(n)
		return n.value
	}

	return -1
}

func (cache *Cache) touch(node *node) {
	node.freq++

	node.detach()
	cache.store.push(node)
}

func (cache *Cache) shrinkBy(count int) {
	for {
		if node := cache.store.pop(); node != nil {
			delete(cache.storeMap, node.key)

			count--
			if count == 0 {
				break
			}
		} else {
			break
		}
	}
}

func (node *node) detach() {
	if node.prev == nil || node.next == nil {
		return
	}

	next := node.next
	prev := node.prev

	prev.next = next
	next.prev = prev

	node.prev = nil
	node.next = nil
}

func (l *list) pop() *node {
	if l == nil || l.tail == nil || l.tail.prev == nil {
		return nil
	}

	curr := l.tail.prev
	if curr.prev == nil {
		// if head node, no need to continue
		return nil
	}

	curr.detach()
	return curr
}

func (l *list) push(n *node) {
	if n == nil || l.head.next == nil {
		return
	}

	next := l.head.next
	l.head.next = n
	next.prev = n

	n.prev = l.head
	n.next = next
}
