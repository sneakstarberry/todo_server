from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from list import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('todo', views.TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('todo/', views.TodoViewSet.as_view(), name="todo")
]

# urlpatterns = format_suffix_patterns(urlpatterns)
