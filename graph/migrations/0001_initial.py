# Generated by Django 3.1.5 on 2022-03-08 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Graphs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_graph', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('value', models.FloatField()),
                ('graph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graph.graphs')),
            ],
        ),
        migrations.CreateModel(
            name='ParentGraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_graph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_graph', to='graph.graphs')),
                ('vector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graph.graphs')),
            ],
        ),
    ]
