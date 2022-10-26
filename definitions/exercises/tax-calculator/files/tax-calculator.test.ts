"use strict";

import { calculateTax } from "./tax-calculator";

test("calculateTax test", () => {
  expect(calculateTax(12)).toBe(1);
  expect(() => calculateTax(-1)).toThrow("Value cannot be negative");
  expect(() => calculateTax(4)).toThrow("Calculated tax value cannot be negative");
});
