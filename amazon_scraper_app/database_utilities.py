# db_connect = create_engine(f'sqlite3:///{DB_NAME}')
from amazon_scraper_app.database_models import AmazonProduct, AmazonProductPrice
products_table = AmazonProduct.__tablename__
product_price_table = AmazonProductPrice.__tablename__

from amazon_scraper_app.server import my_app

db = my_app.db


def get_prodcts():
    products = AmazonProduct.query.all()
    print(type(products[0]))
    return [{'id': product.get('id'), 'name': product.get('name'), 'url': product.get('url')} for product in products]
