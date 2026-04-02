from .models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MyUserCreationForm, UserUpdateForm
from django.views.generic import CreateView, UpdateView, DetailView


class UserCreateView(CreateView):
    model=User
    form_class=MyUserCreationForm
    template_name='users/create.html'
    success_url=reverse_lazy('signup')

class UserDetailView(DetailView):
    model=User
    template_name='users/detail.html'
    context_object_name='profile'

class UserUpdateView(LoginRequiredMixin,UpdateView):
    model=User
    form_class=UserUpdateForm
    template_name='users/update.html'

    def get_success_url(self):
        return reverse_lazy('profile_edit', kwargs={'pk': self.object.pk})