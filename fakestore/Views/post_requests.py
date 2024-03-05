from .APIresponseView import APIResponseView
from .base import base

class add_Product(base, APIResponseView):
    def post(self, request):
        return self.api_response(self.send_request, "products", method="post", data=request.data)
class add_Category(base, APIResponseView):
    def post(self, request):
        return self.api_response(self.send_request, "products/categories", method="post", data=request.data)

class add_Cart(base, APIResponseView):
    def post(self, request):
        return self.api_response(self.send_request, "carts", method="post", data=request.data)

class add_User(base, APIResponseView):
    def post(self, request):
        return self.api_response(self.send_request, "users", method="post", data=request.data)

class add_Order(base, APIResponseView):
    def post(self, request):
        return self.api_response(self.send_request, "orders", method="post", data=request.data)


