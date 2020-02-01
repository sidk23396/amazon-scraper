import uuid


def uuid_generator():
    return uuid.uuid4().hex

class AmazonProduct:
    def __init__(self, name, url):
        self.name = name
        self.url = url

class AmazonProductList:
    def __init__(self):
        pass