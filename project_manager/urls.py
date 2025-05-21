"""
URL configuration for project_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from projetos.views import (
    ProjetoListView, ProjetoCreateView, ProjetoUpdateView,
    ProjetoDeleteView, ProjetoDetailView, TarefaCreateView,
    TarefaUpdateView, TarefaDeleteView, TarefaFinalizarView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProjetoListView.as_view(), name='projeto_list'),
    path('create/', ProjetoCreateView.as_view(), name='projeto_create'),
    path('edit/<int:pk>/', ProjetoUpdateView.as_view(), name='projeto_edit'),
    path('delete/<int:pk>/', ProjetoDeleteView.as_view(), name='projeto_delete'),
    path('<int:pk>/', ProjetoDetailView.as_view(), name='projeto_detail'),  
    path('<int:projeto_id>/tarefas/nova/', TarefaCreateView.as_view(), name='tarefa_create'),
    path('<int:projeto_id>/tarefas/<int:pk>/editar/', TarefaUpdateView.as_view(), name='tarefa_edit'),
    path('<int:projeto_id>/tarefas/<int:pk>/excluir/', TarefaDeleteView.as_view(), name='tarefa_delete'),
    path('<int:projeto_id>/tarefas/<int:pk>/finalizar/', TarefaFinalizarView.as_view(), name='tarefa_finalizar'),
]

