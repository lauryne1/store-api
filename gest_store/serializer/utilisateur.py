from gest_store.models.utilisateur import Utilisateur
from rest_framework import serializers


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['id', 'email', 'username', 'negociated_at', 'is_staff', 'is_superuser']
        read_only_fields = ['negociated_at', 'is_staff', 'is_superuser']