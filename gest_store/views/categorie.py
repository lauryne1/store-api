from gest_store.models.categorie import Categorie
from gest_store.serializer.categorie import CategorieSerializer
from rest_framework import viewsets, permissions



class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Lecture publique, écriture authentifiée