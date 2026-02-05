from django.shortcuts import render
from rest_framework.response import Response # Tipo de Respostas
from rest_framework import status # Não pode importar junto com a 2, porque status não está em Response
from .models import Usuario, Imovel, Contrato, Pagamento
from .serializers import * # Importa tudo com o *
from rest_framework.decorators import api_view
# Um decorator @ é um decorador, o método abaixo dele vai obedece-lo
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Chamando Método com Parâmetro
@api_view(['GET', 'POST'])
def listar_usuarios(request):
    if request.method == 'GET':
        # query - procura, set - definir
        queryset = Usuario.objects.all()
        serializers = UsuarioSerializer(queryset, many=True) # many - vai ter vários usuários
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = UsuarioSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)

# Outra forma de fazer, mas com a classe

# Usuário
class UsuarioView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Imóvel
class ImovelView(ListCreateAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

class ImovelDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

# Contrato
class ContratoView(ListCreateAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class ContratoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    
# Pagamento
class PagamentoView(ListCreateAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

class PagamentoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
