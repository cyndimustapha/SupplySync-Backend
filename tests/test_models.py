import unittest
from models.Products import Product
from models.Transactions import Transaction
from models.Users import User
import datetime
from database.setup import create_tables
from database.connection import get_db_connection

class TestModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        create_tables()

    def setUp(self):

        self.db_conn = get_db_connection()  # Adjust this based on your connection setup

    def test_create_product(self):
        # Create a new product
        product = Product(name="Test Product", sku="TP001", description="This is a test product",
                          quantity=50, price=100.0, supplier="Test Supplier")
        
        # Save the product to the database
        product.save(self.db_conn)
        
        # Retrieve the product from the database by its ID
        retrieved_product = Product.find_by_id(product.id, self.db_conn)
        
        # Assert that the retrieved product matches the original product data
        self.assertIsNotNone(retrieved_product)
        self.assertEqual(retrieved_product.name, "Test Product")
        self.assertEqual(retrieved_product.sku, "TP001")
        self.assertEqual(retrieved_product.description, "This is a test product")
        self.assertEqual(retrieved_product.quantity, 50)
        self.assertEqual(retrieved_product.price, 100.0)
        self.assertEqual(retrieved_product.supplier, "Test Supplier")

    def tearDown(self):
        # Clean up by deleting the test data from the database
        self.db_conn.execute("DELETE FROM products WHERE id = ?", (self.product.id,))
        self.db_conn.execute("DELETE FROM transactions WHERE id = ?", (self.transaction.id,))
        self.db_conn.execute("DELETE FROM users WHERE id = ?", (self.user.id,))

    def test_create_transaction(self):
        # Create a new transaction
        transaction = Transaction(user_id=1, product_id=1, date=datetime.now(), 
                                  quantity=10, total_price=100.0, type="purchase")
        
        # Save the transaction to the database
        transaction.save(self.db_conn)
        
        # Retrieve the transaction from the database by its ID
        retrieved_transaction = Transaction.find_by_id(transaction.id, self.db_conn)
        
        # Assert that the retrieved transaction matches the original transaction data
        self.assertIsNotNone(retrieved_transaction)
        self.assertEqual(retrieved_transaction.user_id, 1)
        self.assertEqual(retrieved_transaction.product_id, 1)
        self.assertEqual(retrieved_transaction.quantity, 10)
        self.assertEqual(retrieved_transaction.total_price, 100.0)
        self.assertEqual(retrieved_transaction.type, "purchase") 


    def test_create_user(self):
        # Create a new user
        user = User(email="testuser@example.com", password="testpassword", companyName="Test Company",
                    country="Test Country", city="Test City")
        
        # Save the user to the database
        user.save(self.db_conn)
        
        # Retrieve the user from the database by its ID
        retrieved_user = User.find_by_id(user.id, self.db_conn)
        
        # Assert that the retrieved user matches the original user data
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, "testuser@example.com")
        self.assertEqual(retrieved_user.password, "testpassword")  # You should hash passwords in actual applications
        self.assertEqual(retrieved_user.companyName, "Test Company")
        self.assertEqual(retrieved_user.country, "Test Country")
        self.assertEqual(retrieved_user.city, "Test City")