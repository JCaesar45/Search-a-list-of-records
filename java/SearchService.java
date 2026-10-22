package com.meridian;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class SearchService {
    public int searchProduct(List<Product> catalog, String name) {
        for (int i = 0; i < catalog.size(); i++) {
            if (catalog.get(i).name().equals(name)) return i;
        }
        return -1;
    }
}
