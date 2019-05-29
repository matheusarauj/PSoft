package crudExample.rest.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

import lombok.Data;

@Data
@Entity
public class Product {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

    private String name;
    private String description;
    private float price;

    public Product(){

    }

    public Product(String name, String description, float price){
        this.name = name;
        this.description = description;
        this.price = price;
    }

	public Product getID() {
		return null;
	}

}