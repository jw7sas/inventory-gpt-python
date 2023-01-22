import pandas as pd
from sqlalchemy.orm import Session
from models import Products, Categories, Suppliers

class LoadInventory:
    def __init__(self, db_connection, file_path:str):
        self.db = db_connection
        self.file_path = file_path

    def load_data(self):
        df = pd.read_csv(self.file_path)
        session = self.db.get_session()
        for index, row in df.iterrows():
            product = Products(product_name=row["Product Name"],
                                product_description=row["Product Description"],
                                product_quantity=row["Product Quantity"],
                                product_price=row["Product Price"])
            category = session.query(Categories).filter(Categories.category_name == row["Product Category"]).first()
            supplier = session.query(Suppliers).filter(Suppliers.supplier_name == row["Product Supplier"]).first()
            if not category:
                category = Categories(category_name=row["Product Category"])
                session.add(category)
                session.commit()
            if not supplier:
                supplier = Suppliers(supplier_name=row["Product Supplier"], supplier_contact_info="N/A")
                session.add(supplier)

            product.product_category = category.category_id
            session.add(product)
            session.commit()