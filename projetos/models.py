from django.db import models

class Projeto(models.Model):
    STATUS_CHOICES = [
        ('andamento', 'Em andamento'),
        ('concluido', 'Concluído'),
        ('pausado', 'Pausado'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    data_entrega = models.DateField()

    def __str__(self):
        return self.nome
    
class Tarefa(models.Model):
    projeto = models.ForeignKey('Projeto', on_delete=models.CASCADE, related_name='tarefas')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    concluida = models.BooleanField(default=False)
    prazo = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo