If you reached to a solution similar to the one below you are in the right direction.

```javascript
"use strict";

const { sum } = require("./sum.js");

test("should return proper result", () => {
  expect(sum(1, 1)).toBe(2);
  expect(sum(-1, 1)).toBe(0);
  expect(sum(-1, -1)).toBe(-2);
});
```

If you look at the `sum()` implementation you'll probably think that just one test is enough, and you are correct! But sometimes it's important to test other cases just to be sure of the program correctness. In this exercise we tested running `sum()` with negative and positive numbers.
