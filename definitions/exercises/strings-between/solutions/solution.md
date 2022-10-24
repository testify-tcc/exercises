# Solution

This solution aims to explain the used steps in more details.

## Step 1: Understanding the requirements, inputs and outputs

The software requirements include three parts: what the program must do (business rules), inputs and output. It's important to identify and understand all three to have a better idea of how to test it. Regarding the example, a possible reasoning would be:

- The program goal is to collect all substrings in a string that are delimited by an `open` tag and a `close` tag, which are the inputs provided by the user.
- Inputs:
  - `str` - string from which the program will extract the substrings
  - `open` - indicates the start of a substring
  - `close` - indicates the end of a substring
- Output: an array containing all substrings found by the program

## Step 2: Explore what the program does for various inputs

On this step you basically execute the program with various inputs to understand its behavior. It's an important step when you've not written the program. In case you've written it, this step may not be needed. For the example case, these are some possible tests (written in Javascript + Jest) that might help you to understand it better:

```javascript
describe("should return proper result", () => {
  // Thought 1: Let's see the program working in a simple happy case.
  it("simple case", () => {
    expect(substringsBetween("abcd", "a", "d")).toEqual(["bc"]);
  });
  
  // Thought 2: What if there are multiple substrings in the main string?
  it("should return multiple substrings", () => {
    expect(substringsBetween("abcdabcdab", "a", "d")).toEqual(["bc", "bc"]);
  });
  
  // Thought 3: I expect it to behave the same if the open and close tags are larger than a single character. Let's test whether that's really the case. 
  it("open and close tags that are longer than one char", () => {
    expect(substringsBetween("aabcddaabfddaab", "aa", "dd")).toEqual(["bc", "bf"]);
  });
});
```

## Step 3: Explore possible inputs and outputs, and identify partitions

The number of possible inputs and outputs can reach to infinity, so it's better to define a set of parameters that will be sufficient to test the correctness of the program. That's possible because even though some inputs are different, they test the same behavior, so it's better just to pick one. Check the following example:

- The inputs/output `substringsBetween("abcd", "a", "d") -> ["bc"]` are pretty much the same as `substringsBetween("xyzw", "x", "w") -> ["yz"]`.

We say that these inputs are **equivalent**. We call a set of equivalent inputs a **partition** or **class**. The idea is to find as much partitions as you can.

A good way to start is to think about the inputs separately:

- `str` can be represented by the cases:
  - Null string
  - Empty string
  - String of length 1
  - String of length $>$ 1 (any string)
- `open` can be represented by the same cases as `str`
- `close` can be represented by the same cases as `str`

 We know that the input variables are related to each other, so now we analyze the combinations between them:

- `str` contains neither the `open` and `close` tag
- `str` contains the `open` tag but not the `close` tag
- `str` contains the `close` tag but not the `open` tag
- `str` contains both the `open` and `close` tags
- `str` contains both the `open` and `close` tags multiple times

It's possible to notice that some of these cases are not mentioned in the requirements, but some times you need to rely on your experience as a tester to analyze which cases shall be tested.

The last step is to explore the outputs:

- Array of strings
  - Null array
  - Empty array
  - Single item
  - Multiple items
- Each individual string
  - Empty
  - Single character
  - Multiple characters

## Step 4: Analyze the Boundaries

Whenever you program has some kind of boundary, it's important to test its behavior when the inputs are close to this boundary. For instance, imagine a method that prints "foo" when a integer input is smaller than 10 or "bar" when greater than or equal to 10. We can say that the boundary is the division between 9 and 10. In this specific case we have two partitions, the integers smaller than 10 and integers greater than or equal to 10. When the input cross the boundary division, the program's behavior changes.

It's common to write two tests for each boundary you find. One test uses the *on point*, which is the input that is on the boundary, in this case the number 10. Also, notice that the number 10 appears in the requirements. The other test uses the *off point*, which is the point closest to the boundary that isn't in the same partition as the *on point*.

Although normally we need only two tests, one for *on point* and other for *off point*, sometimes it's good to test other cases. An example would be to change the requirement to print "bar" only when the integer input is equal to 10 and "foo" otherwise. So in this case we would have two *off points*, 9 and 11. Thus we'd need three test cases.

For the `substringsBetween` example a boundary would be when the string passes from empty to non-empty. We know that when `str` contains both `open` and `close` tags the program (possibly) starts to return something. So the tests would be:

- `str` contains both `open` and `close` tags, with no characters between them
- `str` contains both `open` and `close` tags, with characters between them.

## Step 5: Devise test cases

Once we have the inputs, outputs and boundaries analyzed, we can start to create tests. It's better to combine partitions as we can have hundreds of them, and that would be a lot of work to do. Although for this methodology we use the requirements to write tests, in this step you may need to look at the implementation as it helps to combine partitions. After checking all the found partitions and combining them, you may have the following tests:

- Exceptional cases:
  - T1: `str` is null
  - T2: `str` is empty
  - T3: `open` is null
  - T4: `open` is empty
  - T5: `close` is null
  - T6: `close` is empty
- `str` length $=$ 1
  - T7: the single character in `str` matches `open`
  - T8: the single character in `str` matches `close`
  - T9: the single character in `str` doesn't match either the `open` or `close` tag
  - T10: the single character in `str` matches both the `open` and `close` tags
- `str` length $>$ 1, `open` length $=$ 1, `close` length $=$ 1:
  - T11: `str` doesn't contain either `open` or `close` tag
  - T12: `str` contains `open` but not `close` tag
  - T13: `str` contains `close` but not `open` tag
  - T14: `str` contains both the `open` and `close` tags
  - T15: `str` contains both the `open` and `close` tags multiple times
- `str` length $>$ 1, `open` length $>$ 1, `close` length $>$ 1:
  - T16: `str` doesn't contain either `open` or `close` tag
  - T17: `str` contains `open` but not `close` tag
  - T18: `str` contains `close` but not `open` tag
  - T19: `str` contains both the `open` and `close` tags
  - T20: `str` contains both the `open` and `close` tags multiple times
- T21: `str` contains both the `open` and `close` tags with no characters between them.

## Step 6: Automate the test cases

Basically use a library of framework to code your tests.

## Step 7: Augment the test suit with creativity and experience

Experience always counts. For example, it'd be good to have tests that deal with spaces or any type of special characters in the string.

- T22: `str` contains both `open` and `close` tags (`str` length $>$ 1, `open` length $=$ 1, `close` length $=$ 1). The input `str` contains spaces.
- T23: `str` contains both `open` and `close` tags (`str` length $>$ 1, `open` length $>$ 1, `close` length $>$ 1). All three contain spaces.

Although the implementation might handle these situations generically, they may need to be tested. Hence, it's always a good idea to go through the implementation again and check for tests not mentioned in the requirements.

# Result

These are possible implementation for the tests:

```typescript
describe("should return proper result", () => {
  it("str is null or empty", () => {
    expect(substringsBetween(null, "a", "b")).toEqual(null); // T1
    expect(substringsBetween("", "a", "b")).toEqual([]); // T2
  });

  it("open is null or empty", () => {
    expect(substringsBetween("abc", null, "b")).toEqual(null); // T3
    expect(substringsBetween("abc", "", "b")).toEqual(null); // T4
  });

  it("close is null or empty", () => {
    expect(substringsBetween("abc", "a", null)).toEqual(null); // T5
    expect(substringsBetween("abc", "a", "")).toEqual(null); // T6
  });

  it("str of length 1", () => {
    expect(substringsBetween("a", "a", "b")).toEqual(null); // T7
    expect(substringsBetween("a", "b", "a")).toEqual(null); // T8
    expect(substringsBetween("a", "b", "b")).toEqual(null); // T9
    expect(substringsBetween("a", "a", "a")).toEqual(null); // T10
  });

  it("open and close of length 1", () => {
    expect(substringsBetween("abc", "x", "y")).toEqual(null); // T11
    expect(substringsBetween("abc", "a", "y")).toEqual(null); // T12
    expect(substringsBetween("abc", "x", "c")).toEqual(null); // T13
    expect(substringsBetween("abc", "a", "c")).toEqual(["b"]); // T14
    expect(substringsBetween("abcaec", "a", "c")).toEqual(["b", "e"]); // T15
    expect(substringsBetween("abcabyt byrc", "a", "c")).toEqual(["b", "byt byrc"]); // T22
  });

  it("open and close tags of different sizes", () => {
    expect(substringsBetween("aabbcc", "xx", "yy")).toEqual(null); // T16
    expect(substringsBetween("aabbcc", "aa", "yy")).toEqual(null); // T17
    expect(substringsBetween("aabbcc", "xx", "cc")).toEqual(null); // T18
    expect(substringsBetween("aabbcc", "aa", "cc")).toEqual(["bb"]); // T19
    expect(substringsBetween("aabbccaaeecc", "aa", "cc")).toEqual(["bb", "ee"]); // T20
    expect(substringsBetween("a abb ddc ca abbcc", "a a", "c c")).toEqual(["bb dd"]); // T23
  });

  it("no substring between open and close tags", () => {
    expect(substringsBetween("aabb", "aa", "bb")).toEqual([""]); // T21
  });
});
```
