from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Product, Lesson, UserBalance
from .serializers import ProductSerializer, LessonSerializer, UserBalanceSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'])
    def available(self, request):
        available_products = self.queryset.filter(userbalance__balance__gt=0)
        serializer = self.get_serializer(available_products, many=True)
        return Response(serializer.data)

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class UserBalanceViewSet(viewsets.ModelViewSet):
    queryset = UserBalance.objects.all()
    serializer_class = UserBalanceSerializer

@action(detail=False, methods=['post'])
def pay(self, request):
    user = request.user
    product_id = request.data.get('product_id')
    product = Product.objects.get(id=product_id)
    user_balance = UserBalance.objects.get(user=user)

    if user_balance.balance >= product.price:
        user_balance.balance -= product.price
        user_balance.save()
        # Course access logic
        return Response({'status': 'Access Granted'})
    else:
        return Response({'status': 'Cannot access the course'}, status=400)