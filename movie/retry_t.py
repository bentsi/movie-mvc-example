from uuid import uuid4
import json
import yaml
import xml.etree.ElementTree as ET
import random
import io
import time


class NothingToRetrieveException(Exception):
    pass


class ProductNotFoundException(Exception):
    pass


class retry:
    def __init__(self, n, interval, allowed_exceptions, verbose):
        self.n = n
        self.interval = interval
        self.allowed_exceptions = allowed_exceptions
        self.verbose = verbose

    def __call__(self, func):
        def inner(*args, **kwargs):
            error = True
            quantity = 1
            func_result = None
            while error and quantity != (self.n + 1):
                try:
                    func_result = func(*args, **kwargs)
                    error = False
                except self.allowed_exceptions:
                    if self.verbose:
                        print(f"Retrying <{func.__name__}>. Try {quantity}")
                    time.sleep(self.interval)
                    error = True
                    quantity += 1
            return func_result

        return inner


class Product:
    PRODUCT_LIST_NAMES = ["milk", "meat", "egg", "banana", "apple", "orange", "beer", "juice", "pineapple", ]
    PRODUCTS = []

    def __init__(self, name=random.choice(PRODUCT_LIST_NAMES), identifier=str(uuid4())):
        self.name = name
        self.identifier = identifier
        Product.PRODUCTS.append(self)

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls):
        return json.loads(Product.to_json(Product.PRODUCTS[-1]))

    def to_yaml(self):
        file = io.StringIO()
        yaml.dump(data=repr(self), stream=file)
        file.seek(0)
        return file.read()

    def __repr__(self):


    @classmethod
    def from_yaml(cls):
        file = io.StringIO(str(Product.PRODUCTS[-1]))
        # res = yaml.dump(file)
        # return yaml.load()

    def to_xml(self):
        product = ET.Element("product")
        name = ET.SubElement(product, "name")
        name.text = self.name
        identifier = ET.SubElement(product, "identifier")
        identifier.text = self.identifier
        return product

    @classmethod
    def from_xml(cls):
        result = ET.tostring(Product.to_xml(Product.PRODUCTS[-1]))
        return result


@retry(n=2, interval=1, allowed_exceptions=ProductNotFoundException, verbose=True)
def retrieve_product():
    if random.choice([True, False]):
        try:
            raise NothingToRetrieveException()
        except NothingToRetrieveException:
            get_product(ex=True, format="", data=None)
    else:
        type_serilization = random.choice(["xml", "json"])
        if type_serilization == "yaml":
            result = Product.from_yaml()
        elif type_serilization == "json":
            result = Product.from_json()
        else:
            result = Product.from_xml()
        return get_product(ex=False, format=type_serilization, data=result)


def get_product(ex, format, data):
    if ex:
        raise ProductNotFoundException()
    if format == "xml":
        tree = ET.fromstring(data)
        name = tree.find("name").text
        identifier = tree.find("identifier").text
        return Product(name=name, identifier=identifier)
    if format == "json":
        name = data["name"]
        identifier = data["identifier"]
        return Product(name=name, identifier=identifier)


if __name__ == '__main__':
    pr1 = Product()
    retrieve_product()
    # pr1.to_xml()
    # print(pr1.to_yaml())
    # print(Product.from_yaml())
    # print(retrieve_product())
    # pr1.to_json()
    # get_product(ex=True)
    # print(retrieve_product())
