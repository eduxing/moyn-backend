from rest_framework import viewsets
from .models import MoynUser
from .serializers import MoynUserSerializer

class MoynUserViewSet(viewsets.ModelViewSet):
    queryset = MoynUser.objects.all()
    serializer_class = MoynUserSerializer
