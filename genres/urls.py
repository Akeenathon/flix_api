from django.urls import path
from .views import GenreListCreateView, GenreRetrieveUpdateDestroyView


urlpatterns = [
    path('genres/', GenreListCreateView.as_view(), name='genre-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail'),
]
