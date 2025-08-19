from gest_store.models.article import Article
from gest_store.serializers import ArticleSerializer
from rest_framework import viewsets, permissions # type: ignore


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
