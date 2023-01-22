from faker import Faker

class DataFaker:
    def __init__(self):
        self.faker = Faker()

    def generate_name(self):
        return self.faker.name()

    def generate_email(self):
        return self.faker.email()

    def generate_phone_number(self):
        return self.faker.phone_number()

    def generate_address(self):
        return self.faker.address()

    def generate_product_name(self):
        return self.faker.random_element(
            elements=("Laptop", "Desktop", "Tablet", "Smartphone", "Television", "Camera", "Monitor"))

    def generate_product_description(self):
        return self.faker.paragraph()

    def generate_product_price(self):
        return self.faker.random_number(digits=5)

    def generate_category_name(self):
        return self.faker.random_element(
            elements=("Electronics", "Furniture", "Clothing", "Sports", "Outdoors", "Books", "Tools"))

    def generate_supplier_name(self):
        return self.faker.random_element(
            elements=("Acme Inc", "Beta Corp", "Gamma Enterprises", "Delta Inc", "Epsilon Co"))
