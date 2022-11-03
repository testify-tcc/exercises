# Roman numerals

For this exercise, you'll implement a function that converts Roman numerals (received as `String`) to Arabic numerals (returned as `Integer`). Romans used to represent numbers using 7 symbols:

* I = 1
* V = 5
* X = 10
* L = 50
* C = 100
* D = 500
* M = 1000

To represent all possible numbers, the symbols were combined following these rules:

* Digits of lower or equal value on the right are added to the higher-value digit.
* Digits of lower value on the left are subtracted from the higher-value digit.

Remember you are using TDD to solve this exercise, so both the code and test files are empty, because you are going to fill them out, and you might start by the test.

## Examples

* `convertRomanNumeral("XV") = (10 + 5) = 15`
* `convertRomanNumeral("XXIV") = (10 + 10 -1 + 5) = 24`
