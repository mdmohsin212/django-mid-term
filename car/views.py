from django.shortcuts import render
from django.views.generic import DetailView
from car.models import CarModel
from car.forms import CommentForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

class details(DetailView):
    model = CarModel
    template_name = 'deatils_view.html'
    pk_url_kwarg = 'id'
    
    @method_decorator(login_required, name='dispatch')
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
        comments = data.comments.all()
        context["data"] = data
        context["form"] = CommentForm
        context['comments'] = comments
        return context
    
    
    