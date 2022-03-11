from django.db import models

# Create your models here.
from graph.models import Graphs


class Operations(models.Model):
    name_operation = models.TextField()


class ResultGraph(models.Model):
    graph = models.ForeignKey(Graphs, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operations, on_delete=models.CASCADE)