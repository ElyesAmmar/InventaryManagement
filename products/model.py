class Products:

    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    @property
    def verification(self):
        errors = {}
        # validate name is a string
        if not isinstance(self.name, str) or len(self.name) > 255 or not self.name:
            errors["name"] = "Name cannot be None or Empty or > 255"
        if not isinstance(self.price, float) or not self.price:
            errors["price"] = "Price cannot be None or Empty"
        if not isinstance(self.stock, int) or not self.stock:
            errors["stock"] = "Stock cannot be None or Empty"
        return errors

    def product_data(self):
        verification = self.verification
        if len(verification) == 0:
            return {
                "product_id": self.product_id,
                "name": self.name,
                "price": self.price,
                "stock": self.stock
            }
        else:
            print("errors")
            for err in verification:
                print(verification[err])
