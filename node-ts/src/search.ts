export interface Product {
  id: number;
  name: string;
  collection: string;
  price_usd: number;
  movement: string;
  case_material: string;
}

export function searchProduct(list: Product[], name: string): number {
  for (let i = 0; i < list.length; i++) {
    if (list[i].name === name) return i;
  }
  return -1;
}
