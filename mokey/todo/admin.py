from django.contrib import admin

# Register your models here.
# import the model Todo
from .models import Todo, user_data, product_data,user_cart

# create a class for the admin-model integration
class TodoAdmin(admin.ModelAdmin):

    # add the fields of the model here
    list_display = ("title","description","completed")

class UserAdmin(admin.ModelAdmin):

    # add the fields of the model here
    list_display = ("user_id","email","name","lname","address")

class ProductAdmin(admin.ModelAdmin):

    # add the fields of the model here
    list_display = ("product_id","product_name","product_description","quantity","price")


class CartAdmin(admin.ModelAdmin):

    # add the fields of the model here
    list_display = ("user_id","product_id","quantity")

admin.site.register(Todo,TodoAdmin)
admin.site.register(product_data,ProductAdmin)
admin.site.register(user_data,UserAdmin)
admin.site.register(user_cart,CartAdmin)