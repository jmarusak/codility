package main

import (
	"flag"
	"strconv"
	"os"
	"fmt"
)

type Celsius int

func (c Celsius) String() string {
	return fmt.Sprintf("%vC", int(c))
}

func (c *Celsius) Set(s string) error {
	i, err := strconv.Atoi(s)
	if err != nil {
		fmt.Println("not a number")
		os.Exit(1)
	}
	*c = Celsius(i)
	return nil
}

func addFlag(name string, value Celsius, usage string) *Celsius {
	t := value
	flag.Var(&t, name, usage)
	return &t
}

func main() {
	// checking if Celsius satisfies flag.Value interface
	var _ flag.Value = new(Celsius)

	var temp = addFlag("temp", 20, "the temperature")
	flag.Parse()
	fmt.Println(*temp)

}
