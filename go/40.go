package main

import (
	"fmt"
	"strconv"
)

// An irrational decimal fraction is created by concatenating the positive integers:
// 0.123456789101112131415161718192021...
//              ^
// It can be seen that the 12th digit of the fractional part is 1.

// If dn represents the nth digit of the fractional part, find the value of the following expression.
// d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

// Question From: Nathan Grouse

func iPow(a, b int) int {
	var result int = 1

	for 0 != b {
		if 0 != (b & 1) {
			result *= a
		}
		b >>= 1
		a *= a
	}

	return result
}

func intsOfLen(l int) int {
	return iPow(10, l) - iPow(10, l-1)
}

// d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
// 1 1 5 3 7 2 1
func champDigit(d int) int {

	i := 0
	total := 0
	digitsLeft := d
	for d > total {
		i++
		digitsAtLen := intsOfLen(i) * i
		total += digitsAtLen
		if digitsLeft > digitsAtLen {
			digitsLeft -= digitsAtLen
		}
		// fmt.Println(d, digitsLeft, digitsAtLen)
	}

	whichInt := strconv.Itoa(iPow(10, i-1) + (digitsLeft-1)/i)
	digitOfInt := (digitsLeft - 1) % i
	// fmt.Println(whichInt, digitOfInt)
	digit, _ := strconv.Atoi(string([]rune(whichInt)[digitOfInt]))

	return digit
}

func main() {

	fmt.Println(champDigit(1) * champDigit(10) * champDigit(100) * champDigit(1000) * champDigit(10000) * champDigit(100000) * champDigit(1000000))
}
