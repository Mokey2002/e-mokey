from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets

# import the TodoSerializer from the serializer file
from .serializers import TodoSerializer,UserSerializer,ProductSerializer,CartSerializer

# import the Todo model from the models file
from .models import Todo, user_data, product_data,user_cart
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 

from django.http import HttpResponse, JsonResponse

# create a class for the Todo model viewsets
#class TodoView(viewsets.ModelViewSet):

    # create a serializer class and 
    # assign it to the TodoSerializer class
    #serializer_class = TodoSerializer

    # define a variable and populate it 
    # with the Todo list objects
    #queryset = Todo.objects.all()

    #@action(detail=False, methods=['post'])
    #def add_todo(self, request):
    
    #    user = self.get_object()
    #    response = view(request, pk=1)
    #    print(request)
    #    return Response({'status': 'blog post liked'})

@api_view(['GET', 'POST'])
def TodoView(request):
    if request.method == 'GET':
        tutorials = Todo.objects.all()
        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = TodoSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TodoSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse({'message':'success'}, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def UserView(request):
    if request.method == 'GET':
        tutorials = user_data.objects.all()
        title = request.query_params.get('user_id', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = UserSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = UserSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse({'message':'success'}, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
def ProductView(request):
    if request.method == 'GET':
        products = product_data.objects.all()
        productid = request.query_params.get('user_id', None)
        #if title is not None:
        #    tutorials = tutorials.filter(title__icontains=title)
        
        product_serializer = ProductSerializer(products, many=True)
        return JsonResponse(product_serializer.data, safe=False)
    
    elif request.method == 'POST':
        new_product = JSONParser().parse(request)
        product_serializer = ProductSerializer(data=new_product)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse({'message':'success'}, status=status.HTTP_201_CREATED) 
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
def CartView(request):
    if request.method == 'GET':
        products = user_cart.objects.all()
        productid = request.query_params.get('user_id', None)
        #if title is not None:
        #    tutorials = tutorials.filter(title__icontains=title)
        
        cart_serializer = CartSerializer(products, many=True)
        return JsonResponse(cart_serializer.data, safe=False)
    
    elif request.method == 'POST':
        new_item = JSONParser().parse(request)
        cart_serializer = CartSerializer(data=new_item)
        if cart_serializer.is_valid():
            cart_serializer.save()
            return JsonResponse({'message':'success'}, status=status.HTTP_201_CREATED) 
        return JsonResponse(cart_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def ProductbyIdView(request,id):
    print(id)
    
    product = product_data.objects.filter(product_id=id) 
     
    productbyId_serializer = ProductSerializer(product, many=True)
    
    return JsonResponse(productbyId_serializer.data, safe=False)
    
    #if request.method == 'GET':
    #    products = user_cart.objects.all()
    #    print(request)