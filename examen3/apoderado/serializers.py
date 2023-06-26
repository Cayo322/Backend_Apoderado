from rest_framework import serializers
from .models import TblParentesco, TblApoderado

class ParentescoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblParentesco
        fields = '__all__'
        
class ApoderadoSerializer(serializers.ModelSerializer):
    parentesco_nombre = serializers.ReadOnlyField(source='parentesco.parentesco_nombre')

    class Meta:
        model = TblApoderado
        fields = '__all__'
