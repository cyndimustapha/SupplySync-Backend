from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.Products import Product
from models.Transactions import Transaction
from models.Users import User
from validation_models import ProductModel, TransactionModel, UserModel, LoginModel

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

@app.get('/transactions')
def get_transactions():
    transactions = Transaction.find_all()
    return transactions

@app.post('/transactions')
def create_transaction(transaction: TransactionModel):
    new_transaction = Transaction(user_id=transaction.user_id, product_id=transaction.product_id, date=transaction.date, quantity=transaction.quantity, total_price=transaction.total_price, type=transaction.type)
    new_transaction.save()
    return new_transaction

@app.post('/users')
def create_user(user: UserModel):
    new_user = User(email=user.email, password=user.password, companyName=user.companyName, country=user.country, city=user.city)
    new_user.save()
    return new_user

@app.post('/login')
def login_user(user: LoginModel):
    user = User.find_by_email_and_password(user.email, user.password)
    if user:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=400, detail="Invalid email or password")