import express from "express";
import products from "../products.json";
import { searchProduct, Product } from "./search";

const app = express();
const catalog = products as Product[];

app.get("/products", (_req, res) => res.json(catalog));

app.get("/products/:id", (req, res) => {
  const idx = catalog.findIndex(p => p.id === Number(req.params.id));
  if (idx === -1) return res.status(404).json({ error: "Not found" });
  res.json(catalog[idx]);
});

app.get("/search", (req, res) => {
  const name = String(req.query.name ?? "");
  const idx = searchProduct(catalog, name);
  if (idx === -1) return res.status(404).json({ error: "No match", index: -1 });
  res.json({ index: idx, product: catalog[idx] });
});

app.listen(3000, () => console.log("Meridian Node/TS on http://localhost:3000"));
