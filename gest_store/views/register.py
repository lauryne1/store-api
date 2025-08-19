
from rest_framework.permissions import AllowAny
from rest_framework import generics
from gest_store.models.utilisateur import Utilisateur
from gest_store.serializers import UtilisateurSerializer


class RegisterView(generics.CreateAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [AllowAny]  # Tout le monde peut s'inscrire

    def perform_create(self, serializer):
        serializer.save()