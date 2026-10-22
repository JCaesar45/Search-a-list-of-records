from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    id: int
    name: str
    collection: str
    price_usd: int
    movement: str
    case_material: str

def search_product(catalog: List[Product], name: str) -> int:
    for i, p in enumerate(catalog):
        if p.name == name:
            return i
    return -1
