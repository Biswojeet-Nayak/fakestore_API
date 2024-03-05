from .APIresponseView import APIResponseView
from .base import base

class del_Product(base, APIResponseView):
    def delete(self, request, id):
        return self.api_response(self.send_request, f"products/{id}")

class del_Category(base, APIResponseView):
    def delete(self, request, category):
        return self.api_response(self.send_request, f"products/category/{category}")
class del_Cart(base, APIResponseView):
    def delete(self, request, id):
        return self.api_response(self.send_request, f"carts/{id}")

class del_Order(base, APIResponseView):
    def delete(self, request, id):
        return self.api_response(self.send_request, f"orders/{id}")

class del_User(base, APIResponseView):
    def delete(self, request, id):
        return self.api_response(self.send_request, f"users/{id}")

