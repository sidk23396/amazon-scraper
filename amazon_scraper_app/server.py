from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from amazon_scraper_app.api_resource_models import (AmazonProductResource, AmazonProductListResource,
                                                    AmazonProductPriceResource)
from config.config import DevelopmentConfig


class ScraperApp():
    def __init__(self):
        # Initialize Flask amazon_scraper_app
        self.app = Flask(__name__)
        # Initialize Api handler
        self.api = Api(self.app)
        # Initialize DB
        self.app.config.from_object(DevelopmentConfig)
        self.db = SQLAlchemy(self.app)
        # self.db.get_tables_for_bind()
        # Initialize Api handler amazon_scraper_app endpoints
        self.api.add_resource(AmazonProductListResource, '/products')  # Route_1
        self.api.add_resource(AmazonProductResource, '/products/<product_id>')  # Route_3
        self.api.add_resource(AmazonProductPriceResource, '/prices/<product_id>')

    def run(self, **kwargs):
        self.app.run(host='localhost', port=5000, debug=True)

    def init_db(self):
        self.db.create_all()
        self.app.logger.debug('Initialised database')


my_app = ScraperApp()
