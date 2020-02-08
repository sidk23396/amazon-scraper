from amazon_scraper_app.server import my_app
from datetime import datetime

db = my_app.db


class AmazonProduct(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.String(20), unique=True, primary_key=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    url = db.Column(db.String(150), unique=True, nullable=False)
    prices = db.relationship('AmazonProductPrice', backref='product', lazy=True)

    def __repr__(self):
        return '<Product %r>' % self.name

    def _price_list(self):
        return [p for p in self.prices.price]


class AmazonProductPrice(db.Model):
    __tablename__ = 'price'
    id = db.Column(db.String(20), primary_key=True, nullable=False)
    product_id = db.Column(db.String(20), db.ForeignKey('product.id'), nullable=False)
    # product_id = db.Column(db.String, db.ForeignKey('product.id'))
    # product = db.relationship("AmazonProduct", backref=db.backref("product", uselist=False))
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<ProductPrice %r %r>' % (self.id, self.price)


# if __name__ == '__main__':
#     amazon_scraper_app.run(port=int(7000), host='localhost', debug=True)