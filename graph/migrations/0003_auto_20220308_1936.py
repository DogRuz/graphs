# Generated by Django 3.1.5 on 2022-03-08 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0002_auto_20220308_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjacencymatrix',
            name='ancestor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ancestor_graph', to='graph.graphs'),
        ),
    ]
