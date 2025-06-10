from rest_framework.viewsets import ModelViewSet
from .models import Partida
from .serializers import PartidaSerializer

class PartidaViewSet(ModelViewSet):
    """
    ViewSet para gerenciar o modelo Partida.
    Permite criar, listar, atualizar e excluir partidas via API.
    """
    queryset = Partida.objects.all()  # Retorna todas as partidas
    serializer_class = PartidaSerializer  # Serializador associado ao modelo

