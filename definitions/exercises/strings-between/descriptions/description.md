# Strings Between

Picture a method called `substringsBetween()` with the following requirements: 

- It searches a string for substrings delimited by a start and end tag, returning all matching substrings in an array.
- Method inputs:
  - `str` - String containing the substrings. If `null`, the value `null` must also be returned. If empty, and empty array must be returned.
  - `open` - A string used to identify the start of a substring. If `null` or empty, the method must return `null`.
  - `close` - A string used to identify the end of a substring. If `null` or empty, the method must return `null`.
- Example inputs and outputs
  - Inputs: (`str = "axcaycazc", open = "a", close = "c"`) / Output: `["x", "y", "z"]`
    - Explanation: The substrings will have the following structure: `"a<something>c"`. Thus once a substring like that is found, the value `<something>` will be added to the output.

In case you want more details, this example is used in the book's chapter 2.

Write the tests for the function `stringsBetween()` using the specification-based testing technique. Following the 7 steps explained in this section summary may help.
