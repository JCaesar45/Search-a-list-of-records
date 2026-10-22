from search import Product, search_product

CATALOG = [
    Product(1, "Aurelian Chronograph", "Heritage", 4800, "Automatic", "Steel"),
    Product(2, "Celeste Moonphase",    "Heritage", 7200, "Automatic", "Steel"),
    Product(3, "Nocturne GMT",         "Voyager",  5600, "Automatic", "Titanium"),
    Product(4, "Solstice Dress",       "Atelier",  3900, "Hand-wound", "Rose gold"),
    Product(5, "Cascade Diver",        "Voyager",  4400, "Automatic", "Steel"),
    Product(6, "Obelisk Tourbillon",   "Atelier", 24500, "Automatic", "Platinum"),
]

def test_first_match():
    assert search_product(CATALOG, "Aurelian Chronograph") == 0

def test_middle_match():
    assert search_product(CATALOG, "Nocturne GMT") == 2

def test_last_match():
    assert search_product(CATALOG, "Obelisk Tourbillon") == 5

def test_no_match():
    assert search_product(CATALOG, "Nonexistent") == -1
