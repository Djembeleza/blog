from django.urls import (path,
                         include,
                         re_path)
from .views import (IndexView, PostDetailView, PostDeleteView, PostCreateView, PostUpdateView,
                    UserFormView, UserLoginView, UserLogoutView, UserPasswordChangeView, UserPasswordResetConfirmView,
                    UserPasswordResetView)
app_name = 'post'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/posts/', include('post.api.urls')),
    path('sign_in/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('change_passw0rd/', UserPasswordChangeView.as_view(),
         name='account_change_password'),
    path('reset_password/', UserPasswordResetView.as_view(), name='forgot_password'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('register/', UserFormView.as_view(), name="register-user"),
    path('post/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
]
