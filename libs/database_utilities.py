from config.settings import DB_NAME
from sqlalchemy import create_engine
import uuid

db_connect = create_engine(f'sqlite3:///{DB_NAME}')
products_table = "products"
product_price_table = "product_name"

class Database:
    pass

class AmazonDatabaseProduct:
    def __init__(self):
        conn = db_connect.connect()

    def create_product_table(self):
        pass


    def add_product_to_db(self, product_name, product_url):
        product_id = str(uuid.uuid4().hex)


