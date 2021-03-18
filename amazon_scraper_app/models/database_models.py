from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class AmazonProductDBModel(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.String(20), unique=True, primary_key=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    url = db.Column(db.String(150), unique=True, nullable=False)
    prices = db.relationship('AmazonProductPriceDBModel', backref='product', lazy=True)

    def __repr__(self):
        return '<Product %r>' % self.name

    def _price_list(self):
        return [p for p in self.prices.price]


class AmazonProductPriceDBModel(db.Model):
    __tablename__ = 'price'
    id = db.Column(db.String(20), primary_key=True, nullable=False)
    product_id = db.Column(db.String(20), db.ForeignKey('product.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<ProductPrice %r %r>' % (self.id, self.price)
