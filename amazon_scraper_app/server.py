from flask import Flask
from flask_restful import Api

from amazon_scraper_app.models.api_resource_models import AmazonProductListResource, AmazonProductResource, \
    AmazonProductPriceResource
from config.config import DevelopmentConfig

# import this to initialise additional routes
from amazon_scraper_app.additional_routes import get_price_for_product


class ScraperApp():
    def __init__(self, flask_app, db):
        # Initialize Flask amazon_scraper_app
        self.app = flask_app
        # Initialize Api handler
        self.api = Api(self.app)
        # Initialize DB
        self.app.config.from_object(DevelopmentConfig)
        self.db = db
        # self.db.get_tables_for_bind()
        # Initialize Api handler amazon_scraper_app endpoints
        self.api.add_resource(AmazonProductListResource, '/products')  # Route_1
        self.api.add_resource(AmazonProductResource, '/products/<string:product_id>')  # Route_3
        self.api.add_resource(AmazonProductPriceResource, '/prices/<string:product_id>')

    def run(self):
        self.app.run(host='localhost', port=5000, debug=True)

    def init_db(self):
        self.db.create_all()
        self.app.logger.debug('Initialised database')

    def create_app(self):
        if hasattr(self, 'app') and self.app:
            return self.app
        else:
            self.app = Flask(__name__)
            return self.app
