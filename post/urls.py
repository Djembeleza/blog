from django.urls import (path,
                         include)
from .views import (IndexView, PostDetailView, PostDeleteView, PostCreateView, PostUpdateView,
                    UserFormView, UserLoginView, UserLogoutView)
app_name = 'post'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/posts/', include('post.api.urls')),
    path('sign_in/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserFormView.as_view(), name="register-user"),
    path('post/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
]
