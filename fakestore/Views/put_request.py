from .base import base
from .APIresponseView import APIResponseView

class put_product(base, APIResponseView):
    def put(self, request, id):
        return self.api_response(self.send_request, f"products/{id}", method="put", data=request.data)

class put_category(base, APIResponseView):
    def put(self, request, category):
        return self.api_response(self.send_request, f"products/category/{category}", method="put", data=request.data)

class put_cart(base, APIResponseView):
    def put(self, request, id):
        return self.api_response(self.send_request, f"carts/{id}", method="put", data=request.data)

class put_user(base, APIResponseView):
    def put(self, request, id):
        return self.api_response(self.send_request, f"users/{id}", method="put", data=request.data)

class put_order(base, APIResponseView):
    def put(self, request, id):
        return self.api_response(self.send_request, f"orders/{id}", method="put", data=request.data)


