from rest_framework import viewsets, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomUserSerializer
