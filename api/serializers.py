from rest_framework import serializers
from .models import Partida

class PartidaSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Partida.
    """
    class Meta:
        model = Partida
        fields = '__all__'  # Inclui todos os campos do modelo na API
