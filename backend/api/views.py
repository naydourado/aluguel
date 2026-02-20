from django.shortcuts import render
from rest_framework.response import Response # Tipo de Respostas
from rest_framework import status # Não pode importar junto com a 2, porque status não está em Response
from .models import Usuario, Imovel, Contrato, Pagamento
from .serializers import * # Importa tudo com o *
from rest_framework.decorators import api_view
# Um decorator @ é um decorador, o método abaixo dele vai obedece-lo
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .filters import UsuarioFilter

#-------------- ModelsViewSet --------------
class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    # permission_classes = [IsAuthenticated]
    # Tem que estar autenticado

    #---------- Filtro Tipo | Básico ----------
    # def get_queryset(self):
    #     tipo = self.request.query_params.get('tipo')
    #     if tipo:
    #         self.queryset = self.queryset.filter(tipo=tipo)
    #     return self.queryset

    #---------- Filtro Tipo | Declarativos ----------
    filter_backends = [DjangoFilterBackend]
    filterset_class = UsuarioFilter

class ImovelViewSet(ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

    #---------- Filtro Status e Tipo | Básico ----------
    # def get_queryset(self):
    #     status = self.request.query_params.get('status')
    #     tipo = self.request.query_params.get('tipo')

    #     if status:
    #         self.queryset = self.queryset.filter(status=status)
    #     if tipo:
    #         self.queryset = self.queryset.filter(tipo=tipo)
    #     return self.queryset

#---------- Filtro Status e Tipo | Declarativo ----------
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'tipo']

class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

class ContratoViewSet(ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

# Chamando Método com Parâmetro
# @api_view(['GET', 'POST'])
# def listar_usuarios(request):
#     if request.method == 'GET':
#         # query - procura, set - definir
#         queryset = Usuario.objects.all()
#         serializers = UsuarioSerializer(queryset, many=True) # many - vai ter vários usuários
#         return Response(serializers.data)
#     elif request.method == 'POST':
#         serializers = UsuarioSerializer(data = request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)

#-------------- GENERICS --------------
# Outra forma de fazer, mas com a classe
# ListCreateAPIView - tem dois métodos embutidos (GET e POST)

# Usuário
# class UsuarioView(ListCreateAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

# class UsuarioDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

# Imóvel
# class ImovelView(ListCreateAPIView):
#     queryset = Imovel.objects.all()
#     serializer_class = ImovelSerializer

# class ImovelDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Imovel.objects.all()
#     serializer_class = ImovelSerializer

# Contrato
# class ContratoView(ListCreateAPIView):
#     queryset = Contrato.objects.all()
#     serializer_class = ContratoSerializer

# class ContratoDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Contrato.objects.all()
#     serializer_class = ContratoSerializer
    
# Pagamento
# class PagamentoView(ListCreateAPIView):
#     queryset = Pagamento.objects.all()
#     serializer_class = PagamentoSerializer

# class PagamentoDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Pagamento.objects.all()
#     serializer_class = PagamentoSerializer


#-------------- APIView --------------
# Usuario
# class UsuarioView(APIView):
#     def get(self, request): # Aqui o request é obrigatório
#         usuarios = Usuario.objects.all() # Pega tudo da tabela usuários
#         serializer = UsuarioSerializer(usuarios, many=True) # Converter a tabela em JSON
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = UsuarioSerializer(data=request.data) # Armazenar a tabela dentro de uma variável, para transformar em JSON e depois salvar em 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         # Se retornar .data, ele não vai retornar o erro, tem que identificar por olho; com o .errors, ele dá o número do erro

# class UsuarioDetailView(APIView):
#     def get_object(self, pk):
#         return Usuario.objects.get(pk=pk)
    
#     # Não usou request antes, porque no anterior vai pegar só o número, não dados como um todo
#     def get(self, request, pk):
#         usuario = self.get_object(pk)
#         serializer = UsuarioSerializer(usuario)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         usuario = self.get_object(pk)
#         serializer = UsuarioSerializer(usuario, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         usuario = self.get_object(pk)
#         usuario.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # Imoveis
# class ImovelView(APIView):
#     def get(self, request): # Aqui o request é obrigatório
#         imoveis = Imovel.objects.all() # Pega tudo da tabela usuários
#         serializer = ImovelSerializer(imoveis, many=True) # Converter a tabela em JSON
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ImovelSerializer(data=request.data) # Armazenar a tabela dentro de uma variável, para transformar em JSON e depois salvar em 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         # Se retornar .data, ele não vai retornar o erro, tem que identificar por olho; com o .errors, ele dá o número do erro

# class ImovelDetailView(APIView):
#     def get_object(self, pk):
#         return Imovel.objects.get(pk=pk)
    
#     def get(self, request, pk):
#         imovel = self.get_object(pk)
#         serializer = ImovelSerializer(imovel)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         imovel = self.get_object(pk)
#         serializer = ImovelSerializer(imovel, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         imovel = self.get_object(pk)
#         imovel.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # Pagamentos
# class PagamentoView(APIView):
#     def get(self, request): # Aqui o request é obrigatório
#         pagamentos = Pagamento.objects.all() # Pega tudo da tabela usuários
#         serializer = PagamentoSerializer(pagamentos, many=True) # Converter a tabela em JSON
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = PagamentoSerializer(data=request.data) # Armazenar a tabela dentro de uma variável, para transformar em JSON e depois salvar em 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         # Se retornar .data, ele não vai retornar o erro, tem que identificar por olho; com o .errors, ele dá o número do erro
        
# class PagamentoDetailView(APIView):
#     def get_object(self, pk):
#         return Pagamento.objects.get(pk=pk)
    
#     def get(self, request, pk):
#         pagamento = self.get_object(pk)
#         serializer = PagamentoSerializer(pagamento)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         pagamento = self.get_object(pk)
#         serializer = PagamentoSerializer(pagamento, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         pagamento = self.get_object(pk)
#         pagamento.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# # Contratos
# class ContratoView(APIView):
#     def get(self, request): # Aqui o request é obrigatório
#         contratos = Contrato.objects.all() # Pega tudo da tabela usuários
#         serializer = ContratoSerializer(contratos, many=True) # Converter a tabela em JSON
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ContratoSerializer(data=request.data) # Armazenar a tabela dentro de uma variável, para transformar em JSON e depois salvar em 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         # Se retornar .data, ele não vai retornar o erro, tem que identificar por olho; com o .errors, ele dá o número do erro

# class ContratoDetailView(APIView):
#     def get_object(self, pk):
#         return Contrato.objects.get(pk=pk)
    
#     def get(self, request, pk):
#         contrato = self.get_object(pk)
#         serializer = ContratoSerializer(contrato)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         contrato = self.get_object(pk)
#         serializer = ContratoSerializer(contrato, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         contrato = self.get_object(pk)
#         contrato.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)