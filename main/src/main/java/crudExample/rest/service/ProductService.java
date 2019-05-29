package crudExample.rest.service;


import java.util.Optional;

import org.springframework.stereotype.Service;

import crudExample.exception.product.ProductNotFoundException;
import crudExample.rest.dao.ProductDao;
import crudExample.rest.model.Product;

@Service
public class ProductService {

    private final ProductDao productDao;

    ProductService(ProductDao productDao) {
        this.productDao = productDao;
    }

    public Product create(Product product){
        return productDao.save(product);
    }

    public Product update(Product productToUpdate) throws ProductNotFoundException {

        Product product = productDao.findById(productToUpdate.getID());
        if (product == null){
            throw new ProductNotFoundException("Could not update. The product does not exist.");
        }

        return productDao.save(productToUpdate);
    }

    public void delete(long id) {
        productDao.deleteById(id);
    }

    public Product findById(long id) {
        return productDao.findById(id);
    }
}