from django.urls import path
from .views import IndexView, PostDetailView, PostDeleteView, PostCreateView, PostUpdateView
app_name = 'post'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
]
