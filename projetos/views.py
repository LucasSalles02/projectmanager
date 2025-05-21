from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from django.urls import reverse_lazy
from .models import Projeto, Tarefa

class ProjetoListView(ListView):
    model = Projeto

class ProjetoCreateView(CreateView):
    model = Projeto
    fields = ['nome', 'descricao', 'status', 'data_entrega']
    success_url = reverse_lazy('projeto_list')

class ProjetoUpdateView(UpdateView):
    model = Projeto
    fields = ['nome', 'descricao', 'status', 'data_entrega']
    template_name = 'projetos/projeto_form.html'
    success_url = reverse_lazy('projeto_list')

class ProjetoDeleteView(DeleteView):
    model = Projeto
    template_name = 'projetos/projeto_confirm_delete.html'
    success_url = reverse_lazy('projeto_list')

class ProjetoDetailView(DetailView):
    model = Projeto
    template_name = 'projetos/projeto_detail.html'

class TarefaCreateView(CreateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'prazo', 'concluida']
    template_name = 'projetos/tarefa_form.html'

    def form_valid(self, form):
        form.instance.projeto_id = self.kwargs['projeto_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('projeto_detail', kwargs={'pk': self.kwargs['projeto_id']})
    
class TarefaUpdateView(UpdateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'prazo', 'concluida']
    template_name = 'projetos/tarefa_form.html'

    def get_success_url(self):
        return reverse_lazy('projeto_detail', kwargs={'pk': self.object.projeto.id})

class TarefaDeleteView(DeleteView):
    model = Tarefa
    template_name = 'projetos/tarefa_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('projeto_detail', kwargs={'pk': self.object.projeto.id})

class TarefaFinalizarView(View):
    def post(self, request, projeto_id, pk):
        tarefa = get_object_or_404(Tarefa, pk=pk, projeto_id=projeto_id)
        tarefa.concluida = True
        tarefa.save()
        return redirect('projeto_detail', pk=tarefa.projeto_id)
