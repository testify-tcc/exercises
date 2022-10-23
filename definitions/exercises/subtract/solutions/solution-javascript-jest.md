If you reached to a solution similar to the one below you are in the right direction.

```javascript
"use strict";

const { subtract } = require("./subtract.js");

test("should return proper result", () => {
  expect(subtract(1, 1)).toBe(0);
  expect(subtract(1, -1)).toBe(2);
  expect(subtract(-1, -1)).toBe(0);
});
```

if you look at the `subtract()` implementation you'll probably think that just one test is enough, and you are correct indeed. But sometimes is important to test other cases just to be sure about the program correctness. In this exercise we tested sum between negative and positive numbers as a precaution.
