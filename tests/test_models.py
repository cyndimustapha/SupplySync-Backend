import unittest
from fastapi.testclient import TestClient
from main import app
from models.Products import Product
from models.Transactions import Transaction
from models.Users import User
from database.connection import conn, cursor  
from database.setup import create_tables

class TestInventoryManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        create_tables()
        Product.create_table()
        Transaction.create_table()
        User.create_table()

    def setUp(self):
        self.client = TestClient(app)
        self.conn = conn
        self.cursor = cursor
        self.cursor.execute('DELETE FROM products')
        self.cursor.execute('DELETE FROM transactions')
        self.cursor.execute('DELETE FROM users')
        self.conn.commit()

    def tearDown(self):
        # Clean up the database after each test
        self.cursor.execute('DELETE FROM products')
        self.cursor.execute('DELETE FROM transactions')
        self.cursor.execute('DELETE FROM users')
        self.conn.commit()

    def test_create_product(self):
        # Test creating a product via POST request
        product_data = {
            "name": "Test Product",
            "sku": "TEST123",
            "description": "This is a test product",
            "quantity": 100,
            "price": 50,
            "supplier": "Test Supplier"
        }
        response = self.client.post('/products', json=product_data)
        self.assertEqual(response.status_code, 200)
        new_product = response.json()
        self.assertIn('id', new_product)
        self.assertEqual(new_product['name'], product_data['name'])

if __name__ == "__main__":
    unittest.main()
