from .models import Todo
from .serializers import TodoSerializer

from rest_framework import viewsets


'''
# ReadOnlyModelViewSet은 말 그대로 ListView, DetailView의 조회만 가능
class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
'''
# ModelViewSet은 ListView와 DetailView에 대한 CRUD가 모두 가능

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer