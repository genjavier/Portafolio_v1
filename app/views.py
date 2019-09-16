
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from .forms import FormularioLogin
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Cliente
# Create your views here.


def inicio(request):
    return render(request,'index.html')

def index_administrador(request):
    return render(request,'admin_pages/index.html')

def index_empresa(request):
    return render(request,'empresa_pages/index.html')

def index_trabajador(request):
    return render(request,'trabajador_pages/index.html')




    
# Create your views here.
class Login(FormView):
    template_name = 'sesion/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('inicio:index_administrador')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)
    

def logoutUsuario(request):
        logout(request)
        return HttpResponseRedirect('/accounts/login/')







class CourseList(ListView):
    template_name = 'courses/cliente_list.html'
    model = Cliente


class CourseDetail(DetailView):
    model = Cliente


class CourseCreation(CreateView):
    template_name = 'courses/courses_detail.html'
    model = Cliente
    success_url = reverse_lazy('inicio:list')
    fields = ['id','rut', 'nombre', 'correo', 'telefono','numero']


class CourseUpdate(UpdateView):
    model = Cliente
    template_name = 'courses/courses_detail.html'
    success_url = reverse_lazy('inicio:list')
    fields = ['id','rut', 'nombre', 'correo', 'telefono','numero']


class CourseDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy(':list')