from models.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()

    def one(self, id, unit_price):
        self.id = id
        self.unit_price = unit_price
        return(self)

    def get_prices(self):
        self.cursor.execute("SELECT Product.ProductID, Product.UnitPrice FROM Product")
        return(self.cursor.fetchall())

    def update_prices(self, name_column, currency_rate):
        myresult = self.get_prices()
        for x in myresult:
            val = (float(x[1]) * currency_rate, x[0])
            self.cursor.execute("UPDATE Product SET " + name_column + "= %s WHERE ProductID = %s", val)

    def get_inf_report(self):
        self.cursor.execute("SELECT Product.ProductID, Product.DepartmentID, Product.Category, Product.IDSKU, "
                         "Product.ProductName, Product.Quantity, Product.UnitPrice, Product.UnitPriceUSD, "
                         "Product.UnitPriceEuro, Product.Ranking, Product.ProductDesc, Product.UnitsInStock, "
                         "Product.UnitsInOrder FROM Product")
        return(self.cursor.fetchall())