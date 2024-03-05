from .APIresponseView import APIResponseView
from .base import base



class patch_product(base, APIResponseView):
    def patch(self, request, id):
        return self.api_response(self.send_request, f"products/{id}", method="patch", data=request.data)

class patch_category(base, APIResponseView):
    def patch(self, request, category):
        return self.api_response(self.send_request, f"products/category/{category}", method="patch", data=request.data)



class patch_cart(base, APIResponseView):
    def patch(self, request, id):
        return self.api_response(self.send_request, f"carts/{id}", method="patch", data=request.data)

class patch_user(base, APIResponseView):
    def patch(self, request, id):
        return self.api_response(self.send_request, f"users/{id}", method="patch", data=request.data)

class patch_order(base, APIResponseView):
    def patch(self, request, id):
        return self.api_response(self.send_request, f"orders/{id}", method="patch", data=request.data)

