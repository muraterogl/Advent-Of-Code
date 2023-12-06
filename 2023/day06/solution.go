package main

import (
	"fmt"
	"math"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func find_roots_int(b float64, c float64) (int, int) {
	d := b*b - 4*c
	r1 := (-b + math.Pow(d, 0.5)) / 2
	r2 := (-b - math.Pow(d, 0.5)) / 2
	if r1 > r2 {
		r1, r2 = r2, r1
	}
	if float64(int(r1)) == r1 {r1+=1}
	if float64(int(r2)) == r2 {r2-=1}
	return int(math.Ceil(r1)), int(math.Floor(r2))
}

func main() {
	raw, _ := os.ReadFile("input.txt")
	content := string(raw)
	lines := strings.Split(content, "\n")
	re := regexp.MustCompile(`\d+`)
	times := re.FindAllString(lines[0], -1)
	distances := re.FindAllString(lines[1], -1)
	part1 := 1
	for i:=0; i<len(times); i++ {
		time, _ := strconv.ParseFloat(times[i], 64)
		distance, _ := strconv.ParseFloat(distances[i], 64)
		r1, r2 := find_roots_int(-time, distance)
		part1 *= r2 - r1 + 1
	}
	fmt.Println("part 1:", part1)
	time, _ := strconv.ParseFloat(strings.Join(times, ""), 64)
	distance, _ := strconv.ParseFloat(strings.Join(distances, ""), 64)
	r1, r2 := find_roots_int(-time, distance)
	part2 := r2 - r1 + 1
	fmt.Println("part 2:", part2)
}
