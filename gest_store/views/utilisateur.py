from gest_store.models.utilisateur import Utilisateur
from rest_framework import viewsets, permissions # type: ignore

from gest_store.serializers import UtilisateurSerializer

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [permissions.IsAdminUser]  # Seuls les admins peuvent gérer les utilisateurs