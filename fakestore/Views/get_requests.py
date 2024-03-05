from .APIresponseView import APIResponseView
from .base import base
from django.views import View


class get_allProducts(base, APIResponseView):
    def get(self, request):
        return self.api_response(self.send_request, "products")


class get_singleProduct(base, APIResponseView):
    def get(self, request, id):
        return self.api_response(self.send_request, f"product/{id}")


class get_Categories(base, APIResponseView):
    def get(self, request):
        return self.api_response(self.send_request, "products/categories")


class get_Category(base, APIResponseView):
    def get(self, request, category):
        return self.api_response(self.send_request, f"products/category/{category}")


class get_Carts(base, APIResponseView):
    def get(self, request):
        return self.api_response(self.send_request, "carts")


class get_singleCart(base, APIResponseView):
    def get(self, request, id):
        return self.api_response(self.send_request, f"cart/{id}")


class get_Users(base, APIResponseView):
    def get(self, request):
        return self.api_response(self.send_request, "users")


class get_singleUser(base, APIResponseView):
    def get(self, request, id):
        return self.api_response(self.send_request, f"user/{id}")


class get_Orders(base, APIResponseView):
    def get(self, request):
        return self.api_response(self.send_request, "orders")


class get_singleOrder(base, APIResponseView):
    def get(self, request, id):
        return self.api_response(self.send_request, f"order/{id}")
