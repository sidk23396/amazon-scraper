from amazon_scraper_app.customExceptions import DBOperationException
from amazon_scraper_app.models.database_models import AmazonProductDBModel, AmazonProductPriceDBModel
from amazon_scraper_app.models.database_models import db
from amazon_scraper_app.models.server_utilities import AmazonProduct


def get_products():
    products = AmazonProductDBModel.query.all()
    return [AmazonProduct._load_from_db_object(product).__dict__ for product in products]


def get_product_by_id(id):
    product = AmazonProductDBModel.query.filter_by(id=id).first()
    if product:
        return True, AmazonProduct._load_from_db_object(product)
    return False, None


def add_product_to_db(product):
    if all([product.get("id"), product.get("name"), product.get("url")]):
        new_product = AmazonProductDBModel(id=product.get("id"), name=product.get("name"), url=product.get("url"))
        db.session.add(new_product)
        db.session.commit()
    else:
        raise DBOperationException("Product does not have required keys.")


def delete_product_by_id(product_id):
    # product_found, product_to_delete = get_product_by_id(id=product_id)
    # if product_found:
    AmazonProductDBModel.query.filter_by(id=product_id).delete()
    db.session.commit()
    # else:
    #     print(f"Product with id {product_id} not found")


def get_prices_of_product(product_id):
    prices = AmazonProductPriceDBModel.query.filter_by(product_id=product_id).all()
    return prices if prices else None