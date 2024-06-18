import os
import sys
import pytest
from fastapi.testclient import TestClient
from datetime import datetime

# Adjust the path to make sure we can import the `main` module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app  # Now this should work

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_create_and_get_products():
    product_data = {
        "name": "Test Product",
        "sku": "TP001",
        "description": "This is a test product",
        "quantity": 50,
        "price": 100,
        "supplier": "Test Supplier"
    }
    
    create_response = client.post("/products", json=product_data)
    assert create_response.status_code == 200
    created_product = create_response.json()

    assert created_product["name"] == product_data["name"]
    assert created_product["sku"] == product_data["sku"]
    assert created_product["description"] == product_data["description"]
    assert created_product["quantity"] == product_data["quantity"]
    assert created_product["price"] == product_data["price"]
    assert created_product["supplier"] == product_data["supplier"]

    get_response = client.get("/products")
    assert get_response.status_code == 200
    products = get_response.json()

    assert any(p["name"] == product_data["name"] for p in products)

def test_update_product():
    product_data = {
        "name": "Test Product",
        "sku": "TP001",
        "description": "This is a test product",
        "quantity": 50,
        "price": 100,
        "supplier": "Test Supplier"
    }
    
    create_response = client.post("/products", json=product_data)
    assert create_response.status_code == 200
    created_product = create_response.json()
    product_id = created_product["id"]

    updated_data = {
        "name": "Updated Test Product",
        "sku": "TP001",
        "description": "This is an updated test product",
        "quantity": 100,
        "price": 150,
        "supplier": "Updated Supplier"
    }
    
    update_response = client.put(f"/products/{product_id}", json=updated_data)
    assert update_response.status_code == 200
    updated_product = update_response.json()

    assert updated_product["name"] == updated_data["name"]
    assert updated_product["sku"] == updated_data["sku"]
    assert updated_product["description"] == updated_data["description"]
    assert updated_product["quantity"] == updated_data["quantity"]
    assert updated_product["price"] == updated_data["price"]
    assert updated_product["supplier"] == updated_data["supplier"]

def test_get_low_stock_products():
    product_data = {
        "name": "Low Stock Product",
        "sku": "LSP001",
        "description": "This product has low stock",
        "quantity": 5,
        "price": 50,
        "supplier": "Low Stock Supplier"
    }
    
    create_response = client.post("/products", json=product_data)
    assert create_response.status_code == 200

    threshold = 10
    low_stock_response = client.get(f"/low_stock?threshold={threshold}")
    assert low_stock_response.status_code == 200
    low_stock_products = low_stock_response.json()

    assert any(p["name"] == product_data["name"] for p in low_stock_products)

def test_create_and_get_transactions():
    product_data = {
        "name": "Test Product",
        "sku": "TP001",
        "description": "This is a test product",
        "quantity": 50,
        "price": 100,
        "supplier": "Test Supplier"
    }
    
    create_product_response = client.post("/products", json=product_data)
    assert create_product_response.status_code == 200
    created_product = create_product_response.json()
    product_id = created_product["id"]

    user_data = {
        "email": "testuser@example.com",
        "password": "testpassword",
        "companyName": "Test Company",
        "country": "Test Country",
        "city": "Test City"
    }
    
    create_user_response = client.post("/users", json=user_data)
    assert create_user_response.status_code == 200
    created_user = create_user_response.json()
    user_id = created_user["id"]

    transaction_data = {
        "user_id": user_id,
        "product_id": product_id,
        "date": datetime.now().isoformat(),
        "quantity": 10,
        "total_price": 1000,
        "type": "purchase"
    }
    
    create_transaction_response = client.post("/transactions", json=transaction_data)
    assert create_transaction_response.status_code == 200
    created_transaction = create_transaction_response.json()

    assert created_transaction["user_id"] == transaction_data["user_id"]
    assert created_transaction["product_id"] == transaction_data["product_id"]
    assert created_transaction["quantity"] == transaction_data["quantity"]
    assert created_transaction["total_price"] == transaction_data["total_price"]
    assert created_transaction["type"] == transaction_data["type"]

    get_transactions_response = client.get("/transactions")
    assert get_transactions_response.status_code == 200
    transactions = get_transactions_response.json()

    assert any(t["id"] == created_transaction["id"] for t in transactions)

def test_user_registration_and_login():
    user_data = {
        "email": "testuser@example.com",
        "password": "testpassword",
        "companyName": "Test Company",
        "country": "Test Country",
        "city": "Test City"
    }
    
    create_user_response = client.post("/users", json=user_data)
    assert create_user_response.status_code == 200

    login_data = {
        "email": user_data["email"],
        "password": user_data["password"]
    }
    
    login_response = client.post("/login", json=login_data)
    assert login_response.status_code == 200
    assert login_response.json() == {"message": "Login successful"}
