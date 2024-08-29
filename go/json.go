package main

import (
	"fmt"
	"json"
)

type Movie struct {
	Title  string
	Year   int
	Color  bool
	Actors []string
}

func main() {
	fmt.Printf("%[1]p : %#[1]v\n", m)
}
