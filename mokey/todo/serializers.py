# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from .models import Todo, user_data,product_data, user_cart

# create a serializer class
class TodoSerializer(serializers.ModelSerializer):

    # create a meta class
    class Meta:
        model = Todo
        fields = ('id', 'title','description','completed')

# create a serializer class
class UserSerializer(serializers.ModelSerializer):

    # create a meta class
    class Meta:
        model = user_data
        fields = ('id', 'user_id','email','name','lname','address')

#Product data
class ProductSerializer(serializers.ModelSerializer):

    # create a meta class
    class Meta:
        model = product_data
        fields = ('id', 'product_id','quantity','product_description','quantity','price','product_name')

#Product data
class CartSerializer(serializers.ModelSerializer):

    # create a meta class
    class Meta:
        model = user_cart
        fields = ('id', 'product_id','user_id','quantity')
        