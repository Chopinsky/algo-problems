package challenges

import (
	"math"
	"math/rand"
)

// Solution ...
type RGSolution struct {
	r float64
	x float64
	y float64
}

func RGConstructor(radius float64, x_center float64, y_center float64) RGSolution {
	return RGSolution{
		r: radius,
		x: x_center,
		y: y_center,
	}
}

func (t *RGSolution) RandPoint() []float64 {
	deg := rand.Float64() * 2 * math.Pi
	radius := math.Sqrt(rand.Float64() * t.r * t.r)
	return []float64{t.x + radius*math.Cos(deg), t.y + radius*math.Sin(deg)}

}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(radius, x_center, y_center);
 * param_1 := obj.RandPoint();
 */
