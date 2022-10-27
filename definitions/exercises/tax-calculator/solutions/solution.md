# Solution

- Pre-condition: the input must be greater than or equal to zero
- Post-condition: the output must be greater than or equal to zero as well.

If you reached to something similar to that you are in the right direction:
```typescript
export function calculateTax(value: number): number {
  if (value < 0) {
    throw new Error("Value cannot be negative");
  }

  const taxValue = value / 2 - 5;

  if (taxValue < 0) {
    throw new Error("Calculated tax value cannot be negative");
  }

  return taxValue;
}
```

You are probably thinking that since using inputs smaller than 10 would throw errors, the pre-condition should ensure inputs greater than or equal to 10, and you are correct. But for the sake of learning we didn't do that, as we it's a simple program and we need an example for post-condition.   
