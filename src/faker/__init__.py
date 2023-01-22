from data_faker import DataFaker
from fake_inventory import MakeFakeInventory

def run(products=30):
    """ Método para crear datos de un inventario por defecto. """
    data_faker = DataFaker()
    mk_inventory = MakeFakeInventory(data_faker, products)
    mk_inventory.create_inventory()


if __name__ == '__main__':
    run()