"use strict";

import { IProductStorage, Nullable, Product } from "./utils";

export class Basket {
  private totalValue: number = 0;
  private productStorage: IProductStorage;

  constructor(productStorage: IProductStorage) {
    this.productStorage = productStorage;
  }

  public add(product: Nullable<Product>, qtyToAdd: number): void {
    // BEGINNING EDITING SECTION
    // ENDING EDITING SECTION
  }

  public remove(product: Nullable<Product>): void {
    // BEGINNING EDITING SECTION
    // ENDING EDITING SECTION
  }

  public getTotalValue(): number {
    return this.totalValue;
  }

  public hasProduct(product: Product): boolean {
    return this.productStorage.has(product);
  }

  public getProductQuantity(product: Product): number {
    return this.productStorage.getQuantity(product);
  }
}
