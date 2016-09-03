from system.core.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()
    
    def get_all(self):
        query = "SELECT * FROM product"
        product_data = self.db.query_db(query)
        return product_data
    
    def create_product(self, data):
        query = "INSERT INTO product (name, description, price, created_at, updated_at) VALUES (:name, :description, :price, NOW(), NOW())"        
        self.db.query_db(query,data)
        return True

    def get_product(self, id):
        query = "SELECT * FROM product WHERE id = :id"
        data = {'id': id}
        product_data = self.db.query_db(query,data)[0]
        return product_data

    def update_product(self, data):
        query = "UPDATE product SET name=:name, description=:description, price=:price, updated_at = NOW() WHERE id = :id"
        return self.db.query_db(query,data)

    def destroy_product(self, id):
        query = "DELETE FROM product WHERE id=:id LIMIT 1;"
        data = {'id':id}
        self.db.query_db(query,data)
        return True
        
