from django.contrib import admin
from django.contrib.auth.decorators  import login_required
from django.urls import path 
from django.contrib.auth import views
from . import views
from .views import (
    CourseList,
    CourseDetail,
    CourseCreation,
    CourseUpdate,
    CourseDelete
)
from app.views import Login,logoutUsuario
app_name = 'app'

urlpatterns = [
    path('',Login.as_view()),
    path('administrador/', login_required(views.index_administrador), name='index_administrador'),
    path('trabajador/',  login_required(views.index_trabajador),name='index_trabajador'),
    path('empresa/',  login_required(views.index_empresa),name='index_empresa'),
    
    path('listar/', CourseList.as_view(), name='list'),
    path('<int:pk>/', CourseDetail.as_view(), name='detail'),
    path('nuevo/', CourseCreation.as_view(), name='new'),
    path('editar/<int:pk>/', CourseUpdate.as_view(), name='edit'),
    path('borrar/<int:pk>/', CourseDelete.as_view(), name='delete'),
    # path('',login,{'template_name':'login.html'}, name= 'login')
    
]

 