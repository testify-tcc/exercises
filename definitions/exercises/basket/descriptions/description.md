# Basket

On this exercise you are going to implement the methods `add` and `remove` from the class `Basket`. Here you are going to verify pre-conditions, post-conditions and invariants with conditional statements and explicitly throwing errors in case these conditions are not satisfied. Take a look on the test file, it may help you.

## Class `Basket`

- Attributes:
  - `totalValue`: the sum of all products values multiplied by their quantities. This value must always be greater than or equal to zero.
  - `productStorage`: a map which maps product ids to quantities.

## Method `add`

- Inputs:
  - `product`: represents a product to add into the basket
  - `qtyToAdd`: quantity of this product to be added
- Requirements:
  - In case the product already exists in the basket, the new quantity must be added to the current quantity.
  - In case any error occurs, it isn't expected any changes in the basket.
  - The `product` must be nonnull. In case it isn't, an error must be thrown with the message "Product is required".
  - The `qtyToAdd` must be greater than zero. In case it isn't, an error must be thrown with the message "Quantity has to be greater than zero".
  - The calculated `totalValue` attribute must be greater than the old `totalValue`.In case it isn't, an error must be thrown with the message "Total value should be greater than previous total value".
  - The `product` must be added to the product storage. In case it isn't, an error must be thrown with the message "Product was not inserted in the basket".

## Method `remove`
- Inputs:
  - `product`: represents the product to be removed from the basket
- Requirements:
  - The product must be removed completely, regardeless of its quantity.
  - The product's value must be removed from the `totalValue`, i.e. its value times the quantity.
  - In case any error occurs, it isn't expected any changes in the basket.
  - The `product` must be nonnull. In case it isn't, an error must be thrown with the message "Product is required".
  - The `product` must exist in the storage to be removed. In case it doesn't, an error must be thrown with the message "Product must already be in the basket".
  - The `product` must be removed from the product storage. In case it isn't, an error must be thrown with the message "Product is still in the basket".
