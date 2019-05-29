package crudExample.rest.dao;

import java.io.Serializable;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import crudExample.rest.model.Product;

@Repository
public interface ProductDao<T, ID extends Serializable> extends JpaRepository<Product, Long>{

    Product save(Product product);
    Product findById(long id);
}