from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from author.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.generic import DetailView
from car.models import CarModel
from car.forms import CommentForm
from author.models import Authormodel
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.   

def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'auth.html', {'form' : form, 'type' : 'Signup'})

class user_login(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'auth.html'
    
    def form_valid(self, form):
        messages.success(self.request, "Logged in Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, "Incorrect login information")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login'
        return context
    
    def get_success_url(self):
        return reverse_lazy('home')

@login_required
def show_profile(request):
    data = Authormodel.objects.filter(buyer_name=request.user   )
    return render(request, 'profile.html', {'data' : data})

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ChangeUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        form = ChangeUserForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form' : form})
            
            
@method_decorator(login_required, name='dispatch')
class buy_product(DetailView):
    model = CarModel
    template_name = 'deatils_view.html'
    pk_url_kwarg = 'id'
    
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(data=self.request.POST)
        data = self.get_object()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = data
            comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_object()
        if data.quantity > 0:
            data.quantity -= 1
            data.save()
            
        Authormodel.objects.create(buyer_name=self.request.user, product=data)
        all_comment = self.get_object()
        comments = all_comment.comments.all()
        context["data"] = data
        context["form"] = CommentForm
        context['comments'] = comments
        return context
    
    
    
# 123456SI
# 123456SJ