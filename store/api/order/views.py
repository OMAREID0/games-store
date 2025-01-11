from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem
from api.product.models import Product
from django.http import JsonResponse
from django.contrib.auth import get_user_model


class CreateOrderView(APIView):
    serializer_class = OrderItemSerializer
    def validate_user_session(self, id, token):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(pk=id)
            if user.session_token == token:
                return True
            else:
                return False
        except UserModel.DoesNotExist:
            return False

    def post(self, request):
        user = request.user
        id = user.id
        token = request.COOKIES.get('jwt')
        print(token, id)
        if not self.validate_user_session(id, token):
            return JsonResponse({'error':'Please login again', 'code':'1'})
        query = Order.objects.get(user=id)
        if query.status == 'PENDING_STATE':
            quantity = request.data.get("quantity", 1)
            order_items = OrderItem(order=query, product=Product.name, quantity=quantity, total=(Product.price * quantity))
            order_items.save()
        else:
            order_detail = Order(user=user)
            order_detail.save()
            quantity = request.data.get("quantity", 1)
            order_items = OrderItem(order=order_detail, product=Product.name, quantity=quantity, total=(Product.price * quantity))
            order_items.save()
        return JsonResponse({'success':True, 'error':False, 'msg':'Order placed successfully'})


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all().order_by('id')
    serializer_class = OrderItemSerializer














