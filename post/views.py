
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
    View)
from django.shortcuts import (
    redirect, render
)
from django.contrib.auth import (
    login,
    authenticate
)
from django.contrib.auth.views import (LoginView,
                                       LogoutView,
                                       PasswordChangeView,
                                       PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView)
from django.contrib.auth.mixins import (LoginRequiredMixin)
from .models import (Post,
                     Report)
from .forms import UserForm
from django.urls import reverse_lazy


class IndexView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post/post_create.html"
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('post:index')


class PostDetailView(DetailView):
    model = Post
    template_name = "post/post_detail.html"


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post/post_delete.html"
    success_url = reverse_lazy('post:index')


class PostUpdateView(UpdateView):
    model = Post
    template_name = "post/post_update.html"
    fields = ['title', 'content']
    success_url = reverse_lazy('post:index')


class ReportCreateView(CreateView):
    model = Report
    template_name = "report_create.html"


class UserLoginView(LoginView):
    template_name = 'registration/login.html'


class UserLogoutView(LogoutView):
    next_page = 'post:index'


class UserFormView(View):
    form_class = UserForm
    template_name = 'registration/registration_form.html'

    # Display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Process the form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # Cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.username = username
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

        # returns User objects if credentials are correct

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('post:index')

        return render(request, self.template_name, {'form': form})


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'account/password_change.html'
    success_url = reverse_lazy('post:index')
    # NOTE: Add a success message that displays after password changed


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('post:user-login')


class UserPasswordResetView(PasswordResetView):
    template_name = 'account/password_reset.html'
    success_url = reverse_lazy('post:user-login')
