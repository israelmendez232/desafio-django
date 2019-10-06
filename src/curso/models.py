from django.db import models

class Apostila(models.Model):    
    titulo = models.CharField(max_length=255) 
    numero = models.IntegerField('Número', blank=True, null=True)
    pdf = models.FileField(upload_to='pdfs', blank=True)    
    def __str__(self):        
        return self.titulo

class Curso(models.Model):    
    titulo = models.CharField(max_length=255)   
    descricao = models.TextField('Descrição', max_length=255, blank=True, null=True)    
    imagem = models.FileField('Imagem', upload_to='imagens', blank=True, null=True)    
    def __str__(self):        
        return self.titulo

class Aula(models.Model):    
    titulo = models.CharField(max_length=255)    
    apostilas = models.ManyToManyField(Apostila, blank=True, related_name='aulas')    
    curso = models.ForeignKey(Curso, blank=True, null=True, on_delete=models.PROTECT)
    numero = models.IntegerField('Número', blank=True, null=True) 
    def __str__(self):        
        return self.titulo
