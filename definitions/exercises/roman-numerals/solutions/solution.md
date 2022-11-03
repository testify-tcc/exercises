# Solution

## Coming up with examples

The first thing you should do is to come up with examples, which is part of TDD. Here're some cases you might think of:

* Starting with simple cases:
  * Using "I" as input, the program must return 1
  * Using "V" as input, the program must return 5
  * Using "X" as input, the program must return 10
* More than one character but without using subtraction:
  * Using "II" as input, the program must return 2
  * Using "III" as input, the program must return 3
  * Using "VI" as input, the program must return 6
  * Using "XVII" as input, the program must return 17
* Using simple subtraction:
  * Using "IV" as input, the program must return 4
  * Using "IX" as input, the program must return 9
* Composing numbers with multiple characters and using subtraction:
  * Using "XIV" as input, the program must return 14
  * Using "XXIX" as input, the program must return 29

Let's focus on corner cases (e.g. empty string) after.

## Cycle

Now that you have some examples, you should follow this steps to write the tests and the code:

1. Select the simplest example
2. Write a test case based on this example that exercises the function. The code may not even compile at this point and it'll not pass the test, but it's expected, for the feature is not implemented.
3. Write as much code as needed to make the test pass, but nothing more than that.
4. Stop and reflect about what you've done so far. You may want to refactor the code, improve the test or add more examples.
5. Repeat

## Cycle in practice

After selecting the simplest example and writing the test, you may have something like:

```typescript
"use strict";

import { convertRomanNumeral } from './roman-numerals';

describe("convertRomanNumeral", () => {
  // BEGINNING EXTRA EDITING SECTION
  // ENDING EXTRA EDITING SECTION

  // BEGINNING EDITING SECTION
  it("should convert symbol I", () => {
    expect(convertRomanNumeral("I")).toBe(1);
  });
  // ENDING EDITING SECTION
});

```

By running the test it fails as expected, as the function `convertRomanNumeral` has no implementation. So now, let's implement enough code to make the test pass:

```typescript
"use strict";

// BEGINNING EXTRA EDITING SECTION
// ENDING EXTRA EDITING SECTION

export function convertRomanNumeral(romanNumeral: string): number {
  // BEGINNING EDITING SECTION
  return 1;
  // ENDING EDITING SECTION
}

```

The test starts to pass now, but obviously it's not the definitive implementation, because it works only for one case. But that's what the TDD is about, we take baby steps by following the tests until we have the program entirely implemented.

Let's start again by taking the next example and writing a test for it:

```typescript
"use strict";

import { convertRomanNumeral } from './roman-numerals';

describe("convertRomanNumeral", () => {
  // BEGINNING EXTRA EDITING SECTION
  // ENDING EXTRA EDITING SECTION

  // BEGINNING EDITING SECTION
  it("should convert symbol I", () => {
    expect(convertRomanNumeral("I")).toBe(1);
  });
  it("should convert symbol V", () => {
    expect(convertRomanNumeral("V")).toBe(5);
  });
  // ENDING EDITING SECTION
});
```

Now, your code should pass the test:

```typescript
"use strict";

// BEGINNING EXTRA EDITING SECTION
// ENDING EXTRA EDITING SECTION

export function convertRomanNumeral(romanNumeral: string): number {
  // BEGINNING EDITING SECTION
  if (romanNumeral == "I") return 1;
  if (romanNumeral == "V") return 5; 
  return 0;
  // ENDING EDITING SECTION
}
```

That's the easiest way to make the test pass, but it's not the definitive implementation though. Also, we could do the same for all symbols, but we can generalize the implementation for both the code and the test. Let's improve the test first:

```typescript
"use strict";

import { convertRomanNumeral } from './roman-numerals';

describe("convertRomanNumeral", () => {
  // BEGINNING EXTRA EDITING SECTION
  // ENDING EXTRA EDITING SECTION

  // BEGINNING EDITING SECTION
  it("should convert one char numbers", () => {
    const romanNumbers = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 };
    Object.entries(romanNumbers).forEach(([romanNumber, value]) => {
      expect(convertRomanNumeral(romanNumber)).toBe(value);
    });
  });
  // ENDING EDITING SECTION
});
```

Then we generalize for the production code as well:

```typescript
"use strict";

// BEGINNING EXTRA EDITING SECTION
const symbolsMap: Record<string, number> = {
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000,
};
// ENDING EXTRA EDITING SECTION

export function convertRomanNumeral(romanNumeral: string): number {
  // BEGINNING EDITING SECTION
  return symbolsMap[romanNumeral];
  // ENDING EDITING SECTION
}
```

Your production code is enough to make the test pass for single-character Roman numerals. But we still need to consider the cases with more than on character. Again we start with the test:

```typescript
"use strict";

import { convertRomanNumeral } from './roman-numerals';

describe("convertRomanNumeral", () => {
  // BEGINNING EXTRA EDITING SECTION
  // ENDING EXTRA EDITING SECTION

  // BEGINNING EDITING SECTION
  it("should convert one char numbers", () => {
    const romanNumbers = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 };
    Object.entries(romanNumbers).forEach(([romanNumber, value]) => {
      expect(convertRomanNumeral(romanNumber)).toBe(value);
    });
  });

  it("should convert multiple char numbers", () => {
    expect(convertRomanNumeral("II")).toBe(2);
  });
  // ENDING EDITING SECTION
});
```

The easiest way to make the test pass would be to add "II" to the `symbolsMap`, but that's not generic and we'd need to add for all possible roman numbers, which is not possible. A possible idea would be to iterate over the roman numeral, accumulating the value by using the values stored in the `symbolsMap`. So a simple loop should make the test pass:

```typescript
"use strict";

// BEGINNING EXTRA EDITING SECTION
const symbolsMap: Record<string, number> = {
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000,
};
// ENDING EXTRA EDITING SECTION

export function convertRomanNumeral(romanNumeral: string): number {
  // BEGINNING EDITING SECTION
  let finalNumber = 0;

  for (let i = 0; i < romanNumeral.length; i++) {
    finalNumber += symbolsMap[romanNumeral.charAt(i)];
  }

  return finalNumber;
  // ENDING EDITING SECTION
}
```

Here you can see one of the many advantages of using TDD. As you go through the tests, you don't need to worry about the previous, because in case you add a bug to the previously working behavior while you are implementing the code, it'll be captured by the old tests.

The test is passing but we can still test the new functionality with more examples:

```typescript
"use strict";

import { convertRomanNumeral } from './roman-numerals';

describe("convertRomanNumeral", () => {
  // BEGINNING EXTRA EDITING SECTION
  // ENDING EXTRA EDITING SECTION

  // BEGINNING EDITING SECTION
  it("should convert one char numbers", () => {
    const romanNumbers = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 };
    Object.entries(romanNumbers).forEach(([romanNumber, value]) => {
      expect(convertRomanNumeral(romanNumber)).toBe(value);
    });
  });

  it("should convert multiple char numbers", () => {
    const romanNumbers = { "II": 2, "III": 3, "VI": 6, "XVIII": 18 };
    Object.entries(romanNumbers).forEach(([romanNumber, value]) => {
      expect(convertRomanNumeral(romanNumber)).toBe(value);
    });
  });
  // ENDING EDITING SECTION
});
```

Since both tests have the same logic, you could mix them in a single one that tests both numbers with one char and multiple chars. It's totally your choice. You could at least create a function with the logic and use it in all tests:

```typescript
"use strict";

import { convertRomanNumeral } from './roman-numerals';

describe("convertRomanNumeral", () => {
  // BEGINNING EXTRA EDITING SECTION
  function testConvertRomanNumeralForMap(romanNumbersMap: Record<string, number>) {
    Object.entries(romanNumbersMap).forEach(([romanNumber, value]) => {
      expect(convertRomanNumeral(romanNumber)).toBe(value);
    });
  }
  // ENDING EXTRA EDITING SECTION

  // BEGINNING EDITING SECTION
  it("should convert one char numbers", () => {
    testConvertRomanNumeralForMap({ "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 });
  });

  it("should convert multiple char numbers", () => {
    testConvertRomanNumeralForMap({ "II": 2, "III": 3, "VI": 6, "XVIII": 18 });
  });
  // ENDING EDITING SECTION
});
```

Your next step is to make the subtraction work. Let's start again with the test:

```typescript
"use strict";

import { convertRomanNumeral } from './roman-numerals';

describe("convertRomanNumeral", () => {
  // BEGINNING EXTRA EDITING SECTION
  function testConvertRomanNumeralForMap(romanNumbersMap: Record<string, number>) {
    Object.entries(romanNumbersMap).forEach(([romanNumber, value]) => {
      expect(convertRomanNumeral(romanNumber)).toBe(value);
    });
  }
  // ENDING EXTRA EDITING SECTION

  // BEGINNING EDITING SECTION
  it("should convert one char numbers", () => {
    testConvertRomanNumeralForMap({ "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 });
  });

  it("should convert multiple char numbers", () => {
    testConvertRomanNumeralForMap({ "II": 2, "III": 3, "VI": 6, "XVIII": 18 });
  });

  it("should convert subtractive notation", () => {
    testConvertRomanNumeralForMap({ "IV": 4, "XIV": 14, "XL": 50, "XLI": 41, "CCXCIV": 294 });
  });
  // ENDING EDITING SECTION
});
```

A possible way to make the function pass the last test is to make it loop backwards (from right to left) through the roman number. Accumulating each number to the final result. In case the current number is smaller than its right neighboor, then its value should be subtracted instead of added. Let's implement it then:

```typescript
"use strict";

// BEGINNING EXTRA EDITING SECTION
const symbolsMap: Record<string, number> = {
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000,
};
// ENDING EXTRA EDITING SECTION

export function convertRomanNumeral(romanNumeral: string): number {
  // BEGINNING EDITING SECTION
  let finalNumber = 0;
  let lastNeighboor = 0;
  let currentNumber = 0;

  for (let i = romanNumeral.length - 1; i >= 0; i--) {
    currentNumber = symbolsMap[romanNumeral.charAt(i)];
    finalNumber += currentNumber < lastNeighboor ? -currentNumber : currentNumber;
    lastNeighboor = currentNumber;
  }

  return finalNumber;
  // ENDING EDITING SECTION
}
```

Now you should stop and reflect about what you've done and what you can do better. The function works percetly for the test cases you created. Should you improve the tests? Should you refactor the production code? Shoud you test corner cases? The answers to these questions depend on what you and your team wants.

## Possible corner cases to test

* What happens when the romanNumeral is empty or null?
* What if the romanNumeral contains chars that are not roman symbols, such as "@" or even empty chars?
