from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.Products import Product
from models.Purchases import Purchase
from models.Sales import Sale
from models.Transactions import Transaction
from models.Users import User
from validation_models import ProductModel, PurchaseModel, SaleModel, TransactionModel, UserModel

# Create the FastAPI app
app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/products')
def get_products():
    products = Product.find_all()
    return products

@app.post('/products')
def create_product(product: ProductModel):
    new_product = Product(name=product.name, sku=product.sku, price=product.price, stock=product.stock)
    new_product.save()
    return new_product

@app.post('/purchases')
def create_purchase(purchase: PurchaseModel):
    new_purchase = Purchase(user_id=purchase.user_id, product_id=purchase.product_id, date=purchase.date, quantity=purchase.quantity, total_price=purchase.total_price)
    new_purchase.save()
    return new_purchase

@app.post('/sales')
def create_sale(sale: SaleModel):
    new_sale = Sale(user_id=sale.user_id, product_id=sale.product_id, date=sale.date, quantity=sale.quantity, total_price=sale.total_price)
    new_sale.save()
    return new_sale

@app.post('/transactions')
def create_transaction(transaction: TransactionModel):
    new_transaction = Transaction(user_id=transaction.user_id, product_id=transaction.product_id, date=transaction.date, quantity=transaction.quantity, total_price=transaction.total_price, type=transaction.type)
    new_transaction.save()
    return new_transaction

@app.post('/users')
def create_user(user: UserModel):
    new_user = User(email=user.email, password=user.password, company_name=user.company_name, country=user.country, city=user.city)
    new_user.save()
    return new_user
