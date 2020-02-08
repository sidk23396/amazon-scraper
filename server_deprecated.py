from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
from sqlalchemy import create_engine
from config.config import SERVER_HOST, SERVER_PORT, SERVER_DEBUG_MODE
from amazon_scraper_app.server_utilities import uuid_generator

db_connect = create_engine('sqlite:///amazon_scraper.db')
app = Flask(__name__)
api = Api(app)

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
        PRODUCT = product_in_list(product_id)
        if PRODUCT:
            return {'product': PRODUCT}, 200

        abort(404)

    def delete(self, product_id):
        PRODUCT = product_in_list(product_id)
        if PRODUCT:
            print('in delete product.. if')
            PRODUCTS.remove(PRODUCT)
            return '', 204
        abort(404)

    def patch(self, product_id):
        args = parser.parse_args()
        product_name = args.name
        product_url = args.url

        OLD_PRODUCT = product_in_list(product_id)

        if OLD_PRODUCT:
            PRODUCTS.remove(OLD_PRODUCT)
            print(f'removed old_product: {OLD_PRODUCT}')
            print(PRODUCTS)
            NEW_PRODUCT = {}
            NEW_PRODUCT['name'] = product_name if product_name else OLD_PRODUCT['name']
            NEW_PRODUCT['url'] = product_url if product_url else OLD_PRODUCT['url']
            NEW_PRODUCT['id'] = OLD_PRODUCT['id']
            PRODUCTS.append(NEW_PRODUCT)

            return {'product': NEW_PRODUCT}, 200
        
        abort(404)


class AmazonProductListResource(Resource):
    def get(self):
        return {'products': PRODUCTS}, 200

    # def delete(self):
    #     PRODUCTS = []
    #     return '', 204

    def post(self):
        args = parser.parse_args()
        product_id = uuid_generator()
        product_name = args.name
        product_url = args.url
        PRODUCT = {'id': product_id, 'name': product_name, 'url': product_url}
        PRODUCTS.append(PRODUCT)
        return {'product': PRODUCT}, 201

class AmazonProductPriceResource(Resource):
    def get(self, product_id):
        pass

# class Employees(Resource):
#     def get(self):
#         conn = db_connect.connect() # connect to database
#         query = conn.execute("select * from employees") # This line performs query and returns json result
#         return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

# class Tracks(Resource):
#     def get(self):
#         conn = db_connect.connect()
#         query = conn.execute("select trackid, name, composer, unitprice from tracks;")
#         print(type(query))
#         result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
#         return jsonify(result)

# class Employees_Name(Resource):
#     def get(self, employee_id):
#         conn = db_connect.connect()
#         query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
#         result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
#         return jsonify(result)
        

api.add_resource(AmazonProductListResource, '/products') # Route_1
api.add_resource(AmazonProductResource, '/products/<product_id>') # Route_3
api.add_resource(AmazonProductPriceResource, '/prices/<product_id>')
# api.add_resource(Tracks, '/tracks') # Route_2
# api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
     app.run(port=int(SERVER_PORT),host=SERVER_HOST, debug=SERVER_DEBUG_MODE)