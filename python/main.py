from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from dataclasses import asdict
from search import Product, search_product

CATALOG = [
    Product(1, "Aurelian Chronograph", "Heritage", 4800, "Automatic", "Steel"),
    Product(2, "Celeste Moonphase",    "Heritage", 7200, "Automatic", "Steel"),
    Product(3, "Nocturne GMT",         "Voyager",  5600, "Automatic", "Titanium"),
    Product(4, "Solstice Dress",       "Atelier",  3900, "Hand-wound", "Rose gold"),
    Product(5, "Cascade Diver",        "Voyager",  4400, "Automatic", "Steel"),
    Product(6, "Obelisk Tourbillon",   "Atelier", 24500, "Automatic", "Platinum"),
]

app = FastAPI(title="Meridian")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.get("/products")
def list_products():
    return [asdict(p) for p in CATALOG]

@app.get("/products/{pid}")
def get_product(pid: int):
    for p in CATALOG:
        if p.id == pid:
            return asdict(p)
    raise HTTPException(status_code=404, detail="Not found")

@app.get("/search")
def search(name: str):
    idx = search_product(CATALOG, name)
    if idx == -1:
        raise HTTPException(status_code=404, detail="No match")
    return {"index": idx, "product": asdict(CATALOG[idx])}
