from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from models.Products import Product
from models.Transactions import Transaction
from models.Users import User
from validation_models import ProductModel, TransactionModel, UserModel, LoginModel

DATABASE_FILE = "db.sqlite"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_file():
    return DATABASE_FILE

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/products')
def get_products(db_file: str = Depends(get_db_file)):
    products = Product.find_all(db_file)
    return products

@app.post('/products')
def create_product(product: ProductModel, db_file: str = Depends(get_db_file)):
    new_product = Product(name=product.name, sku=product.sku, description=product.description, quantity=product.quantity, price=product.price, supplier=product.supplier)
    new_product.save(db_file)
    return new_product

@app.get('/low_stock')
def get_low_stock_products(threshold: int, db_file: str = Depends(get_db_file)):
    low_stock_products = Product.find_low_stock(threshold, db_file)
    return low_stock_products

@app.get('/transactions')
def get_transactions(db_file: str = Depends(get_db_file)):
    transactions = Transaction.find_all(db_file)
    return transactions

@app.post('/transactions')
def create_transaction(transaction: TransactionModel, db_file: str = Depends(get_db_file)):
    new_transaction = Transaction(
        user_id=transaction.user_id,
        product_id=transaction.product_id,
        date=transaction.date,
        quantity=transaction.quantity,
        total_price=transaction.total_price,
        type=transaction.type
    )
    new_transaction.save(db_file)
    return new_transaction

@app.post('/users')
def create_user(user: UserModel, db_file: str = Depends(get_db_file)):
    new_user = User(email=user.email, password=user.password, companyName=user.companyName, country=user.country, city=user.city)
    new_user.save(db_file)
    return new_user

@app.post('/login')
def login_user(user: LoginModel, db_file: str = Depends(get_db_file)):
    user = User.find_by_email_and_password(user.email, user.password, db_file)
    if user:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=400, detail="Invalid email or password")
