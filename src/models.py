from sqlalchemy import Column, Integer, String, Text, Date, DECIMAL, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Products(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(255), nullable=False)
    product_description = Column(Text)
    product_category = Column(Integer)
    product_quantity = Column(Integer, nullable=False)
    product_price = Column(DECIMAL(10,2), nullable=False)


class Categories(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(255), nullable=False)


class ProductCategories(Base):
    __tablename__ = 'product_categories'
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.category_id'), primary_key=True)


class Inventory(Base):
    __tablename__ = 'inventory'
    inventory_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    quantity = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)


class Transactions(Base):
    __tablename__ = 'transactions'
    transaction_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    quantity = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    type = Column(String(255), nullable=False)


class Suppliers(Base):
    __tablename__ = 'suppliers'
    supplier_id = Column(Integer, primary_key=True)
    supplier_name = Column(String(255), nullable=False)
    supplier_contact_info = Column(String(255), nullable=False)


class ProductSuppliers(Base):
    __tablename__ = 'product_suppliers'
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    supplier_id = Column(Integer, ForeignKey('suppliers.supplier_id'), primary_key=True)
