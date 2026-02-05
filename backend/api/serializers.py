# especifico do rest_framework

from rest_framework import serializers
from .models import Usuario, Imovel, Contrato, Pagamento
# O ponto é pra indicar onde está 

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta: # Trazer todos os Metadados das tabelas
        model = Usuario
        fields = '__all__'

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = '__all__'

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'