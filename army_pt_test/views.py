from rest_framework import generics
from .models import Cadet
from .serializers import CadetSerializer

# Create your views here.

# api/cadet
# index, post


class CadetList(generics.ListCreateAPIView):
    queryset = Cadet.objects.all()
    serializer_class = CadetSerializer

# api/cadet/id
# show, put, delete


class CadetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cadet.objects.all()
    serializer_class = CadetSerializer
