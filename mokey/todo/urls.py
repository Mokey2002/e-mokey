
from django.urls import path 
from todo import views 
  
urlpatterns = [ 
    path('todo/', 
         views.TodoView, 
         name = 'todo-list'),
        path('login/', 
         views.UserView, 
         name = 'login-user'),
        path('product/', 
         views.ProductView, 
         name = 'product-list'),
        path('cart/', 
         views.CartView, 
         name = 'cart-list'),
        path('product_id/<int:id>/',views.ProductbyIdView,
         name='get-product-by-id'),
        path('delete_cart_product_id/<int:id>/',views.DeleteCartItembyIdView,
         name='delete-cart-product-by-id')


] 
