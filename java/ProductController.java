package com.meridian;
import org.springframework.web.bind.annotation.*;
import java.util.List;
import java.util.Map;

@RestController
public class ProductController {
    private final SearchService search;

    private final List<Product> catalog = List.of(
        new Product(1,"Aurelian Chronograph","Heritage",4800,"Automatic","Steel"),
        new Product(2,"Celeste Moonphase","Heritage",7200,"Automatic","Steel"),
        new Product(3,"Nocturne GMT","Voyager",5600,"Automatic","Titanium"),
        new Product(4,"Solstice Dress","Atelier",3900,"Hand-wound","Rose gold"),
        new Product(5,"Cascade Diver","Voyager",4400,"Automatic","Steel"),
        new Product(6,"Obelisk Tourbillon","Atelier",24500,"Automatic","Platinum")
    );

    public ProductController(SearchService search) { this.search = search; }

    @GetMapping("/products")
    public List<Product> all() { return catalog; }

    @GetMapping("/products/{id}")
    public Product one(@PathVariable int id) {
        return catalog.stream().filter(p -> p.id() == id).findFirst()
            .orElseThrow(() -> new RuntimeException("Not found"));
    }

    @GetMapping("/search")
    public Map<String,Object> search(@RequestParam String name) {
        int idx = search.searchProduct(catalog, name);
        if (idx == -1) return Map.of("index", -1);
        return Map.of("index", idx, "product", catalog.get(idx));
    }
}
