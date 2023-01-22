-- Create the inventory database
CREATE DATABASE inventory;

-- Connect to the inventory database
\c inventory

-- Create the products table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    product_description TEXT,
    product_category INTEGER,
    product_quantity INTEGER NOT NULL,
    product_price DECIMAL(10,2) NOT NULL
);

-- Create the categories table
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL
);

-- Create the product_categories table
CREATE TABLE product_categories (
    product_id INTEGER REFERENCES products(product_id),
    category_id INTEGER REFERENCES categories(category_id)
);

-- Create the inventory table
CREATE TABLE inventory (
    inventory_id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id),
    quantity INTEGER NOT NULL,
    date DATE NOT NULL
);

-- Create the transactions table
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id),
    quantity INTEGER NOT NULL,
    date DATE NOT NULL,
    type VARCHAR(255) NOT NULL
);

-- Create the suppliers table
CREATE TABLE suppliers (
    supplier_id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(255) NOT NULL,
    supplier_contact_info VARCHAR(255) NOT NULL
);

-- Create the product_suppliers table
CREATE TABLE product_suppliers (
    product_id INTEGER REFERENCES products(product_id),
    supplier_id INTEGER REFERENCES suppliers(supplier_id)
);
