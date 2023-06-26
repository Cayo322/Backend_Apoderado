from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .models import TblApoderado,TblParentesco
from .serializers import ApoderadoSerializer, ParentescoSerializer

class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)
    
class ParentescoViewSet(viewsets.ModelViewSet):
    queryset = TblParentesco.objects.all()
    serializer_class = ParentescoSerializer

class ApoderadoViewSet(viewsets.ModelViewSet):
    queryset = TblApoderado.objects.all()
    serializer_class = ApoderadoSerializer

