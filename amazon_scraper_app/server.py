from flask import Flask
from flask_restful import Api

from amazon_scraper_app.models.api_resource_models import AmazonProductListResource, AmazonProductResource, \
    AmazonProductPriceResource

# import this to initialise additional routes
from amazon_scraper_app.additional_routes import get_price_for_product


class ScraperApp():
    def __init__(self, flask_app, db, create_tables=False):
        # Initialize Flask amazon_scraper_app
        self.app = flask_app
        # self.app.config.from_object(DevelopmentConfig)
        self.db = db
        self.create_tables = create_tables

        # Initialize Api handler
        self.api = Api(self.app)

        # Initialize DB
        self._init_db()

        # Initialize Api handler amazon_scraper_app endpoints
        self.api.add_resource(AmazonProductListResource, '/products')  # Route_1
        self.api.add_resource(AmazonProductResource, '/products/<string:product_id>')  # Route_3
        self.api.add_resource(AmazonProductPriceResource, '/prices/<string:product_id>')

    def run(self, **kwargs):
        self.app.run(host=kwargs.get('host', 'localhost'),
                     port=kwargs.get('port', 5000),
                     debug=kwargs.get('debug', False))

    def _init_db(self):
        self.db.init_app(self.app)
        if self.create_tables:
            with self.app.app_context():
                self.db.create_all()
        self.app.logger.debug('Initialised database')
