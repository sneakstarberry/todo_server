from .models import Todo
from .serializers import TodoSerializer

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet


# ModelViewSet은 ListView와 DetailView에 대한 CRUD가 모두 가능

class TodofilterSet(FilterSet):
    class Meta:
        model = Todo
        fields = {'todo':['exact', 'contains'], 'done': ['exact'], 'due_date':['date__gt']}

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = TodofilterSet

    ordering_fields = ['created_date', 'due_date']
    ordering = ['created_date']

