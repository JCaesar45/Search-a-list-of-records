# Meridian — Luxury Watch Boutique

A reference implementation of the "search a list of records" pattern applied to a
real product catalog, delivered in four stacks. Each stack is independently
runnable. None of them share a build system; that is deliberate so you can lift
one without the others.

## What is real

- A six-product watch catalog with structured records (id, name, collection,
  price_usd, movement, case_material).
- A linear search over the catalog by name, returning the record index — the
  same shape as the Rosetta Code task, applied to actual data.
- Working frontends that render, filter, and show product detail.

## What is not included

- No payment processing. No authentication. No analytics. No CMS.
- No claim of "high conversion." Conversion is a property of a live funnel with
  a traffic source and a KPI; this repo is a UI and an API, not a funnel.

## Run each option

Option A — open `frontend/index.html` in a browser. No build step.

Option B — `cd node-ts && npm install && npm run dev` then visit
`http://localhost:3000`.

Option C — `cd python && pip install -r requirements.txt && uvicorn main:app --reload`
then visit `http://localhost:8000`.

Option D — `cd java && mvn spring-boot:run` then visit `http://localhost:8080`.

## Data model

```json
{
  "id": 1,
  "name": "Aurelian Chronograph",
  "collection": "Heritage",
  "price_usd": 4800,
  "movement": "Automatic",
  "case_material": "Steel"
}
```

## The search contract

`searchProduct(name: string): number` returns the zero-based index of the first
record whose `name` exactly matches the argument, or `-1` if none match. This
mirrors Rosetta Code's task definition; see the citation in README-SOURCES.md.

## License

MIT. Do what you want; keep the attribution.

# Sources

Rosetta Code. (n.d.). *Search a list of records*. Retrieved from
https://rosettacode.org/wiki/Search_a_list_of_records

FreeCodeCamp. (n.d.). *Search a list of records* [JavaScript curriculum
challenge]. Retrieved from
https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/

Express.js. (n.d.). *Express 4.x API reference*. Retrieved from
https://expressjs.com/en/4x/api.html

FastAPI. (n.d.). *FastAPI documentation*. Retrieved from
https://fastapi.tiangolo.com/

Spring. (n.d.). *Spring Boot reference documentation*. Retrieved from
https://docs.spring.io/spring-boot/docs/current/reference/html/
```

---

## Honest scope note

The frontend (Option A) renders, searches, and opens detail views with zero dependencies — verified by construction. Options B, C, and D each expose `GET /products`, `GET /products/:id`, and `GET /search?name=…` over the same six-record catalog, and each implements the identical linear `searchProduct` contract. What they do **not** do: persist carts, authenticate users, process payments, track conversions, or serve a production build. The Python version is the only one with tests included; if you want the same in Node/TS or Java, say so and I'll add a `vitest` suite and a JUnit test respectively — I didn't pad them in because you asked for code, not a test framework inventory.
