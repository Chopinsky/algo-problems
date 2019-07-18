package problems

import (
	"fmt"
	"math"

	d "../Utils"
)

// SST ...
type SST struct {
	source    []string
	ppl       [][]string
	output    []int
	testCount int
}

// CreateSST ...
func CreateSST() *SST {
	return &SST{}
}

// Build ...
func (p *SST) Build(test int) {
	p.ResetGlobals()
	p.testCount = 2

	switch test {
	case 1:
		p.source = []string{"algo", "math", "java", "reactjs", "csharp", "aws"}
		p.ppl = [][]string{
			{"algo", "math", "java"},
			{"algo", "math", "reactjs"},
			{"java", "csharp", "aws"},
			{"reactjs", "csharp"},
			{"csharp", "math"},
			{"aws", "java"},
		}
		p.output = []int{1, 2}

	default:
		p.source = []string{"java", "nodejs", "reactjs"}
		p.ppl = [][]string{
			{"java"},
			{"nodejs"},
			{"nodejs", "reactjs"},
		}
		p.output = []int{0, 2}

	}
}

// ResetGlobals ...
func (p *SST) ResetGlobals() {
}

// Run ...
func (p *SST) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")

				ppl, skills := build(p.ppl, p.source)
				d.Output(findTeam2(ppl, skills), p.output)
			} else {
				ppl, skills := build(p.ppl, p.source)
				findTeam(ppl, skills)
			}
		}
	}
}

type team struct {
	members int
	skills  int
}

// returns: skill -> people who has the skill, person -> skills the person has
func build(candidates [][]string, skills []string) (map[int]int, map[int][]int) {
	skillID := make(map[string]int, len(skills))
	skillMap := make(map[int][]int, len(skills))
	peopleMap := make(map[int]int)

	// build the skill to id map
	for i := range skills {
		skillID[skills[i]] = i
		skillMap[i] = []int{}
	}

	for i := range candidates {
		// i-th people
		for j := range candidates[i] {
			// j-th skill of the i-th people, convert to skill id
			id := skillID[candidates[i][j]]

			// update the skill map and the people map
			skillMap[id] = append(skillMap[id], i)
			peopleMap[i] |= 1 << uint(id)
		}
	}

	return peopleMap, skillMap
}

func findTeam(people map[int]int, skill map[int][]int) []int {
	skillCount, peopleCount := len(skill), len(people)
	teams := []*team{}
	minTeamSize, minTeam := math.MaxInt64, 0
	candidates := skill[0]

	// the initial team
	for i := range candidates {
		teams = append(teams, &team{
			members: 1 << uint(candidates[i]),
			skills:  people[candidates[i]],
		})
	}

	// loop over the skill set and update the team
	for i := 1; i < skillCount; i++ {
		candidates = skill[i]
		skillSet := 1<<uint(i+1) - 1
		nextTeams := make([]*team, 0, len(candidates)*len(teams))
		added := make(map[int]bool)

		for j := range candidates {
			candidate := candidates[j]

			for k := range teams {
				// team already added, skip
				if added[k] {
					continue
				}

				//extract the team
				t := teams[k]

				if needPerson(skillSet, t.skills, people[candidate]) {
					// add the person to fullfil the requirement
					t = &team{
						members: t.members | 1<<uint(candidate),
						skills:  t.skills | people[candidate],
					}
				} else {
					// this existing team already meet the requirement
					added[k] = true
				}

				// update the next team list
				nextTeams = append(nextTeams, t)

				if i == skillCount-1 {
					// only run this on the last skill
					size := countPeople(t.members, peopleCount)

					if size < minTeamSize {
						minTeam = t.members
						minTeamSize = size
					}
				}
			}
		}

		teams = nextTeams
	}

	return convertToTeam(minTeam, peopleCount)
}

func findTeam2(people map[int]int, skill map[int][]int) []int {
	skillCount, peopleCount := len(skill), len(people)
	teams := make([]*team, 0, len(people)*len(skill))
	candidates := skill[0]

	// the initial team
	for i := range candidates {
		teams = append(teams, &team{
			members: 1 << uint(candidates[i]),
			skills:  people[candidates[i]],
		})
	}

	// loop over the skill set and update the team
	for i := 1; i < skillCount; i++ {
		candidates = skill[i]
		skillSet := 1<<uint(i+1) - 1

		bound := len(teams)
		for k := 0; k < bound; k++ {
			t := teams[k]
			srcMembers, srcSkills := t.members, t.skills // save off the team state, as itself could have been updated
			updated := false

			if teamMeetRequirement(srcSkills, skillSet) {
				continue
			}

			for j := range candidates {
				if teamHasPerson(srcMembers, candidates[j]) {
					continue
				}

				if updated {
					teams = append(teams, &team{
						members: srcMembers | 1<<uint(candidates[j]),
						skills:  srcSkills | people[candidates[j]],
					})
				} else {
					t.members |= 1 << uint(candidates[j])
					t.skills |= people[candidates[j]]
					updated = true
				}
			}
		}
	}

	minTeamSize, minTeam := math.MaxInt64, 0
	for i := range teams {
		// only run this on the last skill
		size := countPeople(teams[i].members, peopleCount)

		if size < minTeamSize {
			minTeam = teams[i].members
			minTeamSize = size
		}
	}

	return convertToTeam(minTeam, peopleCount)
}

func teamMeetRequirement(teamSet, skillSet int) bool {
	return skillSet&teamSet == skillSet
}

func needPerson(skillSet, teamSet, personSet int) bool {
	// the team already has the required skills so far
	if teamMeetRequirement(teamSet, skillSet) {
		return false
	}

	// there're skills that can benefit the team
	if ^(^skillSet|teamSet)&personSet > 0 {
		return true
	}

	// won't bring in required skills, skip
	return false
}

func teamHasPerson(members, person int) bool {
	return (members>>uint(person))&1 == 1
}

func countPeople(members, count int) int {
	num := 0
	base := members

	for count > 0 {
		if base&1 == 1 {
			num++
		}

		base = base >> 1
		count--
	}

	return num
}

func convertToTeam(members, count int) []int {
	team, size := make([]int, 0, count), count
	base := members

	for count > 0 {
		if base&1 == 1 {
			team = append(team, size-count)
		}

		base = base >> 1
		count--
	}

	return team
}
