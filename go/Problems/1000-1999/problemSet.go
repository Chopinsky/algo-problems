package problems

import (
	"errors"
	"fmt"

	i "../interface"
)

// MakeProblemSet ...
func MakeProblemSet(num int) (i.Problem, string, error) {
	var p i.Problem
	var t string

	switch num {
	case 1043:
		t = "Partition Array for Maximum Sum"
		p = CreatePAMS()

	case 1092:
		t = "Shortest Common Super-Sequence"
		p = CreateSCSS()

	case 1024:
		t = "Video Stitching"
		p = CreateVS()

	case 1019:
		t = "Next Greater Node"
		p = CreateNGN()

	case 1105:
		t = "Filling Bookcase Shelf"
		p = CreateFBS()

	case 1106:
		t = "Parsing Boolean Expression"
		p = CreatePBE()

	case 1124:
		t = "Longest Well-Performing Interval"
		p = CreateLPI()

	case 1125:
		t = "Smallest Sufficient Team"
		p = CreateSST()

	case 1129:
		t = "Shortest Path with Alternative colors"
		p = CreateSPC()

	case 1140:
		t = "Stone Game II"
		p = CreateSGII()

	case 1145:
		t = "Binary Tree Coloring"
		p = CreateBTC()

	case 1110:
		t = "DeleteNodesAndReturnForest"
		p = CreateDNRF()

	case 1155:
		t = "Num of Dice Rools with Target Sum"
		p = CreateNDR()

	case 1172:
		t = "Dinner Plate Stack"
		p = CreateDPS()

	case 1178:
		t = "Number of Valid Words for Each Puzzle"
		p = CreateNVW()

	case 1187:
		t = "Make the Array Strictly Increasing"
		p = CreateMAI()

	case 1191:
		t = "K-Concaatenation Max Sum"
		p = CreateKCMS()

	case 1201:
		t = "Ugly Numbers III"
		p = CreateUNIII()

	case 1202:
		t = "Smallest String With Swaps"
		p = CreateSSS()

	case 1218:
		t = "Longest Arithmetic Subsequence with Given Difference"
		p = CreateLAS()

	case 1220:
		t = "Counting Voewls Permutations"
		p = CreateVP()

	case 1223:
		t = "Dice Roll Simulation"
		p = CreateDRS()

	case 1239:
		t = "Max Len of a Concatenated String with Unique Char"
		p = CreateMLS()

	case 1240:
		t = "Tiling a Rectangle with the Fewest Squares"
		p = CreateTR()

	case 1268:
		t = "Search Suggestions System"
		p = CreateSSS2()

	case 1263:
		t = "Minimum Move Game"
		p = CreateMMG()

	case 1278:
		t = "Palindrom Patition III"
		p = CreatePPIII()

	case 1283:
		t = "Smallest Divisor"
		p = CreateSD()

	case 1284:
		t = "Min Number of Flips to Convert Binary Matrix to Zero"
		p = CreateMNCBM()

	case 1292:
		t = "Max Length of Square Width with Sum Less Than Threshold"
		p = CreateMSW()

	case 1293:
		t = "Shortest Path in A Grid with Obstacles Elimination"
		p = CreateSPG()

	case 1296:
		t = "Divide Array in Sets of K Consecutive Numbers"
		p = CreateDASKCN()

	case 1298:
		t = "Maxium Number of Candies You Can Get From Boxes"
		p = CreateMCFB()

	case 1301:
		t = "Number of Paths with max Score"
		p = CreateNPMS()

	case 1312:
		t = "Minimum Insertions to Make a String a Palindrome"
		p = CreateMISP()

	case 1310:
		t = "XOR Queries of a Subarray"
		p = CreateXORQ()

	case 1319:
		t = "Number of Operations to Make Network Connected"
		p = CreateMOMNC()

	case 1320:
		t = "Minimum Distance to Type a Word with 2 Fingers"
		p = CreateMDTW()

	case 1326:
		t = "Minimum Number of Taps to Open to Water a Garden"
		p = CreateMNTWG()

	case 1335:
		t = "Minimum Difficulty of a Job Schedule"
		p = CreateMDJS()

	case 1344:
		t = "Jump Game V"
		p = CreateJGV()

	default:
		return nil, "", errors.New(fmt.Sprint("unable to find the problem: ", num))
	}

	return p, t, nil
}
