package com.meridian;

public record Product(
    int id,
    String name,
    String collection,
    int price_usd,
    String movement,
    String case_material
) {}
