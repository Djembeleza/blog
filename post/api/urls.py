from django.urls import path
from .views import (PostListAPIView,
                    PostCreateAPIView,
                    PostUpdateAPIView,
                    PostDetailAPIView)

app_name = 'api'

urlpatterns = [
    path('', PostListAPIView.as_view(), name='api-list'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='detail'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('<int:pk>/update/', PostUpdateAPIView.as_view(), name='update'),
]
