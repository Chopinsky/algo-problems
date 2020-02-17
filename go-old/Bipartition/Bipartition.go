package bipartition

// Person ...
type Person struct {
	id       int
	dislikes []*Person
	color    int
}

var _store map[int]*Person
var _count int

// BuildGraph ...
func BuildGraph(count int, dislikes [][]int) {
	_store = make(map[int]*Person, count)
	_count = count

	for i := 1; i <= count; i++ {
		person := &Person{
			id:       i,
			dislikes: []*Person{},
			color:    -1,
		}

		_store[i] = person
	}

	for i := 0; i < len(dislikes); i++ {
		if one, ok := _store[dislikes[i][0]]; ok {
			if two, ok := _store[dislikes[i][1]]; ok {
				one.dislikes = append(one.dislikes, two)
				two.dislikes = append(two.dislikes, one)
			}
		}
	}
}

// Search ...
func Search() (bool, [][]int) {
	red := []int{}
	blue := []int{}

	for id, person := range _store {
		if len(person.dislikes) == 0 {
			person.color = 0
			red = append(red, id)
			continue
		}

		// The group has not been dyed yet
		if person.color == -1 {
			person.color = 0
			done, r, b := dyeGroup([]*Person{person})

			if !done {
				return false, nil
			}

			if len(r) > 0 {
				red = append(red, r...)
			}

			if len(b) > 0 {
				blue = append(blue, b...)
			}
		}
	}

	result := make([][]int, 2)
	result[0] = red
	result[1] = blue

	return true, result
}

func dyeGroup(queue []*Person) (confict bool, red, blue []int) {
	var target int
	var curr *Person

	for {
		if len(queue) == 0 {
			break
		}

		curr = queue[0]
		queue = queue[1:]

		if curr != nil {
			if curr.color == 0 {
				target = 1
				red = append(red, curr.id)
			} else {
				target = 0
				blue = append(blue, curr.id)
			}

			for _, dislike := range curr.dislikes {
				if dislike.color == -1 {
					queue = append(queue, dislike)
				}

				if !dislike.dye(target) {
					return false, nil, nil
				}
			}
		}
	}

	return true, red, blue
}

func (person *Person) dye(color int) bool {
	if person.color == color {
		return true
	}

	if person.color == -1 {
		person.color = color
		return true
	}

	return false
}
