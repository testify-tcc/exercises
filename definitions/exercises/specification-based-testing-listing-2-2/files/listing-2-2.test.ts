"use strict";

import { substringsBetween } from "./listing-2-2";

describe("should return proper result", () => {
  // Write a test case that's easy to understand and has simple results
  it("simple case", () => {
    expect().toEqual(["bc"]);
  });
  // This test case should test whether the function works properly
  // when multiple substrings should be retuned
  it("should return multiple substrings", () => {
    expect().toEqual(["bc", "bc"]);
  });
  // This test case verifies the function correctness when
  // there's more than one character in the open and close tags
  it("open and close tags that are longer than one char", () => {
    expect().toEqual(["bc", "bf"]);
  });
});
