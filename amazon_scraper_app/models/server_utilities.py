import uuid


def uuid_generator():
    return uuid.uuid4().hex


class AmazonProduct:
    def __init__(self, product_id, name, url):
        self.id = product_id
        self.name = name
        self.url = url

    @staticmethod
    def _load_from_db_object(db_object):
        id = db_object.id
        name = db_object.name
        url = db_object.url

        return AmazonProduct(id, name, url)
