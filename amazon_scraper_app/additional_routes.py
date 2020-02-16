from config.config import ROOT_PATH
import markdown
from amazon_scraper_app import my_app
from amazon_scraper_app.models.database_models import db, AmazonProductPriceDBModel
from amazon_scraper_app.utilities.database_utilities import get_products
from amazon_scraper_app.utilities.server_operational_methods import get_price_from_amazon_url
from amazon_scraper_app.customExceptions import PriceNotFoundException
import concurrent
import concurrent.futures
from amazon_scraper_app.models.server_utilities import uuid_generator
import os


def get_price_for_product(product):
    # 1. extract product url
    product_url = product.get("url")
    # 2. get price using selector lib
    _, product_price = get_price_from_amazon_url(product_url)
    # 3. return price in euros
    if product_price:
        return product, product_price
    else:
        raise PriceNotFoundException(f'Price not found for product {product.name} with url: {product_url}')


@my_app.route("/")
def index():
    """Present some documentation"""
    # Open the README file
    with open(os.path.join(ROOT_PATH, 'README.md'), 'r') as markdown_file:
        # Read the content of the file
        content = markdown_file.read()
        # Convert to HTML
        return markdown.markdown(content)
#
#
# @my_app.route("/update_prices", methods=['GET'])
# def update_prices():
#     pass
#     products = get_products()
#     worker_threads_list = []
#     product_with_prices = []
#     with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#         for product in products:
#             worker_thread = executor.submit(get_price_for_product, product.url)
#             worker_threads_list.append(worker_thread)
#
#         for future in concurrent.futures.as_completed(worker_threads_list):
#             product, product_price = future.result()
#             product.update({'price': product_price})
#             product_with_prices.append(product)
#
#     for product_price in product_with_prices:
#         price_db_obj = AmazonProductPriceDBModel(product_id=product_price.get('id'), price=product_price.get('price'))
#         db.session.add(price_db_obj)
#
#     db.session.commit()

@my_app.route("/update_prices", methods=['GET'])
def update_prices():
    products = get_products()
    worker_threads_list = []
    product_with_prices = []

    if products:
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            for product in products:
                worker_thread = executor.submit(get_price_for_product, product)
                worker_threads_list.append(worker_thread)

            for future in concurrent.futures.as_completed(worker_threads_list):
                product, product_price = future.result()
                product.update({'price': product_price})
                product_with_prices.append(product)

        for product_price in product_with_prices:
            price_db_obj = AmazonProductPriceDBModel(id=uuid_generator(),product_id=product_price.get('id'), price=product_price.get('price'))
            db.session.add(price_db_obj)

        db.session.commit()
        return "", 204

    else:
        return "", 204
