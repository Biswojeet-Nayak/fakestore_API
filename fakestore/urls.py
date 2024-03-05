from django.urls import path
from .views import get_requests as getter
from .views import post_requests as postman
from .views import patch_requests as patcher
from .views import del_request as delete
from .views import put_request as putter

urlpatterns = [
    path('products/', getter.get_allProducts.as_view(), name='get_all_products'),
    path('product/<int:id>/', getter.get_singleProduct.as_view(), name='get_single_product'),
    path('categories/', getter.get_Categories.as_view(), name='get_categories'),
    path('category/<str:category>/', getter.get_Category.as_view(), name='get_category'),
    path('carts/', getter.get_Carts.as_view(), name='get_carts'),
    path('cart/<int:id>/', getter.get_singleCart.as_view(), name='get_single_cart'),
    path('users/', getter.get_Users.as_view(), name='get_users'),
    path('user/<int:id>/', getter.get_singleUser.as_view(), name='get_single_user'),
    path('orders/', getter.get_Orders.as_view(), name='get_orders'),
    path('order/<int:id>/', getter.get_singleOrder.as_view(), name='get_single_order'),
    path('add/product/', postman.add_Product.as_view(), name='add_new_product'),
    path('add/category/', postman.add_Category.as_view(), name='add_new_category'),
    path('add/cart/', postman.add_Cart.as_view(), name='add_new_cart'),
    path('add/user/', postman.add_User.as_view(), name='add_new_user'),
    path('add/order/', postman.add_Order.as_view(), name='add_new_order'),
    path('patch/product/<int:id>/', patcher.patch_product.as_view(), name='patch_product'),
    path('patch/cart/<int:id>/', patcher.patch_cart.as_view(), name='patch_cart'),
    path('patch/user/<int:id>/', patcher.patch_user.as_view(), name='patch_user'),
    path('patch/order/<int:id>/', patcher.patch_order.as_view(), name='patch_order'),
    path('patch/category/<str:category>/', patcher.patch_category.as_view(), name='patch_category'),
    path('delete/product/<int:id>/', delete.del_Product.as_view(), name='delete_product'),
    path('delete/category/<str:category>/', delete.del_Category.as_view(), name='delete_category'),
    path('delete/cart/<int:id>/', delete.del_Cart.as_view(), name='delete_cart'),
    path('delete/user/<int:id>/', delete.del_User.as_view(), name='delete_user'),
    path('delete/order/<int:id>/', delete.del_Order.as_view(), name='delete_order'),
    path('put/product/<int:id>/', putter.put_product.as_view(), name='put_product'),
    path('put/category/<str:category>/', putter.put_category.as_view(), name='put_category'),
    path('put/cart/<int:id>/', putter.put_cart.as_view(), name='put_cart'),
    path('put/user/<int:id>/', putter.put_user.as_view(), name='put_user'),
    path('put/order/<int:id>/', putter.put_order.as_view(), name='put_order'),





]

