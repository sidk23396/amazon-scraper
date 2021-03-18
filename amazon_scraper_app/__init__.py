from flask import Flask

from amazon_scraper_app.models.api_resource_models import AmazonProductListResource, AmazonProductResource, \
    AmazonProductPriceResource
from config.config import DevelopmentConfig

my_app = Flask(__name__)
my_app.config.from_object(DevelopmentConfig)


