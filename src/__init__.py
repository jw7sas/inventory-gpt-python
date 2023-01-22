from load_inventory import LoadInventory
from db import DBConnection

def saveData():
    """ Método para guardar datos fake de inventarios en un sistema de inventarios"""
    db_url = "postgresql://username:password@localhost:5432/inventory"
    db = DBConnection(db_url)
    load_inventory = LoadInventory(db, "src/data/fake_inventory.csv")
    load_inventory.load_data()


if __name__ == "__main__":
    saveData()