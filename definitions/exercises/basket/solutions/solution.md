# Solution

## Add

- Pre-conditions:
  - Product must be nonnull
  - Quantity must be greater than zero
- Post-conditions:
  - Old `totalValue` must be greater than new `totalValue`
  - The product must be added to the product storage
- Invariant: The `totalValue` must always be greater than or equal to zero.

## Remove

- Pre-conditions:
  - Product must be nonnull
  - Product storage must contain the product
- Post-conditions:
  - Product storage must not contain the product
- Invariant: The `totalValue` must always be greater than or equal to zero. 

## Code

If you reached to something similar to that you are in the right direction:
```typescript
public add(product: Nullable<Product>, qtyToAdd: number): void {
  // BEGINNING EDITING SECTION
  if (product == null) {
    throw new Error("Product is required");
  }

  if (qtyToAdd <= 0) {
    throw new Error("Quantity has to be greater than zero");
  }

  const oldTotalValue = this.totalValue;
  const newTotalValue = oldTotalValue + product.value*qtyToAdd;

  if (oldTotalValue > newTotalValue) {
    throw new Error("Total value should be greater than previous total value");
  }

  if (newTotalValue < 0) {
    throw new Error("Total value can't be negative");
  }

  this.productStorage.add(product, qtyToAdd);

  if (!this.productStorage.has(product)) {
    throw new Error("Product was not inserted in the basket");
  }

  this.totalValue = newTotalValue;
  // ENDING EDITING SECTION
}

public remove(product: Nullable<Product>): void {
  // BEGINNING EDITING SECTION
  if (product == null) {
    throw new Error("Product is required");
  }

  if (!this.productStorage.has(product)) {
    throw new Error("Product must already be in the basket");
  }

  const productQuantity = this.productStorage.getQuantity(product);
  const oldTotalValue = this.totalValue;
  const newTotalValue = oldTotalValue - product.value*productQuantity;

  if (newTotalValue < 0) {
    throw new Error("Total value can't be negative");
  }

  this.productStorage.remove(product);

  if (this.productStorage.has(product)) {
    throw new Error("Product is still in the basket");
  }

  this.totalValue = newTotalValue;
  // ENDING EDITING SECTION
}
```

You are probably thinking that since using inputs smaller than 10 would throw errors, the pre-condition should ensure inputs greater than or equal to 10, and you are correct. But for the sake of learning we didn't do that, as we it's a simple program and we need an example for post-condition.   
