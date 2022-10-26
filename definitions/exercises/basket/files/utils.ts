export type Nullable<T> = T | null;

export class Product {
  public id: string;
  public value: number;

  constructor(id: string, value: number) {
    this.id = id;
    this.value = value;
  }
}

export interface IProductStorage {
  getQuantity(product: Product): number;
  add(product: Product, quantity: number): void;
  remove(product: Product): void;
  has(product: Product): boolean;
}

export class ProductStorage {
  private storage = new Map<string, number>();

  public getQuantity(product: Product): number {
    const quantity = this.storage.get(product.id);
    return quantity == null ? 0 : quantity;
  }

  public add(product: Product, quantity: number): void {
    const oldQuantity = this.storage.get(product.id);
    const newQuantity = oldQuantity == null ? quantity : oldQuantity + quantity;
    this.storage.set(product.id, newQuantity);
  }

  public remove(product: Product): void {
    this.storage.delete(product.id);
  }

  public has(product: Product): boolean {
    return this.storage.has(product.id);
  }
}
