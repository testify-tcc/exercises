"use strict";

import { IProductStorage, Product, ProductStorage } from "./utils";

import { Basket } from "./basket";

class MockProductStorage implements IProductStorage {
  private storage = new Map();

  public getQuantity(product: Product): number {
    return this.storage.get(product.id);
  }

  public add(product: Product, quantity: number): void {
    this.storage.set(product.id, quantity);
    return;
  }

  public remove(): void {
    return;
  }

  public has(product: Product): boolean {
    return this.storage.has(product.id);
  }
}

class MockProductStorageNoProduct extends MockProductStorage {
  public has(): boolean {
    return false;
  }
}

describe("Basket test", () => {
  function buildBasketPostErrorVerifier(productStorage: IProductStorage, basket: Basket, basketProducts: Product[]) {
    const oldBasket = new Basket(productStorage);

    basketProducts.forEach(product => {
      oldBasket.add(product, basket.getProductQuantity(product));
    });

    return (newBasket: Basket) => {
      expect(newBasket.getTotalValue()).toBe(oldBasket.getTotalValue());
      for (const product of basketProducts) {
        expect(newBasket.hasProduct(product)).toBe(true);
        expect(newBasket.getProductQuantity(product)).toBe(oldBasket.getProductQuantity(product));
      }
    };
  }

  it("add one valid product", () => {
    const product = new Product("1", 20);
    const productStorage = new ProductStorage();
    const basket = new Basket(productStorage);
    
    basket.add(product, 1);

    expect(basket.hasProduct(product)).toBe(true);
    expect(basket.getProductQuantity(product)).toBe(1);
    expect(basket.getTotalValue()).toBe(product.value);
  });

  it("add multiple valid products", () => {
    const product1 = new Product("1", 20);
    const product2 = new Product("2", 15);
    const productStorage = new ProductStorage();
    const basket = new Basket(productStorage);

    basket.add(product1, 1);
    basket.add(product2, 2);

    expect(basket.hasProduct(product1)).toBe(true);
    expect(basket.hasProduct(product2)).toBe(true);
    expect(basket.getProductQuantity(product1)).toBe(1);
    expect(basket.getProductQuantity(product2)).toBe(2);
    expect(basket.getTotalValue()).toBe(product1.value + 2*product2.value);
  });

  it("add a valid product twice", () => {
    const product = new Product("1", 20);
    const productStorage = new ProductStorage();
    const basket = new Basket(productStorage);
    
    basket.add(product, 1);

    expect(basket.hasProduct(product)).toBe(true);
    expect(basket.getProductQuantity(product)).toBe(1);
    expect(basket.getTotalValue()).toBe(product.value);

    basket.add(product, 1);

    expect(basket.hasProduct(product)).toBe(true);
    expect(basket.getProductQuantity(product)).toBe(2);
    expect(basket.getTotalValue()).toBe(2*product.value);
  });

  it("add null product", () => {
    const productStorage = new ProductStorage();
    const basket = new Basket(productStorage);
    const verifyIfBasketChangedAfterError = buildBasketPostErrorVerifier(productStorage, basket, []);

    expect(() => basket.add(null, 1)).toThrow("Product is required");
    verifyIfBasketChangedAfterError(basket);
  });

  it("add zero and negative quantity of a product", () => {
    const product = new Product("1", 20);
    const productStorage = new ProductStorage();
    const basket = new Basket(productStorage);
    const verifyIfBasketChangedAfterError = buildBasketPostErrorVerifier(productStorage, basket, []);

    expect(() => basket.add(product, 0)).toThrow("Quantity has to be greater than zero");
    expect(() => basket.add(product, -1)).toThrow("Quantity has to be greater than zero");
    verifyIfBasketChangedAfterError(basket);
  });

  it("product not inserted on basket", () => {
    const product = new Product("1", 20);
    const productStorage = new MockProductStorageNoProduct();
    const basket = new Basket(productStorage);
    const verifyIfBasketChangedAfterError = buildBasketPostErrorVerifier(productStorage, basket, []);

    expect(() => basket.add(product, 1)).toThrow("Product was not inserted in the basket");
    verifyIfBasketChangedAfterError(basket);
  });

  it("basket total value smaller than old total value after adding product", () => {
    const product1 = new Product("1", 10);
    const product2 = new Product("2", -1);
    const productStorage = new ProductStorage();
    const basket = new Basket(productStorage);

    basket.add(product1, 1);
    const verifyIfBasketChangedAfterError = buildBasketPostErrorVerifier(productStorage, basket, [product1]);

    expect(() => basket.add(product2, 1)).toThrow("Total value should be greater than previous total value");
    verifyIfBasketChangedAfterError(basket);
  });

  it("remove valid product", () => {
    const product = new Product("1", 10);
    const productStorage = new ProductStorage();
    const basket = new Basket(productStorage);
    
    basket.add(product, 1);

    const oldTotalValue = basket.getTotalValue();

    basket.remove(product);

    expect(basket.hasProduct(product)).toBe(false);
    expect(basket.getProductQuantity(product)).toBe(0);
    expect(basket.getTotalValue()).toBe(0);
    expect(oldTotalValue).toBeGreaterThan(basket.getTotalValue());
    expect(basket.getTotalValue()).toBeGreaterThanOrEqual(0);
  });

  it("remove valid product from basket with multiple products", () => {
    const product1 = new Product("1", 3);
    const product2 = new Product("2", 5);
    const productStorage = new ProductStorage();
    const basket = new Basket(productStorage);

    basket.add(product1, 3);
    basket.add(product2, 2);

    const oldTotalValue = basket.getTotalValue();

    basket.remove(product2);

    expect(basket.hasProduct(product1)).toBe(true);
    expect(basket.hasProduct(product2)).toBe(false);
    expect(basket.getProductQuantity(product1)).toBe(3);
    expect(basket.getProductQuantity(product2)).toBe(0);
    expect(basket.getTotalValue()).toBe(3*product1.value);
    expect(oldTotalValue).toBeGreaterThan(basket.getTotalValue());
  });

  it("remove null product", () => {
    const productStorage = new ProductStorage();
    const basket = new Basket(productStorage);
    const verifyIfBasketChangedAfterError = buildBasketPostErrorVerifier(productStorage, basket, []);
    
    expect(() => basket.remove(null)).toThrow("Product is required");
    verifyIfBasketChangedAfterError(basket);
  });

  it("remove product that doens't exist in basket", () => {
    const product = new Product("1", 10);
    const productStorage = new ProductStorage();
    const basket = new Basket(productStorage);
    const verifyIfBasketChangedAfterError = buildBasketPostErrorVerifier(productStorage, basket, []);
    
    expect(() => basket.remove(product)).toThrow("Product must already be in the basket");
    verifyIfBasketChangedAfterError(basket);
  });

  it("product not removed from basket", () => {
    const product = new Product("1", 10);
    const productStorage = new MockProductStorage();
    const basket = new Basket(productStorage);

    basket.add(product, 1);

    const verifyIfBasketChangedAfterError = buildBasketPostErrorVerifier(productStorage, basket, [product]);

    expect(() => basket.remove(product)).toThrow("Product is still in the basket");
    verifyIfBasketChangedAfterError(basket);
  });

  it("basket total value is negative after removing product", () => {
    const product = new Product("1", 10);
    const productStorage = new MockProductStorage();

    productStorage.add(product, 1);

    const basket = new Basket(productStorage);
    const verifyIfBasketChangedAfterError = buildBasketPostErrorVerifier(productStorage, basket, []);

    expect(() => basket.remove(product)).toThrow("Total value can't be negative");
    verifyIfBasketChangedAfterError(basket);
  });
});
