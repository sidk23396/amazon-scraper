from flask_restful import Resource, abort, reqparse

from amazon_scraper_app.models.server_utilities import AmazonProduct
from amazon_scraper_app.models.server_utilities import uuid_generator
from amazon_scraper_app.utilities.database_utilities import (get_products, get_product_by_id, delete_product_by_id,
                                                             add_product_to_db, get_prices_of_product)

PRODUCTS = [
        {'name': 'sony_wh1000xm3_headphones',
         'url': 'https://www.amazon.co.uk/Sony-WH-1000XM3-Wireless-Cancelling-Headphones-Black/dp/B07GDR2LYK/ref=sr_1_2?crid=3O5WK212UF75V&keywords=wh1000xm3&qid=1580595084&sprefix=wh1000%2Caps%2C150&sr=8-2',
         'id': 'fiasbfnksadnfisadn1293r1y24bjkda'},
        {'name': 'samsung_note10plus',
         'url': 'https://www.amazon.co.uk/Samsung-Dual-SIM-SM-N975F-SIM-Free-Smartphone/dp/B07W6XFX64/ref=sr_1_2?keywords=note+10+plus&qid=1580595141&sr=8-2',
         'id': 'fiasbfnksadnfisadn1293r1y24bjkda'}
    ]


parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('url')
parser.add_argument('id')


def product_in_list(product_id):
    for product in PRODUCTS:
        if product['id'] == product_id:
            return product
    return None


# Handles requests for one particular product
class AmazonProductResource(Resource):
    # return price data from db for product
    def get(self, product_id):
        product_found, product = get_product_by_id(id=product_id)
        # PRODUCT = product_in_list(product_id)
        if product_found:
            return {'data': {'product': product.__dict__}}, 200
        else:
            return {'data': {'message': f"Product with id {product_id} not found"}}, 404

        abort(404)

    def delete(self, product_id):
        product_found, product = get_product_by_id(id=product_id)
        if product_found:
            delete_product_by_id(product_id)
            return '', 204
        abort(404)


    # def patch(self, product_id):
    #     args = parser.parse_args()
    #     product_name = args.name
    #     product_url = args.url
    #
    #     OLD_PRODUCT = product_in_list(product_id)
    #
    #     if OLD_PRODUCT:
    #         PRODUCTS.remove(OLD_PRODUCT)
    #         print(f'removed old_product: {OLD_PRODUCT}')
    #         print(PRODUCTS)
    #         NEW_PRODUCT = {}
    #         NEW_PRODUCT['name'] = product_name if product_name else OLD_PRODUCT['name']
    #         NEW_PRODUCT['url'] = product_url if product_url else OLD_PRODUCT['url']
    #         NEW_PRODUCT['id'] = OLD_PRODUCT['id']
    #         PRODUCTS.append(NEW_PRODUCT)
    #
    #         return {'product': NEW_PRODUCT}, 200
    #
    #     abort(404)


class AmazonProductListResource(Resource):
    def get(self):
        products = get_products()
        return {'data': {'products': products}}, 200

    def post(self):
        args = parser.parse_args()
        product_id = uuid_generator()
        product_name = args.name
        product_url = args.url
        product = AmazonProduct(product_id, product_name, product_url)
        add_product_to_db(product.__dict__)
        return {'data': {'product': product.__dict__}}, 201


class AmazonProductPriceResource(Resource):
    def get(self, product_id):
        prices = get_prices_of_product(product_id)

        if prices:
            prices_dates_for_product = [{'price': float(f"{pr.price:.2f}"), 'date': str(pr.date)} for pr in prices]
            return {'data': prices_dates_for_product}, 200
            
        abort(404)

    # def delete(self, product_id):
    #     pass