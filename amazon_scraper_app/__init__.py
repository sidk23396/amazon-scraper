from flask import Flask
from amazon_scraper_app.models.api_resource_models import AmazonProductListResource, AmazonProductResource, \
    AmazonProductPriceResource

my_app = Flask(__name__)
