import pandas as pd
from typing import List

class MakeFakeInventory:
    def __init__(self, data_faker, quantity:int):
        self.data_faker = data_faker
        self.quantity = quantity

    def create_inventory(self):
        inventory_data = []
        for i in range(self.quantity):
            product_name = self.data_faker.generate_product_name()
            product_description = self.data_faker.generate_product_description()
            product_price = self.data_faker.generate_product_price()
            product_category = self.data_faker.generate_category_name()
            product_supplier = self.data_faker.generate_supplier_name()
            product_quantity = self.data_faker.faker.random_number(digits=3)
            inventory_data.append([product_name, product_description, product_price, product_category, product_supplier, product_quantity])
        df = pd.DataFrame(inventory_data, columns=["Product Name", "Product Description", "Product Price", "Product Category", "Product Supplier", "Product Quantity"])
        df.to_csv("src/data/fake_inventory.csv", index=False)
