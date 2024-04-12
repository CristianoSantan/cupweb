# Generated by Django 5.0.4 on 2024-04-12 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('requisitos', models.TextField()),
                ('jornada_trabalho', models.CharField(max_length=50)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
